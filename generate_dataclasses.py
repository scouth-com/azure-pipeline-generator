import json
from typing import List, Optional, Any, Union


# File paths
SCHEMA_FILE = "azure_pipelines_generator/schema/azure_pipelines_schema.json"
OUTPUT_FILE = "azure_pipelines_generator/models/azure_pipelines_models.py"


def resolve_type(json_type: str) -> str:
    """Map JSON Schema types to Python types."""
    type_mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict",
        "array": "List",
    }
    return type_mapping.get(json_type, "Any")


def parse_properties(properties: dict, required: List[str]) -> List[str]:
    """Parse properties and generate dataclass fields."""
    fields = []
    for name, details in properties.items():
        if "$ref" in details:
            py_type = details["$ref"].split("/")[-1].capitalize()
        elif details.get("type") == "array" and "items" in details:
            if "$ref" in details["items"]:
                item_type = details["items"]["$ref"].split("/")[-1].capitalize()
                py_type = f"List[{item_type}]"
            else:
                item_type = details["items"].get("type", "Any")
                py_type = f"List[{resolve_type(item_type)}]"
        else:
            json_type = details.get("type", "Any")
            py_type = resolve_type(json_type)

        if name not in required:
            py_type = f"Optional[{py_type}]"
            default_value = " = None"
        else:
            default_value = ""

        description = details.get("description", "").replace("\n", " ")
        deprecation = details.get("deprecationMessage", "")
        comment = f"  # {description}{' (Deprecated: ' + deprecation + ')' if deprecation else ''}"
        fields.append(f"    {name}: {py_type}{default_value}{comment}")
    return fields


def generate_dataclass(name: str, properties: dict, required: List[str]) -> str:
    """Generate a Python dataclass from JSON Schema properties."""
    fields = parse_properties(properties, required)
    fields_code = "\n".join(fields)
    return f"@dataclass\nclass {name}:\n{fields_code or '    pass'}\n"


def handle_anyof(name: str, variations: List[dict]) -> str:
    """Generate a base class and manage `anyOf` variations."""
    union_types = []
    subclasses = []
    base_class = ""

    for idx, variation in enumerate(variations, 1):
        if "$ref" in variation:
            ref_name = variation["$ref"].split("/")[-1].capitalize()
            union_types.append(ref_name)
        elif variation.get("type") == "object":
            properties = variation.get("properties", {})
            required = variation.get("required", [])
            subclass_name = f"{name}Variant{idx}"
            union_types.append(subclass_name)
            subclass = generate_dataclass(subclass_name, properties, required)
            subclasses.append(subclass)
        elif variation.get("type") in ["string", "integer", "boolean", "array"]:
            primitive_type = resolve_type(variation["type"])
            if primitive_type == "List":
                union_types.append("List[Any]")
            else:
                union_types.append(primitive_type)
        else:
            subclasses.append(f"# Unsupported variation for {name}, index {idx}\n")

    # Generate the Union type if there are multiple valid variations
    if union_types:
        union_annotation = f"Union[{', '.join(union_types)}]"
        base_class = f"{name} = {union_annotation}\n\n"

    return base_class + "\n\n".join(subclasses)


def process_schema(schema: dict, output_file: str):
    """Process JSON Schema to generate Python dataclasses."""
    definitions = schema.get("definitions", {})
    dataclasses = []

    for key, definition in definitions.items():
        name = key.capitalize()

        if "anyOf" in definition:
            # Handle anyOf with subclasses and Union
            anyof_output = handle_anyof(name, definition["anyOf"])
            dataclasses.append(anyof_output)
        elif definition.get("type") == "object":
            properties = definition.get("properties", {})
            required = definition.get("required", [])
            dataclasses.append(generate_dataclass(name, properties, required))
        elif definition.get("type") == "array" and "items" in definition:
            # Handle arrays with $ref or primitive types
            if "$ref" in definition["items"]:
                item_type = definition["items"]["$ref"].split("/")[-1].capitalize()
                py_type = f"List[{item_type}]"
            else:
                item_type = definition["items"].get("type", "Any")
                py_type = f"List[{resolve_type(item_type)}]"
            deprecation = definition.get("deprecationMessage", "")
            comment = f"  # Deprecated: {deprecation}" if deprecation else ""
            dataclasses.append(f"@dataclass\nclass {name}:\n    items: {py_type}{comment}\n")
        else:
            dataclasses.append(f"# Unsupported type for {name}\n")

    # Write to the output file
    with open(output_file, "w") as f:
        f.write("from dataclasses import dataclass\nfrom typing import List, Optional, Any, Union\n\n")
        f.write("\n\n".join(dataclasses))
        print(f"Dataclasses written to {output_file}")


# Main execution
if __name__ == "__main__":
    with open(SCHEMA_FILE, "r") as schema_file:
        schema = json.load(schema_file)

    process_schema(schema, OUTPUT_FILE)
