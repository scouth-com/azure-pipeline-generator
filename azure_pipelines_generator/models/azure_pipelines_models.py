from typing import Optional, List, Dict
from enum import Enum


class BranchClass:
    ref: Optional[str]

    def __init__(self, ref: Optional[str]) -> None:
        self.ref = ref


class AnyAnyOf:
    type: Optional[str]
    items: Optional[BranchClass]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], items: Optional[BranchClass], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.items = items
        self.additional_properties = additional_properties


class AnyClass:
    any_of: Optional[List[AnyAnyOf]]

    def __init__(self, any_of: Optional[List[AnyAnyOf]]) -> None:
        self.any_of = any_of


class AnyAllowExpressions:
    any_of: Optional[List[AnyAnyOf]]

    def __init__(self, any_of: Optional[List[AnyAnyOf]]) -> None:
        self.any_of = any_of


class AnyOfIgnoreCase(Enum):
    VALUE = "value"


class BranchFilterType(Enum):
    BOOLEAN = "boolean"
    INTEGER = "integer"
    STRING = "string"


class BooleanAnyOf:
    type: Optional[BranchFilterType]
    ignore_case: Optional[AnyOfIgnoreCase]
    pattern: Optional[str]

    def __init__(self, type: Optional[BranchFilterType], ignore_case: Optional[AnyOfIgnoreCase], pattern: Optional[str]) -> None:
        self.type = type
        self.ignore_case = ignore_case
        self.pattern = pattern


class Boolean:
    any_of: Optional[List[BooleanAnyOf]]

    def __init__(self, any_of: Optional[List[BooleanAnyOf]]) -> None:
        self.any_of = any_of


class BranchFilter:
    type: Optional[BranchFilterType]
    description: Optional[str]
    pattern: Optional[str]

    def __init__(self, type: Optional[BranchFilterType], description: Optional[str], pattern: Optional[str]) -> None:
        self.type = type
        self.description = description
        self.pattern = pattern


class BranchFilterArray:
    type: Optional[str]
    items: Optional[BranchClass]

    def __init__(self, type: Optional[str], items: Optional[BranchClass]) -> None:
        self.type = type
        self.items = items


class BuildRef(Enum):
    DEFINITIONS_REFERENCE_NAME = "#/definitions/referenceName"


class Build:
    description: Optional[str]
    ref: Optional[BuildRef]

    def __init__(self, description: Optional[str], ref: Optional[BuildRef]) -> None:
        self.description = description
        self.ref = ref


class ConnectionRef(Enum):
    DEFINITIONS_NON_EMPTY_STRING = "#/definitions/nonEmptyString"


class Connection:
    description: Optional[str]
    ref: Optional[ConnectionRef]

    def __init__(self, description: Optional[str], ref: Optional[ConnectionRef]) -> None:
        self.description = description
        self.ref = ref


class DeployClass:
    description: Optional[str]
    ref: Optional[str]

    def __init__(self, description: Optional[str], ref: Optional[str]) -> None:
        self.description = description
        self.ref = ref


class BuildResourceProperties:
    build: Optional[Build]
    type: Optional[Connection]
    connection: Optional[Connection]
    source: Optional[Connection]
    version: Optional[BranchClass]
    branch: Optional[BranchClass]
    trigger: Optional[DeployClass]

    def __init__(self, build: Optional[Build], type: Optional[Connection], connection: Optional[Connection], source: Optional[Connection], version: Optional[BranchClass], branch: Optional[BranchClass], trigger: Optional[DeployClass]) -> None:
        self.build = build
        self.type = type
        self.connection = connection
        self.source = source
        self.version = version
        self.branch = branch
        self.trigger = trigger


class BuildResourceType(Enum):
    OBJECT = "object"


class BuildResource:
    type: Optional[BuildResourceType]
    properties: Optional[BuildResourceProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[BuildResourceProperties], additional_properties: Optional[bool], first_property: Optional[List[str]], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.required = required


class LegacyRepoResourceAlias:
    type: Optional[BranchFilterType]
    pattern: Optional[str]

    def __init__(self, type: Optional[BranchFilterType], pattern: Optional[str]) -> None:
        self.type = type
        self.pattern = pattern


class BuildResourceTrigger:
    any_of: Optional[List[LegacyRepoResourceAlias]]

    def __init__(self, any_of: Optional[List[LegacyRepoResourceAlias]]) -> None:
        self.any_of = any_of


class TemplateClass:
    ref: Optional[ConnectionRef]

    def __init__(self, ref: Optional[ConnectionRef]) -> None:
        self.ref = ref


class CanaryDeploymentIncrements:
    type: Optional[str]
    items: Optional[TemplateClass]

    def __init__(self, type: Optional[str], items: Optional[TemplateClass]) -> None:
        self.type = type
        self.items = items


class CanaryDeploymentStrategyProperties:
    increments: Optional[DeployClass]
    pre_deploy: Optional[DeployClass]
    deploy: Optional[DeployClass]
    route_traffic: Optional[DeployClass]
    post_route_traffic: Optional[DeployClass]
    on: Optional[DeployClass]

    def __init__(self, increments: Optional[DeployClass], pre_deploy: Optional[DeployClass], deploy: Optional[DeployClass], route_traffic: Optional[DeployClass], post_route_traffic: Optional[DeployClass], on: Optional[DeployClass]) -> None:
        self.increments = increments
        self.pre_deploy = pre_deploy
        self.deploy = deploy
        self.route_traffic = route_traffic
        self.post_route_traffic = post_route_traffic
        self.on = on


class CanaryDeploymentStrategy:
    type: Optional[BuildResourceType]
    properties: Optional[CanaryDeploymentStrategyProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[CanaryDeploymentStrategyProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class EnvRef(Enum):
    DEFINITIONS_MAPPING_OF_STRING_STRING = "#/definitions/mappingOfStringString"


class InputsClass:
    description: Optional[str]
    ref: Optional[EnvRef]

    def __init__(self, description: Optional[str], ref: Optional[EnvRef]) -> None:
        self.description = description
        self.ref = ref


class ImageRef(Enum):
    DEFINITIONS_STRING = "#/definitions/string"


class Image:
    description: Optional[str]
    ref: Optional[ImageRef]
    examples: Optional[List[str]]

    def __init__(self, description: Optional[str], ref: Optional[ImageRef], examples: Optional[List[str]]) -> None:
        self.description = description
        self.ref = ref
        self.examples = examples


class MapDockerSocketRef(Enum):
    DEFINITIONS_BOOLEAN = "#/definitions/boolean"


class MapDockerSocket:
    description: Optional[str]
    ref: Optional[MapDockerSocketRef]

    def __init__(self, description: Optional[str], ref: Optional[MapDockerSocketRef]) -> None:
        self.description = description
        self.ref = ref


class ContainerBaseProperties:
    endpoint: Optional[DeployClass]
    env: Optional[InputsClass]
    image: Optional[Image]
    map_docker_socket: Optional[MapDockerSocket]
    options: Optional[DeployClass]
    ports: Optional[BranchClass]
    volumes: Optional[BranchClass]
    mount_read_only: Optional[BranchClass]

    def __init__(self, endpoint: Optional[DeployClass], env: Optional[InputsClass], image: Optional[Image], map_docker_socket: Optional[MapDockerSocket], options: Optional[DeployClass], ports: Optional[BranchClass], volumes: Optional[BranchClass], mount_read_only: Optional[BranchClass]) -> None:
        self.endpoint = endpoint
        self.env = env
        self.image = image
        self.map_docker_socket = map_docker_socket
        self.options = options
        self.ports = ports
        self.volumes = volumes
        self.mount_read_only = mount_read_only


class ContainerBase:
    type: Optional[BuildResourceType]
    properties: Optional[ContainerBaseProperties]
    additional_properties: Optional[bool]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[ContainerBaseProperties], additional_properties: Optional[bool], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.required = required


class ContainerResourceProperties:
    container: Optional[Build]
    type: Optional[BranchClass]
    trigger: Optional[BranchClass]
    endpoint: Optional[DeployClass]
    env: Optional[InputsClass]
    image: Optional[Image]
    map_docker_socket: Optional[MapDockerSocket]
    options: Optional[DeployClass]
    ports: Optional[BranchClass]
    volumes: Optional[BranchClass]
    mount_read_only: Optional[BranchClass]

    def __init__(self, container: Optional[Build], type: Optional[BranchClass], trigger: Optional[BranchClass], endpoint: Optional[DeployClass], env: Optional[InputsClass], image: Optional[Image], map_docker_socket: Optional[MapDockerSocket], options: Optional[DeployClass], ports: Optional[BranchClass], volumes: Optional[BranchClass], mount_read_only: Optional[BranchClass]) -> None:
        self.container = container
        self.type = type
        self.trigger = trigger
        self.endpoint = endpoint
        self.env = env
        self.image = image
        self.map_docker_socket = map_docker_socket
        self.options = options
        self.ports = ports
        self.volumes = volumes
        self.mount_read_only = mount_read_only


class ContainerResource:
    type: Optional[BuildResourceType]
    properties: Optional[ContainerResourceProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[ContainerResourceProperties], additional_properties: Optional[bool], first_property: Optional[List[str]], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.required = required


class Always:
    ref: Optional[MapDockerSocketRef]

    def __init__(self, ref: Optional[MapDockerSocketRef]) -> None:
        self.ref = ref


class PurpleProperties:
    enabled: Optional[Always]
    tags: Optional[BranchClass]

    def __init__(self, enabled: Optional[Always], tags: Optional[BranchClass]) -> None:
        self.enabled = enabled
        self.tags = tags


class ContainerResourceTriggerAnyOf:
    type: Optional[str]
    pattern: Optional[str]
    properties: Optional[PurpleProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], pattern: Optional[str], properties: Optional[PurpleProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.pattern = pattern
        self.properties = properties
        self.additional_properties = additional_properties


class ContainerResourceTrigger:
    any_of: Optional[List[ContainerResourceTriggerAnyOf]]

    def __init__(self, any_of: Optional[List[ContainerResourceTriggerAnyOf]]) -> None:
        self.any_of = any_of


class DeployHookProperties:
    steps: Optional[DeployClass]
    pool: Optional[DeployClass]

    def __init__(self, steps: Optional[DeployClass], pool: Optional[DeployClass]) -> None:
        self.steps = steps
        self.pool = pool


class Hook:
    type: Optional[BuildResourceType]
    properties: Optional[DeployHookProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[DeployHookProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class FluffyProperties:
    name: Optional[Connection]
    resource_name: Optional[Connection]
    resource_id: Optional[Connection]
    resource_type: Optional[Connection]
    tags: Optional[Connection]

    def __init__(self, name: Optional[Connection], resource_name: Optional[Connection], resource_id: Optional[Connection], resource_type: Optional[Connection], tags: Optional[Connection]) -> None:
        self.name = name
        self.resource_name = resource_name
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tags = tags


class DeploymentEnvironmentAnyOf:
    type: Optional[str]
    properties: Optional[FluffyProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], properties: Optional[FluffyProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class DeploymentEnvironment:
    description: Optional[str]
    any_of: Optional[List[DeploymentEnvironmentAnyOf]]

    def __init__(self, description: Optional[str], any_of: Optional[List[DeploymentEnvironmentAnyOf]]) -> None:
        self.description = description
        self.any_of = any_of


class TentacledProperties:
    run_once: Optional[DeployClass]
    rolling: Optional[DeployClass]
    canary: Optional[DeployClass]

    def __init__(self, run_once: Optional[DeployClass], rolling: Optional[DeployClass], canary: Optional[DeployClass]) -> None:
        self.run_once = run_once
        self.rolling = rolling
        self.canary = canary


class DeploymentStrategyAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[TentacledProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[TentacledProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class DeploymentStrategy:
    any_of: Optional[List[DeploymentStrategyAnyOf]]

    def __init__(self, any_of: Optional[List[DeploymentStrategyAnyOf]]) -> None:
        self.any_of = any_of


class ExplicitResourcesProperties:
    repositories: Optional[DeployClass]
    pools: Optional[DeployClass]

    def __init__(self, repositories: Optional[DeployClass], pools: Optional[DeployClass]) -> None:
        self.repositories = repositories
        self.pools = pools


class ExplicitResources:
    type: Optional[BuildResourceType]
    properties: Optional[ExplicitResourcesProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[ExplicitResourcesProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class ExtendsProperties:
    template: Optional[TemplateClass]
    parameters: Optional[DeployClass]

    def __init__(self, template: Optional[TemplateClass], parameters: Optional[DeployClass]) -> None:
        self.template = template
        self.parameters = parameters


class Extends:
    type: Optional[BuildResourceType]
    properties: Optional[ExtendsProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[ExtendsProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class StickyProperties:
    stages: Optional[BranchClass]
    trigger: Optional[BranchClass]
    resources: Optional[BranchClass]
    parameters: Optional[BranchClass]
    variables: Optional[BranchClass]
    jobs: Optional[BranchClass]
    steps: Optional[BranchClass]
    extends: Optional[BranchClass]

    def __init__(self, stages: Optional[BranchClass], trigger: Optional[BranchClass], resources: Optional[BranchClass], parameters: Optional[BranchClass], variables: Optional[BranchClass], jobs: Optional[BranchClass], steps: Optional[BranchClass], extends: Optional[BranchClass]) -> None:
        self.stages = stages
        self.trigger = trigger
        self.resources = resources
        self.parameters = parameters
        self.variables = variables
        self.jobs = jobs
        self.steps = steps
        self.extends = extends


class ExtendsTemplateAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[StickyProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[StickyProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class ExtendsTemplate:
    any_of: Optional[List[ExtendsTemplateAnyOf]]

    def __init__(self, any_of: Optional[List[ExtendsTemplateAnyOf]]) -> None:
        self.any_of = any_of


class ExtendsTemplateBaseProperties:
    trigger: Optional[BranchClass]
    resources: Optional[BranchClass]
    parameters: Optional[BranchClass]
    variables: Optional[BranchClass]

    def __init__(self, trigger: Optional[BranchClass], resources: Optional[BranchClass], parameters: Optional[BranchClass], variables: Optional[BranchClass]) -> None:
        self.trigger = trigger
        self.resources = resources
        self.parameters = parameters
        self.variables = variables


class ExtendsTemplateBase:
    type: Optional[BuildResourceType]
    properties: Optional[ExtendsTemplateBaseProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[ExtendsTemplateBaseProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class IncludeExcludeFiltersProperties:
    include: Optional[BranchClass]
    exclude: Optional[BranchClass]

    def __init__(self, include: Optional[BranchClass], exclude: Optional[BranchClass]) -> None:
        self.include = include
        self.exclude = exclude


class IncludeExcludeFilters:
    type: Optional[BuildResourceType]
    properties: Optional[IncludeExcludeFiltersProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[IncludeExcludeFiltersProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class IncludeExcludeStringFiltersAnyOf:
    type: Optional[str]
    items: Optional[TemplateClass]
    properties: Optional[IncludeExcludeFiltersProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], items: Optional[TemplateClass], properties: Optional[IncludeExcludeFiltersProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.items = items
        self.properties = properties
        self.additional_properties = additional_properties


class IncludeExcludeStringFilters:
    any_of: Optional[List[IncludeExcludeStringFiltersAnyOf]]

    def __init__(self, any_of: Optional[List[IncludeExcludeStringFiltersAnyOf]]) -> None:
        self.any_of = any_of


class FetchDepth:
    description: Optional[str]
    ref: Optional[ImageRef]

    def __init__(self, description: Optional[str], ref: Optional[ImageRef]) -> None:
        self.description = description
        self.ref = ref


class ContinueOnErrorDescription(Enum):
    CONTINUE_RUNNING_EVEN_ON_FAILURE = "Continue running even on failure?"


class PurpleContinueOnError:
    description: Optional[ContinueOnErrorDescription]
    ref: Optional[str]

    def __init__(self, description: Optional[ContinueOnErrorDescription], ref: Optional[str]) -> None:
        self.description = description
        self.ref = ref


class DisplayName:
    ref: Optional[ImageRef]

    def __init__(self, ref: Optional[ImageRef]) -> None:
        self.ref = ref


class IndigoProperties:
    job: Optional[Build]
    display_name: Optional[FetchDepth]
    depends_on: Optional[DeployClass]
    condition: Optional[FetchDepth]
    continue_on_error: Optional[PurpleContinueOnError]
    timeout_in_minutes: Optional[Connection]
    cancel_timeout_in_minutes: Optional[Connection]
    variables: Optional[DeployClass]
    strategy: Optional[DeployClass]
    pool: Optional[DeployClass]
    container: Optional[DeployClass]
    services: Optional[DeployClass]
    workspace: Optional[DeployClass]
    uses: Optional[DeployClass]
    steps: Optional[DeployClass]
    template_context: Optional[BranchClass]
    deployment: Optional[DisplayName]
    environment: Optional[BranchClass]
    template: Optional[Connection]
    parameters: Optional[DeployClass]

    def __init__(self, job: Optional[Build], display_name: Optional[FetchDepth], depends_on: Optional[DeployClass], condition: Optional[FetchDepth], continue_on_error: Optional[PurpleContinueOnError], timeout_in_minutes: Optional[Connection], cancel_timeout_in_minutes: Optional[Connection], variables: Optional[DeployClass], strategy: Optional[DeployClass], pool: Optional[DeployClass], container: Optional[DeployClass], services: Optional[DeployClass], workspace: Optional[DeployClass], uses: Optional[DeployClass], steps: Optional[DeployClass], template_context: Optional[BranchClass], deployment: Optional[DisplayName], environment: Optional[BranchClass], template: Optional[Connection], parameters: Optional[DeployClass]) -> None:
        self.job = job
        self.display_name = display_name
        self.depends_on = depends_on
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.timeout_in_minutes = timeout_in_minutes
        self.cancel_timeout_in_minutes = cancel_timeout_in_minutes
        self.variables = variables
        self.strategy = strategy
        self.pool = pool
        self.container = container
        self.services = services
        self.workspace = workspace
        self.uses = uses
        self.steps = steps
        self.template_context = template_context
        self.deployment = deployment
        self.environment = environment
        self.template = template
        self.parameters = parameters


class JobAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[IndigoProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[IndigoProperties], additional_properties: Optional[bool], first_property: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property


class Job:
    any_of: Optional[List[JobAnyOf]]

    def __init__(self, any_of: Optional[List[JobAnyOf]]) -> None:
        self.any_of = any_of


class IndecentProperties:
    alias: Optional[FetchDepth]
    endpoint: Optional[DeployClass]
    env: Optional[InputsClass]
    image: Optional[Image]
    map_docker_socket: Optional[MapDockerSocket]
    options: Optional[DeployClass]
    ports: Optional[BranchClass]
    volumes: Optional[BranchClass]
    mount_read_only: Optional[BranchClass]

    def __init__(self, alias: Optional[FetchDepth], endpoint: Optional[DeployClass], env: Optional[InputsClass], image: Optional[Image], map_docker_socket: Optional[MapDockerSocket], options: Optional[DeployClass], ports: Optional[BranchClass], volumes: Optional[BranchClass], mount_read_only: Optional[BranchClass]) -> None:
        self.alias = alias
        self.endpoint = endpoint
        self.env = env
        self.image = image
        self.map_docker_socket = map_docker_socket
        self.options = options
        self.ports = ports
        self.volumes = volumes
        self.mount_read_only = mount_read_only


class JobContainerAnyOf:
    type: Optional[str]
    properties: Optional[IndecentProperties]
    additional_properties: Optional[bool]
    required: Optional[List[str]]

    def __init__(self, type: Optional[str], properties: Optional[IndecentProperties], additional_properties: Optional[bool], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.required = required


class JobContainer:
    any_of: Optional[List[JobContainerAnyOf]]

    def __init__(self, any_of: Optional[List[JobContainerAnyOf]]) -> None:
        self.any_of = any_of


class JobContinueOnError:
    type: Optional[BranchFilterType]

    def __init__(self, type: Optional[BranchFilterType]) -> None:
        self.type = type


class JobDecoratorStepsProperties:
    steps: Optional[DeployClass]

    def __init__(self, steps: Optional[DeployClass]) -> None:
        self.steps = steps


class JobDecoratorSteps:
    type: Optional[BuildResourceType]
    properties: Optional[JobDecoratorStepsProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[JobDecoratorStepsProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class JobDependsOnAnyOf:
    type: Optional[str]
    items: Optional[DisplayName]

    def __init__(self, type: Optional[str], items: Optional[DisplayName]) -> None:
        self.type = type
        self.items = items


class JobDependsOn:
    any_of: Optional[List[JobDependsOnAnyOf]]

    def __init__(self, any_of: Optional[List[JobDependsOnAnyOf]]) -> None:
        self.any_of = any_of


class PatternProperties:
    a_za_z0_9_: Optional[BranchClass]

    def __init__(self, a_za_z0_9_: Optional[BranchClass]) -> None:
        self.a_za_z0_9_ = a_za_z0_9_


class JobMatrixAnyOf:
    type: Optional[str]
    additional_properties: Optional[bool]
    min_properties: Optional[int]
    pattern_properties: Optional[PatternProperties]

    def __init__(self, type: Optional[str], additional_properties: Optional[bool], min_properties: Optional[int], pattern_properties: Optional[PatternProperties]) -> None:
        self.type = type
        self.additional_properties = additional_properties
        self.min_properties = min_properties
        self.pattern_properties = pattern_properties


class JobMatrix:
    any_of: Optional[List[JobMatrixAnyOf]]

    def __init__(self, any_of: Optional[List[JobMatrixAnyOf]]) -> None:
        self.any_of = any_of


class JobServices:
    type: Optional[BuildResourceType]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.additional_properties = additional_properties


class HilariousProperties:
    matrix: Optional[BranchClass]
    max_parallel: Optional[Connection]
    parallel: Optional[Connection]

    def __init__(self, matrix: Optional[BranchClass], max_parallel: Optional[Connection], parallel: Optional[Connection]) -> None:
        self.matrix = matrix
        self.max_parallel = max_parallel
        self.parallel = parallel


class JobStrategyAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[HilariousProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[HilariousProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class JobStrategy:
    any_of: Optional[List[JobStrategyAnyOf]]

    def __init__(self, any_of: Optional[List[JobStrategyAnyOf]]) -> None:
        self.any_of = any_of


class CommandsClass:
    description: Optional[str]
    enum: Optional[List[str]]
    ref: Optional[ImageRef]

    def __init__(self, description: Optional[str], enum: Optional[List[str]], ref: Optional[ImageRef]) -> None:
        self.description = description
        self.enum = enum
        self.ref = ref


class JobWorkspaceProperties:
    clean: Optional[CommandsClass]

    def __init__(self, clean: Optional[CommandsClass]) -> None:
        self.clean = clean


class JobWorkspace:
    type: Optional[BuildResourceType]
    properties: Optional[JobWorkspaceProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[JobWorkspaceProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class QueueClass:
    description: Optional[str]
    deprecation_message: Optional[str]
    do_not_suggest: Optional[bool]
    ref: Optional[str]

    def __init__(self, description: Optional[str], deprecation_message: Optional[str], do_not_suggest: Optional[bool], ref: Optional[str]) -> None:
        self.description = description
        self.deprecation_message = deprecation_message
        self.do_not_suggest = do_not_suggest
        self.ref = ref


class AmbitiousProperties:
    parameters: Optional[DeployClass]
    jobs: Optional[DeployClass]
    phases: Optional[QueueClass]

    def __init__(self, parameters: Optional[DeployClass], jobs: Optional[DeployClass], phases: Optional[QueueClass]) -> None:
        self.parameters = parameters
        self.jobs = jobs
        self.phases = phases


class JobsTemplateAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[AmbitiousProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[AmbitiousProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class JobsTemplate:
    any_of: Optional[List[JobsTemplateAnyOf]]

    def __init__(self, any_of: Optional[List[JobsTemplateAnyOf]]) -> None:
        self.any_of = any_of


class WorkspaceRepoClass:
    description: Optional[str]
    enum: Optional[List[bool]]
    ref: Optional[ImageRef]

    def __init__(self, description: Optional[str], enum: Optional[List[bool]], ref: Optional[ImageRef]) -> None:
        self.description = description
        self.enum = enum
        self.ref = ref


class LegacyResourceProperties:
    repo: Optional[BranchClass]
    clean: Optional[WorkspaceRepoClass]
    fetch_depth: Optional[FetchDepth]
    lfs: Optional[FetchDepth]

    def __init__(self, repo: Optional[BranchClass], clean: Optional[WorkspaceRepoClass], fetch_depth: Optional[FetchDepth], lfs: Optional[FetchDepth]) -> None:
        self.repo = repo
        self.clean = clean
        self.fetch_depth = fetch_depth
        self.lfs = lfs


class LegacyResource:
    type: Optional[BuildResourceType]
    properties: Optional[LegacyResourceProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[LegacyResourceProperties], additional_properties: Optional[bool], first_property: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property


class MatrixProperties:
    type: Optional[BuildResourceType]
    description: Optional[str]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], description: Optional[str], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.description = description
        self.additional_properties = additional_properties


class OnSuccessOrFailureHookProperties:
    failure: Optional[DeployClass]
    success: Optional[DeployClass]

    def __init__(self, failure: Optional[DeployClass], success: Optional[DeployClass]) -> None:
        self.failure = failure
        self.success = success


class OnSuccessOrFailureHook:
    type: Optional[BuildResourceType]
    properties: Optional[OnSuccessOrFailureHookProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[OnSuccessOrFailureHookProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class PackageResourceProperties:
    package: Optional[Build]
    type: Optional[Connection]
    connection: Optional[Connection]
    name: Optional[Connection]
    version: Optional[BranchClass]
    tag: Optional[BranchClass]
    trigger: Optional[DeployClass]

    def __init__(self, package: Optional[Build], type: Optional[Connection], connection: Optional[Connection], name: Optional[Connection], version: Optional[BranchClass], tag: Optional[BranchClass], trigger: Optional[DeployClass]) -> None:
        self.package = package
        self.type = type
        self.connection = connection
        self.name = name
        self.version = version
        self.tag = tag
        self.trigger = trigger


class PackageResource:
    type: Optional[BuildResourceType]
    properties: Optional[PackageResourceProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[PackageResourceProperties], additional_properties: Optional[bool], first_property: Optional[List[str]], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.required = required


class CunningProperties:
    parameters: Optional[DeployClass]
    steps: Optional[DeployClass]
    jobs: Optional[DeployClass]
    stages: Optional[BranchClass]
    resources: Optional[BranchClass]
    extends: Optional[DeployClass]

    def __init__(self, parameters: Optional[DeployClass], steps: Optional[DeployClass], jobs: Optional[DeployClass], stages: Optional[BranchClass], resources: Optional[BranchClass], extends: Optional[DeployClass]) -> None:
        self.parameters = parameters
        self.steps = steps
        self.jobs = jobs
        self.stages = stages
        self.resources = resources
        self.extends = extends


class ParametersTemplateAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[CunningProperties]
    additional_properties: Optional[bool]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[CunningProperties], additional_properties: Optional[bool], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.required = required


class ParametersTemplate:
    any_of: Optional[List[ParametersTemplateAnyOf]]

    def __init__(self, any_of: Optional[List[ParametersTemplateAnyOf]]) -> None:
        self.any_of = any_of


class MagentaProperties:
    phase: Optional[Build]
    depends_on: Optional[DeployClass]
    display_name: Optional[FetchDepth]
    condition: Optional[FetchDepth]
    continue_on_error: Optional[PurpleContinueOnError]
    queue: Optional[QueueClass]
    variables: Optional[DeployClass]
    steps: Optional[DeployClass]
    server: Optional[QueueClass]
    template: Optional[Connection]
    parameters: Optional[DeployClass]

    def __init__(self, phase: Optional[Build], depends_on: Optional[DeployClass], display_name: Optional[FetchDepth], condition: Optional[FetchDepth], continue_on_error: Optional[PurpleContinueOnError], queue: Optional[QueueClass], variables: Optional[DeployClass], steps: Optional[DeployClass], server: Optional[QueueClass], template: Optional[Connection], parameters: Optional[DeployClass]) -> None:
        self.phase = phase
        self.depends_on = depends_on
        self.display_name = display_name
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.queue = queue
        self.variables = variables
        self.steps = steps
        self.server = server
        self.template = template
        self.parameters = parameters


class PhaseAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[MagentaProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[MagentaProperties], additional_properties: Optional[bool], first_property: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property


class Phase:
    deprecation_message: Optional[str]
    any_of: Optional[List[PhaseAnyOf]]

    def __init__(self, deprecation_message: Optional[str], any_of: Optional[List[PhaseAnyOf]]) -> None:
        self.deprecation_message = deprecation_message
        self.any_of = any_of


class FriskyProperties:
    cancel_timeout_in_minutes: Optional[Connection]
    container: Optional[Connection]
    demands: Optional[DeployClass]
    matrix: Optional[BranchClass]
    name: Optional[FetchDepth]
    parallel: Optional[Connection]
    timeout_in_minutes: Optional[Connection]
    workspace: Optional[BranchClass]

    def __init__(self, cancel_timeout_in_minutes: Optional[Connection], container: Optional[Connection], demands: Optional[DeployClass], matrix: Optional[BranchClass], name: Optional[FetchDepth], parallel: Optional[Connection], timeout_in_minutes: Optional[Connection], workspace: Optional[BranchClass]) -> None:
        self.cancel_timeout_in_minutes = cancel_timeout_in_minutes
        self.container = container
        self.demands = demands
        self.matrix = matrix
        self.name = name
        self.parallel = parallel
        self.timeout_in_minutes = timeout_in_minutes
        self.workspace = workspace


class PhaseQueueTargetAnyOf:
    type: Optional[str]
    properties: Optional[FriskyProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], properties: Optional[FriskyProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class PhaseQueueTarget:
    description: Optional[str]
    deprecation_message: Optional[str]
    any_of: Optional[List[PhaseQueueTargetAnyOf]]

    def __init__(self, description: Optional[str], deprecation_message: Optional[str], any_of: Optional[List[PhaseQueueTargetAnyOf]]) -> None:
        self.description = description
        self.deprecation_message = deprecation_message
        self.any_of = any_of


class MischievousProperties:
    cancel_timeout_in_minutes: Optional[Connection]
    matrix: Optional[BranchClass]
    parallel: Optional[Connection]
    timeout_in_minutes: Optional[Connection]

    def __init__(self, cancel_timeout_in_minutes: Optional[Connection], matrix: Optional[BranchClass], parallel: Optional[Connection], timeout_in_minutes: Optional[Connection]) -> None:
        self.cancel_timeout_in_minutes = cancel_timeout_in_minutes
        self.matrix = matrix
        self.parallel = parallel
        self.timeout_in_minutes = timeout_in_minutes


class PhaseServerTargetAnyOf:
    type: Optional[str]
    properties: Optional[MischievousProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], properties: Optional[MischievousProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class PhaseServerTarget:
    any_of: Optional[List[PhaseServerTargetAnyOf]]

    def __init__(self, any_of: Optional[List[PhaseServerTargetAnyOf]]) -> None:
        self.any_of = any_of


class PhaseTargetDemands:
    any_of: Optional[List[CanaryDeploymentIncrements]]

    def __init__(self, any_of: Optional[List[CanaryDeploymentIncrements]]) -> None:
        self.any_of = any_of


class PhaseTargetMatrixAnyOf:
    type: Optional[str]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.additional_properties = additional_properties


class PhaseTargetMatrix:
    description: Optional[str]
    any_of: Optional[List[PhaseTargetMatrixAnyOf]]
    min_properties: Optional[int]
    pattern_properties: Optional[PatternProperties]

    def __init__(self, description: Optional[str], any_of: Optional[List[PhaseTargetMatrixAnyOf]], min_properties: Optional[int], pattern_properties: Optional[PatternProperties]) -> None:
        self.description = description
        self.any_of = any_of
        self.min_properties = min_properties
        self.pattern_properties = pattern_properties


class PhaseTargetWorkspace:
    type: Optional[BuildResourceType]
    properties: Optional[JobWorkspaceProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[JobWorkspaceProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class DefinitionsPhases:
    type: Optional[str]
    deprecation_message: Optional[str]
    items: Optional[BranchClass]

    def __init__(self, type: Optional[str], deprecation_message: Optional[str], items: Optional[BranchClass]) -> None:
        self.type = type
        self.deprecation_message = deprecation_message
        self.items = items


class BraggadociousProperties:
    stages: Optional[DeployClass]
    pool: Optional[DeployClass]
    name: Optional[DeployClass]
    append_commit_message_to_run_name: Optional[MapDockerSocket]
    trigger: Optional[DeployClass]
    parameters: Optional[DeployClass]
    pr: Optional[DeployClass]
    schedules: Optional[BranchClass]
    resources: Optional[DeployClass]
    variables: Optional[DeployClass]
    lock_behavior: Optional[DeployClass]
    extends: Optional[DeployClass]
    jobs: Optional[DeployClass]
    phases: Optional[QueueClass]
    strategy: Optional[DeployClass]
    continue_on_error: Optional[PurpleContinueOnError]
    container: Optional[DeployClass]
    services: Optional[BranchClass]
    workspace: Optional[BranchClass]
    steps: Optional[DeployClass]
    queue: Optional[QueueClass]
    server: Optional[QueueClass]

    def __init__(self, stages: Optional[DeployClass], pool: Optional[DeployClass], name: Optional[DeployClass], append_commit_message_to_run_name: Optional[MapDockerSocket], trigger: Optional[DeployClass], parameters: Optional[DeployClass], pr: Optional[DeployClass], schedules: Optional[BranchClass], resources: Optional[DeployClass], variables: Optional[DeployClass], lock_behavior: Optional[DeployClass], extends: Optional[DeployClass], jobs: Optional[DeployClass], phases: Optional[QueueClass], strategy: Optional[DeployClass], continue_on_error: Optional[PurpleContinueOnError], container: Optional[DeployClass], services: Optional[BranchClass], workspace: Optional[BranchClass], steps: Optional[DeployClass], queue: Optional[QueueClass], server: Optional[QueueClass]) -> None:
        self.stages = stages
        self.pool = pool
        self.name = name
        self.append_commit_message_to_run_name = append_commit_message_to_run_name
        self.trigger = trigger
        self.parameters = parameters
        self.pr = pr
        self.schedules = schedules
        self.resources = resources
        self.variables = variables
        self.lock_behavior = lock_behavior
        self.extends = extends
        self.jobs = jobs
        self.phases = phases
        self.strategy = strategy
        self.continue_on_error = continue_on_error
        self.container = container
        self.services = services
        self.workspace = workspace
        self.steps = steps
        self.queue = queue
        self.server = server


class PipelineAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[BraggadociousProperties]
    additional_properties: Optional[bool]
    required: Optional[List[str]]
    deprecation_message: Optional[str]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[BraggadociousProperties], additional_properties: Optional[bool], required: Optional[List[str]], deprecation_message: Optional[str]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.required = required
        self.deprecation_message = deprecation_message


class Pipeline:
    any_of: Optional[List[PipelineAnyOf]]

    def __init__(self, any_of: Optional[List[PipelineAnyOf]]) -> None:
        self.any_of = any_of


class PipelineAnyBaseProperties:
    trigger: Optional[DeployClass]
    name: Optional[DeployClass]
    append_commit_message_to_run_name: Optional[DeployClass]
    parameters: Optional[DeployClass]
    pr: Optional[DeployClass]
    schedules: Optional[BranchClass]
    resources: Optional[DeployClass]
    variables: Optional[DeployClass]
    stages: Optional[BranchClass]
    jobs: Optional[DeployClass]
    extends: Optional[DeployClass]
    phases: Optional[QueueClass]
    strategy: Optional[DeployClass]
    continue_on_error: Optional[PurpleContinueOnError]
    pool: Optional[DeployClass]
    container: Optional[DeployClass]
    services: Optional[BranchClass]
    workspace: Optional[BranchClass]
    steps: Optional[DeployClass]
    queue: Optional[QueueClass]
    server: Optional[QueueClass]
    lock_behavior: Optional[DeployClass]

    def __init__(self, trigger: Optional[DeployClass], name: Optional[DeployClass], append_commit_message_to_run_name: Optional[DeployClass], parameters: Optional[DeployClass], pr: Optional[DeployClass], schedules: Optional[BranchClass], resources: Optional[DeployClass], variables: Optional[DeployClass], stages: Optional[BranchClass], jobs: Optional[DeployClass], extends: Optional[DeployClass], phases: Optional[QueueClass], strategy: Optional[DeployClass], continue_on_error: Optional[PurpleContinueOnError], pool: Optional[DeployClass], container: Optional[DeployClass], services: Optional[BranchClass], workspace: Optional[BranchClass], steps: Optional[DeployClass], queue: Optional[QueueClass], server: Optional[QueueClass], lock_behavior: Optional[DeployClass]) -> None:
        self.trigger = trigger
        self.name = name
        self.append_commit_message_to_run_name = append_commit_message_to_run_name
        self.parameters = parameters
        self.pr = pr
        self.schedules = schedules
        self.resources = resources
        self.variables = variables
        self.stages = stages
        self.jobs = jobs
        self.extends = extends
        self.phases = phases
        self.strategy = strategy
        self.continue_on_error = continue_on_error
        self.pool = pool
        self.container = container
        self.services = services
        self.workspace = workspace
        self.steps = steps
        self.queue = queue
        self.server = server
        self.lock_behavior = lock_behavior


class PipelineAnyBaseClass:
    type: Optional[BuildResourceType]
    properties: Optional[PipelineAnyBaseProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[PipelineAnyBaseProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class PipelineBaseProperties:
    name: Optional[DeployClass]
    append_commit_message_to_run_name: Optional[MapDockerSocket]
    trigger: Optional[DeployClass]
    parameters: Optional[DeployClass]
    pr: Optional[DeployClass]
    schedules: Optional[BranchClass]
    resources: Optional[DeployClass]
    variables: Optional[DeployClass]
    lock_behavior: Optional[DeployClass]

    def __init__(self, name: Optional[DeployClass], append_commit_message_to_run_name: Optional[MapDockerSocket], trigger: Optional[DeployClass], parameters: Optional[DeployClass], pr: Optional[DeployClass], schedules: Optional[BranchClass], resources: Optional[DeployClass], variables: Optional[DeployClass], lock_behavior: Optional[DeployClass]) -> None:
        self.name = name
        self.append_commit_message_to_run_name = append_commit_message_to_run_name
        self.trigger = trigger
        self.parameters = parameters
        self.pr = pr
        self.schedules = schedules
        self.resources = resources
        self.variables = variables
        self.lock_behavior = lock_behavior


class PipelineBase:
    type: Optional[BuildResourceType]
    properties: Optional[PipelineBaseProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[PipelineBaseProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class PipelineResourceProperties:
    pipeline: Optional[Build]
    project: Optional[TemplateClass]
    source: Optional[TemplateClass]
    version: Optional[BranchClass]
    branch: Optional[BranchClass]
    tags: Optional[BranchClass]
    trigger: Optional[BranchClass]

    def __init__(self, pipeline: Optional[Build], project: Optional[TemplateClass], source: Optional[TemplateClass], version: Optional[BranchClass], branch: Optional[BranchClass], tags: Optional[BranchClass], trigger: Optional[BranchClass]) -> None:
        self.pipeline = pipeline
        self.project = project
        self.source = source
        self.version = version
        self.branch = branch
        self.tags = tags
        self.trigger = trigger


class PipelineResource:
    type: Optional[BuildResourceType]
    properties: Optional[PipelineResourceProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[PipelineResourceProperties], additional_properties: Optional[bool], first_property: Optional[List[str]], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.required = required


class Properties1:
    enabled: Optional[Always]
    branches: Optional[BranchClass]
    stages: Optional[BranchClass]
    tags: Optional[BranchClass]

    def __init__(self, enabled: Optional[Always], branches: Optional[BranchClass], stages: Optional[BranchClass], tags: Optional[BranchClass]) -> None:
        self.enabled = enabled
        self.branches = branches
        self.stages = stages
        self.tags = tags


class PipelineResourceTriggerAnyOf:
    type: Optional[str]
    pattern: Optional[str]
    properties: Optional[Properties1]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], pattern: Optional[str], properties: Optional[Properties1], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.pattern = pattern
        self.properties = properties
        self.additional_properties = additional_properties


class PipelineResourceTrigger:
    any_of: Optional[List[PipelineResourceTriggerAnyOf]]

    def __init__(self, any_of: Optional[List[PipelineResourceTriggerAnyOf]]) -> None:
        self.any_of = any_of


class PipelineTemplateParameterProperties:
    name: Optional[TemplateClass]
    display_name: Optional[FetchDepth]
    type: Optional[BranchClass]
    default: Optional[BranchClass]
    values: Optional[BranchClass]

    def __init__(self, name: Optional[TemplateClass], display_name: Optional[FetchDepth], type: Optional[BranchClass], default: Optional[BranchClass], values: Optional[BranchClass]) -> None:
        self.name = name
        self.display_name = display_name
        self.type = type
        self.default = default
        self.values = values


class TemplateParameter:
    type: Optional[BuildResourceType]
    properties: Optional[PipelineTemplateParameterProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[PipelineTemplateParameterProperties], additional_properties: Optional[bool], first_property: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property


class Properties2:
    name: Optional[Connection]
    demands: Optional[DeployClass]

    def __init__(self, name: Optional[Connection], demands: Optional[DeployClass]) -> None:
        self.name = name
        self.demands = demands


class PoolAnyOf:
    type: Optional[str]
    properties: Optional[Properties2]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], properties: Optional[Properties2], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class Pool:
    description: Optional[str]
    any_of: Optional[List[PoolAnyOf]]

    def __init__(self, description: Optional[str], any_of: Optional[List[PoolAnyOf]]) -> None:
        self.description = description
        self.any_of = any_of


class PoolDemands:
    any_of: Optional[List[CanaryDeploymentIncrements]]

    def __init__(self, any_of: Optional[List[CanaryDeploymentIncrements]]) -> None:
        self.any_of = any_of


class Properties3:
    auto_cancel: Optional[MapDockerSocket]
    branches: Optional[BranchClass]
    paths: Optional[BranchClass]
    drafts: Optional[MapDockerSocket]

    def __init__(self, auto_cancel: Optional[MapDockerSocket], branches: Optional[BranchClass], paths: Optional[BranchClass], drafts: Optional[MapDockerSocket]) -> None:
        self.auto_cancel = auto_cancel
        self.branches = branches
        self.paths = paths
        self.drafts = drafts


class PRAnyOf:
    type: Optional[str]
    pattern: Optional[str]
    items: Optional[BranchClass]
    properties: Optional[Properties3]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], pattern: Optional[str], items: Optional[BranchClass], properties: Optional[Properties3], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.pattern = pattern
        self.items = items
        self.properties = properties
        self.additional_properties = additional_properties


class PR:
    any_of: Optional[List[PRAnyOf]]

    def __init__(self, any_of: Optional[List[PRAnyOf]]) -> None:
        self.any_of = any_of


class ReadOnlyMountsProperties:
    work: Optional[MapDockerSocket]
    externals: Optional[MapDockerSocket]
    tools: Optional[MapDockerSocket]
    tasks: Optional[MapDockerSocket]

    def __init__(self, work: Optional[MapDockerSocket], externals: Optional[MapDockerSocket], tools: Optional[MapDockerSocket], tasks: Optional[MapDockerSocket]) -> None:
        self.work = work
        self.externals = externals
        self.tools = tools
        self.tasks = tasks


class ReadOnlyMounts:
    type: Optional[BuildResourceType]
    properties: Optional[ReadOnlyMountsProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[ReadOnlyMountsProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class RepositoryCheckoutOptionsProperties:
    clean: Optional[WorkspaceRepoClass]
    fetch_depth: Optional[FetchDepth]
    fetch_tags: Optional[FetchDepth]
    lfs: Optional[FetchDepth]
    submodules: Optional[FetchDepth]
    persist_credentials: Optional[FetchDepth]

    def __init__(self, clean: Optional[WorkspaceRepoClass], fetch_depth: Optional[FetchDepth], fetch_tags: Optional[FetchDepth], lfs: Optional[FetchDepth], submodules: Optional[FetchDepth], persist_credentials: Optional[FetchDepth]) -> None:
        self.clean = clean
        self.fetch_depth = fetch_depth
        self.fetch_tags = fetch_tags
        self.lfs = lfs
        self.submodules = submodules
        self.persist_credentials = persist_credentials


class RepositoryCheckoutOptions:
    type: Optional[BuildResourceType]
    properties: Optional[RepositoryCheckoutOptionsProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[RepositoryCheckoutOptionsProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class CheckoutOptions:
    deprecation_message: Optional[str]
    do_not_suggest: Optional[bool]
    ref: Optional[str]

    def __init__(self, deprecation_message: Optional[str], do_not_suggest: Optional[bool], ref: Optional[str]) -> None:
        self.deprecation_message = deprecation_message
        self.do_not_suggest = do_not_suggest
        self.ref = ref


class RepositoryResourceProperties:
    repository: Optional[Build]
    endpoint: Optional[Connection]
    trigger: Optional[BranchClass]
    checkout_options: Optional[CheckoutOptions]
    ref: Optional[BranchClass]

    def __init__(self, repository: Optional[Build], endpoint: Optional[Connection], trigger: Optional[BranchClass], checkout_options: Optional[CheckoutOptions], ref: Optional[BranchClass]) -> None:
        self.repository = repository
        self.endpoint = endpoint
        self.trigger = trigger
        self.checkout_options = checkout_options
        self.ref = ref


class RepositoryResource:
    type: Optional[BuildResourceType]
    properties: Optional[RepositoryResourceProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[RepositoryResourceProperties], additional_properties: Optional[bool], first_property: Optional[List[str]], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.required = required


class Properties4:
    builds: Optional[DeployClass]
    containers: Optional[DeployClass]
    pipelines: Optional[BranchClass]
    repositories: Optional[DeployClass]
    webhooks: Optional[DeployClass]
    packages: Optional[DeployClass]

    def __init__(self, builds: Optional[DeployClass], containers: Optional[DeployClass], pipelines: Optional[BranchClass], repositories: Optional[DeployClass], webhooks: Optional[DeployClass], packages: Optional[DeployClass]) -> None:
        self.builds = builds
        self.containers = containers
        self.pipelines = pipelines
        self.repositories = repositories
        self.webhooks = webhooks
        self.packages = packages


class ResourcesAnyOf:
    type: Optional[str]
    properties: Optional[Properties4]
    additional_properties: Optional[bool]
    items: Optional[BranchClass]

    def __init__(self, type: Optional[str], properties: Optional[Properties4], additional_properties: Optional[bool], items: Optional[BranchClass]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.items = items


class Resources:
    any_of: Optional[List[ResourcesAnyOf]]

    def __init__(self, any_of: Optional[List[ResourcesAnyOf]]) -> None:
        self.any_of = any_of


class RollingDeploymentStrategyProperties:
    max_parallel: Optional[Connection]
    pre_deploy: Optional[DeployClass]
    deploy: Optional[DeployClass]
    route_traffic: Optional[DeployClass]
    post_route_traffic: Optional[DeployClass]
    on: Optional[DeployClass]

    def __init__(self, max_parallel: Optional[Connection], pre_deploy: Optional[DeployClass], deploy: Optional[DeployClass], route_traffic: Optional[DeployClass], post_route_traffic: Optional[DeployClass], on: Optional[DeployClass]) -> None:
        self.max_parallel = max_parallel
        self.pre_deploy = pre_deploy
        self.deploy = deploy
        self.route_traffic = route_traffic
        self.post_route_traffic = post_route_traffic
        self.on = on


class RollingDeploymentStrategy:
    type: Optional[BuildResourceType]
    properties: Optional[RollingDeploymentStrategyProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[RollingDeploymentStrategyProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class RunOnceDeploymentStrategyProperties:
    pre_deploy: Optional[DeployClass]
    deploy: Optional[DeployClass]
    route_traffic: Optional[DeployClass]
    post_route_traffic: Optional[DeployClass]
    on: Optional[DeployClass]

    def __init__(self, pre_deploy: Optional[DeployClass], deploy: Optional[DeployClass], route_traffic: Optional[DeployClass], post_route_traffic: Optional[DeployClass], on: Optional[DeployClass]) -> None:
        self.pre_deploy = pre_deploy
        self.deploy = deploy
        self.route_traffic = route_traffic
        self.post_route_traffic = post_route_traffic
        self.on = on


class RunOnceDeploymentStrategy:
    type: Optional[BuildResourceType]
    properties: Optional[RunOnceDeploymentStrategyProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[RunOnceDeploymentStrategyProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class ScheduleProperties:
    cron: Optional[TemplateClass]
    display_name: Optional[DisplayName]
    branches: Optional[BranchClass]
    batch: Optional[Always]
    always: Optional[Always]

    def __init__(self, cron: Optional[TemplateClass], display_name: Optional[DisplayName], branches: Optional[BranchClass], batch: Optional[Always], always: Optional[Always]) -> None:
        self.cron = cron
        self.display_name = display_name
        self.branches = branches
        self.batch = batch
        self.always = always


class Schedule:
    type: Optional[BuildResourceType]
    properties: Optional[ScheduleProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[ScheduleProperties], additional_properties: Optional[bool], first_property: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property


class Properties5:
    stage: Optional[FetchDepth]
    display_name: Optional[FetchDepth]
    pool: Optional[DeployClass]
    depends_on: Optional[DeployClass]
    condition: Optional[FetchDepth]
    variables: Optional[DeployClass]
    jobs: Optional[DeployClass]
    lock_behavior: Optional[DeployClass]
    trigger: Optional[DeployClass]
    is_skippable: Optional[MapDockerSocket]
    template_context: Optional[BranchClass]
    template: Optional[Connection]
    parameters: Optional[DeployClass]

    def __init__(self, stage: Optional[FetchDepth], display_name: Optional[FetchDepth], pool: Optional[DeployClass], depends_on: Optional[DeployClass], condition: Optional[FetchDepth], variables: Optional[DeployClass], jobs: Optional[DeployClass], lock_behavior: Optional[DeployClass], trigger: Optional[DeployClass], is_skippable: Optional[MapDockerSocket], template_context: Optional[BranchClass], template: Optional[Connection], parameters: Optional[DeployClass]) -> None:
        self.stage = stage
        self.display_name = display_name
        self.pool = pool
        self.depends_on = depends_on
        self.condition = condition
        self.variables = variables
        self.jobs = jobs
        self.lock_behavior = lock_behavior
        self.trigger = trigger
        self.is_skippable = is_skippable
        self.template_context = template_context
        self.template = template
        self.parameters = parameters


class StageAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[Properties5]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[Properties5], additional_properties: Optional[bool], first_property: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property


class Stage:
    any_of: Optional[List[StageAnyOf]]

    def __init__(self, any_of: Optional[List[StageAnyOf]]) -> None:
        self.any_of = any_of


class StagesTemplateProperties:
    parameters: Optional[BranchClass]
    stages: Optional[BranchClass]

    def __init__(self, parameters: Optional[BranchClass], stages: Optional[BranchClass]) -> None:
        self.parameters = parameters
        self.stages = stages


class StagesTemplate:
    type: Optional[BuildResourceType]
    properties: Optional[StagesTemplateProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[StagesTemplateProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class FluffyContinueOnError:
    description: Optional[ContinueOnErrorDescription]
    ref: Optional[MapDockerSocketRef]

    def __init__(self, description: Optional[ContinueOnErrorDescription], ref: Optional[MapDockerSocketRef]) -> None:
        self.description = description
        self.ref = ref


class DisplayNameDescription(Enum):
    HUMAN_READABLE_NAME_FOR_THE_TASK = "Human-readable name for the task"


class PurpleDisplayName:
    description: Optional[DisplayNameDescription]
    ref: Optional[ImageRef]

    def __init__(self, description: Optional[DisplayNameDescription], ref: Optional[ImageRef]) -> None:
        self.description = description
        self.ref = ref


class EnabledDescription(Enum):
    RUN_THIS_TASK_WHEN_THE_JOB_RUNS = "Run this task when the job runs?"


class PurpleEnabled:
    description: Optional[EnabledDescription]
    ref: Optional[MapDockerSocketRef]

    def __init__(self, description: Optional[EnabledDescription], ref: Optional[MapDockerSocketRef]) -> None:
        self.description = description
        self.ref = ref


class EnvDescription(Enum):
    VARIABLES_TO_MAP_INTO_THE_PROCESS_S_ENVIRONMENT = "Variables to map into the process's environment"


class PurpleEnv:
    description: Optional[EnvDescription]
    ref: Optional[EnvRef]

    def __init__(self, description: Optional[EnvDescription], ref: Optional[EnvRef]) -> None:
        self.description = description
        self.ref = ref


class NameDescription(Enum):
    ID_OF_THE_STEP = "ID of the step"


class Name:
    description: Optional[NameDescription]
    ref: Optional[BuildRef]

    def __init__(self, description: Optional[NameDescription], ref: Optional[BuildRef]) -> None:
        self.description = description
        self.ref = ref


class RetryCountOnTaskFailureDescription(Enum):
    NUMBER_OF_RETRIES_IF_THE_TASK_FAILS = "Number of retries if the task fails"


class PurpleRetryCountOnTaskFailure:
    description: Optional[RetryCountOnTaskFailureDescription]
    ref: Optional[ImageRef]

    def __init__(self, description: Optional[RetryCountOnTaskFailureDescription], ref: Optional[ImageRef]) -> None:
        self.description = description
        self.ref = ref


class TargetDescription(Enum):
    ENVIRONMENT_IN_WHICH_TO_RUN_THIS_TASK = "Environment in which to run this task"


class TargetRef(Enum):
    DEFINITIONS_STEP_TARGET = "#/definitions/stepTarget"


class Target:
    description: Optional[TargetDescription]
    ref: Optional[TargetRef]

    def __init__(self, description: Optional[TargetDescription], ref: Optional[TargetRef]) -> None:
        self.description = description
        self.ref = ref


class Upload:
    deprecation_message: Optional[str]
    do_not_suggest: Optional[bool]
    ref: Optional[ImageRef]

    def __init__(self, deprecation_message: Optional[str], do_not_suggest: Optional[bool], ref: Optional[ImageRef]) -> None:
        self.deprecation_message = deprecation_message
        self.do_not_suggest = do_not_suggest
        self.ref = ref


class Properties6:
    script: Optional[FetchDepth]
    fail_on_stderr: Optional[FetchDepth]
    working_directory: Optional[FetchDepth]
    condition: Optional[FetchDepth]
    continue_on_error: Optional[FluffyContinueOnError]
    display_name: Optional[PurpleDisplayName]
    target: Optional[Target]
    enabled: Optional[PurpleEnabled]
    env: Optional[PurpleEnv]
    name: Optional[Name]
    timeout_in_minutes: Optional[Connection]
    retry_count_on_task_failure: Optional[PurpleRetryCountOnTaskFailure]
    powershell: Optional[FetchDepth]
    error_action_preference: Optional[DisplayName]
    ignore_lastexitcode: Optional[FetchDepth]
    pwsh: Optional[FetchDepth]
    bash: Optional[FetchDepth]
    checkout: Optional[FetchDepth]
    clean: Optional[WorkspaceRepoClass]
    fetch_depth: Optional[FetchDepth]
    fetch_filter: Optional[FetchDepth]
    fetch_tags: Optional[FetchDepth]
    lfs: Optional[FetchDepth]
    persist_credentials: Optional[FetchDepth]
    submodules: Optional[FetchDepth]
    path: Optional[FetchDepth]
    workspace_repo: Optional[WorkspaceRepoClass]
    download: Optional[Connection]
    artifact: Optional[DeployClass]
    patterns: Optional[DeployClass]
    download_build: Optional[Connection]
    inputs: Optional[InputsClass]
    get_package: Optional[Connection]
    upload: Optional[Upload]
    publish: Optional[DisplayName]
    template: Optional[Connection]
    parameters: Optional[DeployClass]
    review_app: Optional[DisplayName]

    def __init__(self, script: Optional[FetchDepth], fail_on_stderr: Optional[FetchDepth], working_directory: Optional[FetchDepth], condition: Optional[FetchDepth], continue_on_error: Optional[FluffyContinueOnError], display_name: Optional[PurpleDisplayName], target: Optional[Target], enabled: Optional[PurpleEnabled], env: Optional[PurpleEnv], name: Optional[Name], timeout_in_minutes: Optional[Connection], retry_count_on_task_failure: Optional[PurpleRetryCountOnTaskFailure], powershell: Optional[FetchDepth], error_action_preference: Optional[DisplayName], ignore_lastexitcode: Optional[FetchDepth], pwsh: Optional[FetchDepth], bash: Optional[FetchDepth], checkout: Optional[FetchDepth], clean: Optional[WorkspaceRepoClass], fetch_depth: Optional[FetchDepth], fetch_filter: Optional[FetchDepth], fetch_tags: Optional[FetchDepth], lfs: Optional[FetchDepth], persist_credentials: Optional[FetchDepth], submodules: Optional[FetchDepth], path: Optional[FetchDepth], workspace_repo: Optional[WorkspaceRepoClass], download: Optional[Connection], artifact: Optional[DeployClass], patterns: Optional[DeployClass], download_build: Optional[Connection], inputs: Optional[InputsClass], get_package: Optional[Connection], upload: Optional[Upload], publish: Optional[DisplayName], template: Optional[Connection], parameters: Optional[DeployClass], review_app: Optional[DisplayName]) -> None:
        self.script = script
        self.fail_on_stderr = fail_on_stderr
        self.working_directory = working_directory
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.display_name = display_name
        self.target = target
        self.enabled = enabled
        self.env = env
        self.name = name
        self.timeout_in_minutes = timeout_in_minutes
        self.retry_count_on_task_failure = retry_count_on_task_failure
        self.powershell = powershell
        self.error_action_preference = error_action_preference
        self.ignore_lastexitcode = ignore_lastexitcode
        self.pwsh = pwsh
        self.bash = bash
        self.checkout = checkout
        self.clean = clean
        self.fetch_depth = fetch_depth
        self.fetch_filter = fetch_filter
        self.fetch_tags = fetch_tags
        self.lfs = lfs
        self.persist_credentials = persist_credentials
        self.submodules = submodules
        self.path = path
        self.workspace_repo = workspace_repo
        self.download = download
        self.artifact = artifact
        self.patterns = patterns
        self.download_build = download_build
        self.inputs = inputs
        self.get_package = get_package
        self.upload = upload
        self.publish = publish
        self.template = template
        self.parameters = parameters
        self.review_app = review_app


class StepAnyOf:
    type: Optional[BuildResourceType]
    ref: Optional[str]
    properties: Optional[Properties6]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], ref: Optional[str], properties: Optional[Properties6], additional_properties: Optional[bool], first_property: Optional[List[str]], required: Optional[List[str]]) -> None:
        self.type = type
        self.ref = ref
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.required = required


class Step:
    any_of: Optional[List[StepAnyOf]]

    def __init__(self, any_of: Optional[List[StepAnyOf]]) -> None:
        self.any_of = any_of


class Properties7:
    container: Optional[Connection]
    commands: Optional[CommandsClass]
    settable_variables: Optional[DeployClass]

    def __init__(self, container: Optional[Connection], commands: Optional[CommandsClass], settable_variables: Optional[DeployClass]) -> None:
        self.container = container
        self.commands = commands
        self.settable_variables = settable_variables


class StepTargetAnyOf:
    type: Optional[str]
    properties: Optional[Properties7]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], properties: Optional[Properties7], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class StepTarget:
    description: Optional[str]
    any_of: Optional[List[StepTargetAnyOf]]

    def __init__(self, description: Optional[str], any_of: Optional[List[StepTargetAnyOf]]) -> None:
        self.description = description
        self.any_of = any_of


class StepsTemplateProperties:
    parameters: Optional[DeployClass]
    steps: Optional[DeployClass]

    def __init__(self, parameters: Optional[DeployClass], steps: Optional[DeployClass]) -> None:
        self.parameters = parameters
        self.steps = steps


class StepsTemplate:
    type: Optional[BuildResourceType]
    properties: Optional[StepsTemplateProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[StepsTemplateProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class FirstProperty(Enum):
    INPUTS = "inputs"
    TASK = "task"


class PropertyIgnoreCase(Enum):
    ALL = "all"
    KEY = "key"


class Property:
    description: Optional[str]
    ignore_case: Optional[PropertyIgnoreCase]
    enum: Optional[List[str]]
    type: Optional[BranchFilterType]
    aliases: Optional[List[str]]

    def __init__(self, description: Optional[str], ignore_case: Optional[PropertyIgnoreCase], enum: Optional[List[str]], type: Optional[BranchFilterType], aliases: Optional[List[str]]) -> None:
        self.description = description
        self.ignore_case = ignore_case
        self.enum = enum
        self.type = type
        self.aliases = aliases


class PurpleInputs:
    description: Optional[str]
    properties: Optional[Dict[str, Property]]
    additional_properties: Optional[bool]
    required: Optional[List[str]]

    def __init__(self, description: Optional[str], properties: Optional[Dict[str, Property]], additional_properties: Optional[bool], required: Optional[List[str]]) -> None:
        self.description = description
        self.properties = properties
        self.additional_properties = additional_properties
        self.required = required


class PurpleTask:
    description: Optional[str]
    ignore_case: Optional[AnyOfIgnoreCase]
    pattern: Optional[str]

    def __init__(self, description: Optional[str], ignore_case: Optional[AnyOfIgnoreCase], pattern: Optional[str]) -> None:
        self.description = description
        self.ignore_case = ignore_case
        self.pattern = pattern


class Properties8:
    task: Optional[PurpleTask]
    inputs: Optional[PurpleInputs]

    def __init__(self, task: Optional[PurpleTask], inputs: Optional[PurpleInputs]) -> None:
        self.task = task
        self.inputs = inputs


class PurpleAnyOf:
    properties: Optional[Properties8]
    do_not_suggest: Optional[bool]
    first_property: Optional[List[FirstProperty]]
    required: Optional[List[FirstProperty]]
    deprecation_message: Optional[str]

    def __init__(self, properties: Optional[Properties8], do_not_suggest: Optional[bool], first_property: Optional[List[FirstProperty]], required: Optional[List[FirstProperty]], deprecation_message: Optional[str]) -> None:
        self.properties = properties
        self.do_not_suggest = do_not_suggest
        self.first_property = first_property
        self.required = required
        self.deprecation_message = deprecation_message


class Condition:
    type: Optional[BranchFilterType]
    description: Optional[str]

    def __init__(self, type: Optional[BranchFilterType], description: Optional[str]) -> None:
        self.type = type
        self.description = description


class FluffyDisplayName:
    type: Optional[BranchFilterType]
    description: Optional[DisplayNameDescription]

    def __init__(self, type: Optional[BranchFilterType], description: Optional[DisplayNameDescription]) -> None:
        self.type = type
        self.description = description


class FluffyEnabled:
    type: Optional[BranchFilterType]
    description: Optional[EnabledDescription]

    def __init__(self, type: Optional[BranchFilterType], description: Optional[EnabledDescription]) -> None:
        self.type = type
        self.description = description


class FluffyEnv:
    type: Optional[BuildResourceType]
    description: Optional[EnvDescription]

    def __init__(self, type: Optional[BuildResourceType], description: Optional[EnvDescription]) -> None:
        self.type = type
        self.description = description


class FluffyInputs:
    type: Optional[BuildResourceType]
    description: Optional[str]

    def __init__(self, type: Optional[BuildResourceType], description: Optional[str]) -> None:
        self.type = type
        self.description = description


class FluffyRetryCountOnTaskFailure:
    type: Optional[BranchFilterType]
    description: Optional[RetryCountOnTaskFailureDescription]

    def __init__(self, type: Optional[BranchFilterType], description: Optional[RetryCountOnTaskFailureDescription]) -> None:
        self.type = type
        self.description = description


class FluffyAnyOf:
    description: Optional[str]
    do_not_suggest: Optional[bool]
    ignore_case: Optional[AnyOfIgnoreCase]
    enum: Optional[List[str]]
    deprecation_message: Optional[str]

    def __init__(self, description: Optional[str], do_not_suggest: Optional[bool], ignore_case: Optional[AnyOfIgnoreCase], enum: Optional[List[str]], deprecation_message: Optional[str]) -> None:
        self.description = description
        self.do_not_suggest = do_not_suggest
        self.ignore_case = ignore_case
        self.enum = enum
        self.deprecation_message = deprecation_message


class FluffyTask:
    any_of: Optional[List[FluffyAnyOf]]

    def __init__(self, any_of: Optional[List[FluffyAnyOf]]) -> None:
        self.any_of = any_of


class TaskProperties:
    task: Optional[FluffyTask]
    display_name: Optional[FluffyDisplayName]
    name: Optional[BranchFilter]
    condition: Optional[Condition]
    continue_on_error: Optional[Condition]
    enabled: Optional[FluffyEnabled]
    retry_count_on_task_failure: Optional[FluffyRetryCountOnTaskFailure]
    timeout_in_minutes: Optional[Condition]
    inputs: Optional[FluffyInputs]
    env: Optional[FluffyEnv]

    def __init__(self, task: Optional[FluffyTask], display_name: Optional[FluffyDisplayName], name: Optional[BranchFilter], condition: Optional[Condition], continue_on_error: Optional[Condition], enabled: Optional[FluffyEnabled], retry_count_on_task_failure: Optional[FluffyRetryCountOnTaskFailure], timeout_in_minutes: Optional[Condition], inputs: Optional[FluffyInputs], env: Optional[FluffyEnv]) -> None:
        self.task = task
        self.display_name = display_name
        self.name = name
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.enabled = enabled
        self.retry_count_on_task_failure = retry_count_on_task_failure
        self.timeout_in_minutes = timeout_in_minutes
        self.inputs = inputs
        self.env = env


class DefinitionsTask:
    type: Optional[BuildResourceType]
    properties: Optional[TaskProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[FirstProperty]]
    any_of: Optional[List[PurpleAnyOf]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[TaskProperties], additional_properties: Optional[bool], first_property: Optional[List[FirstProperty]], any_of: Optional[List[PurpleAnyOf]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.any_of = any_of


class TaskBaseProperties:
    condition: Optional[FetchDepth]
    continue_on_error: Optional[FluffyContinueOnError]
    display_name: Optional[PurpleDisplayName]
    target: Optional[Target]
    enabled: Optional[PurpleEnabled]
    env: Optional[PurpleEnv]
    name: Optional[Name]
    timeout_in_minutes: Optional[Connection]
    retry_count_on_task_failure: Optional[PurpleRetryCountOnTaskFailure]

    def __init__(self, condition: Optional[FetchDepth], continue_on_error: Optional[FluffyContinueOnError], display_name: Optional[PurpleDisplayName], target: Optional[Target], enabled: Optional[PurpleEnabled], env: Optional[PurpleEnv], name: Optional[Name], timeout_in_minutes: Optional[Connection], retry_count_on_task_failure: Optional[PurpleRetryCountOnTaskFailure]) -> None:
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.display_name = display_name
        self.target = target
        self.enabled = enabled
        self.env = env
        self.name = name
        self.timeout_in_minutes = timeout_in_minutes
        self.retry_count_on_task_failure = retry_count_on_task_failure


class TaskBase:
    type: Optional[BuildResourceType]
    properties: Optional[TaskBaseProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[TaskBaseProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class TemplateParameters:
    any_of: Optional[List[AnyAnyOf]]

    def __init__(self, any_of: Optional[List[AnyAnyOf]]) -> None:
        self.any_of = any_of


class Properties9:
    batch: Optional[MapDockerSocket]
    branches: Optional[BranchClass]
    paths: Optional[BranchClass]
    tags: Optional[BranchClass]

    def __init__(self, batch: Optional[MapDockerSocket], branches: Optional[BranchClass], paths: Optional[BranchClass], tags: Optional[BranchClass]) -> None:
        self.batch = batch
        self.branches = branches
        self.paths = paths
        self.tags = tags


class TriggerAnyOf:
    type: Optional[str]
    pattern: Optional[str]
    items: Optional[BranchClass]
    properties: Optional[Properties9]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[str], pattern: Optional[str], items: Optional[BranchClass], properties: Optional[Properties9], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.pattern = pattern
        self.items = items
        self.properties = properties
        self.additional_properties = additional_properties


class DefinitionsTrigger:
    any_of: Optional[List[TriggerAnyOf]]

    def __init__(self, any_of: Optional[List[TriggerAnyOf]]) -> None:
        self.any_of = any_of


class TriggerBranchFilterAnyOf:
    type: Optional[str]
    properties: Optional[IncludeExcludeFiltersProperties]
    additional_properties: Optional[bool]
    items: Optional[BranchClass]

    def __init__(self, type: Optional[str], properties: Optional[IncludeExcludeFiltersProperties], additional_properties: Optional[bool], items: Optional[BranchClass]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.items = items


class TriggerBranchFilter:
    any_of: Optional[List[TriggerBranchFilterAnyOf]]

    def __init__(self, any_of: Optional[List[TriggerBranchFilterAnyOf]]) -> None:
        self.any_of = any_of


class Properties10:
    name: Optional[TemplateClass]
    value: Optional[DisplayName]
    readonly: Optional[Always]
    group: Optional[TemplateClass]
    template: Optional[TemplateClass]
    parameters: Optional[BranchClass]

    def __init__(self, name: Optional[TemplateClass], value: Optional[DisplayName], readonly: Optional[Always], group: Optional[TemplateClass], template: Optional[TemplateClass], parameters: Optional[BranchClass]) -> None:
        self.name = name
        self.value = value
        self.readonly = readonly
        self.group = group
        self.template = template
        self.parameters = parameters


class VariableAnyOf:
    type: Optional[BuildResourceType]
    properties: Optional[Properties10]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[Properties10], additional_properties: Optional[bool], first_property: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property


class Variable:
    any_of: Optional[List[VariableAnyOf]]

    def __init__(self, any_of: Optional[List[VariableAnyOf]]) -> None:
        self.any_of = any_of


class VariableRestrictionsAnyOf:
    type: Optional[str]
    ignore_case: Optional[AnyOfIgnoreCase]
    pattern: Optional[str]
    items: Optional[TemplateClass]

    def __init__(self, type: Optional[str], ignore_case: Optional[AnyOfIgnoreCase], pattern: Optional[str], items: Optional[TemplateClass]) -> None:
        self.type = type
        self.ignore_case = ignore_case
        self.pattern = pattern
        self.items = items


class VariableRestrictions:
    any_of: Optional[List[VariableRestrictionsAnyOf]]

    def __init__(self, any_of: Optional[List[VariableRestrictionsAnyOf]]) -> None:
        self.any_of = any_of


class Variables:
    any_of: Optional[List[AnyAnyOf]]

    def __init__(self, any_of: Optional[List[AnyAnyOf]]) -> None:
        self.any_of = any_of


class VariablesTemplateProperties:
    parameters: Optional[BranchClass]
    variables: Optional[BranchClass]

    def __init__(self, parameters: Optional[BranchClass], variables: Optional[BranchClass]) -> None:
        self.parameters = parameters
        self.variables = variables


class VariablesTemplate:
    type: Optional[BuildResourceType]
    properties: Optional[VariablesTemplateProperties]
    additional_properties: Optional[bool]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[VariablesTemplateProperties], additional_properties: Optional[bool]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties


class WebhookFilterProperties:
    path: Optional[Connection]
    value: Optional[Connection]

    def __init__(self, path: Optional[Connection], value: Optional[Connection]) -> None:
        self.path = path
        self.value = value


class WebhookFilter:
    type: Optional[BuildResourceType]
    properties: Optional[WebhookFilterProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[WebhookFilterProperties], additional_properties: Optional[bool], first_property: Optional[List[str]], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.required = required


class WebhookResourceProperties:
    webhook: Optional[Build]
    connection: Optional[Connection]
    type: Optional[Connection]
    filters: Optional[DeployClass]

    def __init__(self, webhook: Optional[Build], connection: Optional[Connection], type: Optional[Connection], filters: Optional[DeployClass]) -> None:
        self.webhook = webhook
        self.connection = connection
        self.type = type
        self.filters = filters


class WebhookResource:
    type: Optional[BuildResourceType]
    properties: Optional[WebhookResourceProperties]
    additional_properties: Optional[bool]
    first_property: Optional[List[str]]
    required: Optional[List[str]]

    def __init__(self, type: Optional[BuildResourceType], properties: Optional[WebhookResourceProperties], additional_properties: Optional[bool], first_property: Optional[List[str]], required: Optional[List[str]]) -> None:
        self.type = type
        self.properties = properties
        self.additional_properties = additional_properties
        self.first_property = first_property
        self.required = required


class Definitions:
    string: Optional[JobContinueOnError]
    sequence: Optional[BranchFilterArray]
    mapping: Optional[JobServices]
    any: Optional[AnyClass]
    pipeline: Optional[Pipeline]
    pipeline_base: Optional[PipelineBase]
    pipeline_trigger: Optional[PipelineAnyBaseClass]
    pipeline_parameters: Optional[PipelineAnyBaseClass]
    pipeline_pr: Optional[PipelineAnyBaseClass]
    pipeline_schedules: Optional[PipelineAnyBaseClass]
    pipeline_any_base: Optional[PipelineAnyBaseClass]
    pr: Optional[PR]
    trigger: Optional[DefinitionsTrigger]
    include_exclude_filters: Optional[IncludeExcludeFilters]
    include_exclude_string_filters: Optional[IncludeExcludeStringFilters]
    branch_filter_array: Optional[BranchFilterArray]
    branch_filter: Optional[BranchFilter]
    template_parameters: Optional[TemplateParameters]
    template_parameter: Optional[TemplateParameter]
    template_parameter_type: Optional[BuildResourceTrigger]
    pipeline_template_parameters: Optional[BranchFilterArray]
    pipeline_template_parameter: Optional[TemplateParameter]
    pipeline_template_parameter_type: Optional[BuildResourceTrigger]
    schedules: Optional[BranchFilterArray]
    schedule: Optional[Schedule]
    resources: Optional[Resources]
    build_resources: Optional[BranchFilterArray]
    build_resource: Optional[BuildResource]
    build_resource_trigger: Optional[BuildResourceTrigger]
    package_resources: Optional[BranchFilterArray]
    package_resource: Optional[PackageResource]
    package_resource_trigger: Optional[BuildResourceTrigger]
    container_resources: Optional[BranchFilterArray]
    container_resource: Optional[ContainerResource]
    container_artifact_type: Optional[Boolean]
    container_resource_trigger: Optional[ContainerResourceTrigger]
    pipeline_resources: Optional[BranchFilterArray]
    pipeline_resource: Optional[PipelineResource]
    pipeline_resource_trigger: Optional[PipelineResourceTrigger]
    trigger_branch_filter: Optional[TriggerBranchFilter]
    repository_resources: Optional[BranchFilterArray]
    repository_resource: Optional[RepositoryResource]
    repository_checkout_options: Optional[RepositoryCheckoutOptions]
    legacy_resource: Optional[LegacyResource]
    legacy_repo_resource_alias: Optional[LegacyRepoResourceAlias]
    webhook_resources: Optional[BranchFilterArray]
    webhook_resource: Optional[WebhookResource]
    webhook_filters: Optional[BranchFilterArray]
    webhook_filter: Optional[WebhookFilter]
    variables_template: Optional[VariablesTemplate]
    variables: Optional[Variables]
    variable: Optional[Variable]
    stages_template: Optional[StagesTemplate]
    stages: Optional[BranchFilterArray]
    stage: Optional[Stage]
    lock_behavior: Optional[BuildResourceTrigger]
    stage_trigger: Optional[BuildResourceTrigger]
    extends_parameters: Optional[BranchFilterArray]
    extends_template: Optional[ExtendsTemplate]
    extends_template_base: Optional[ExtendsTemplateBase]
    parameters_template: Optional[ParametersTemplate]
    extends: Optional[Extends]
    jobs_template: Optional[JobsTemplate]
    jobs: Optional[BranchFilterArray]
    job: Optional[Job]
    explicit_resources: Optional[ExplicitResources]
    pool: Optional[Pool]
    pool_demands: Optional[PoolDemands]
    job_container: Optional[JobContainer]
    container_base: Optional[ContainerBase]
    read_only_mounts: Optional[ReadOnlyMounts]
    job_services: Optional[JobServices]
    job_workspace: Optional[JobWorkspace]
    job_strategy: Optional[JobStrategy]
    job_matrix: Optional[JobMatrix]
    matrix_properties: Optional[MatrixProperties]
    deployment_environment: Optional[DeploymentEnvironment]
    deployment_strategy: Optional[DeploymentStrategy]
    pre_deploy_hook: Optional[Hook]
    deploy_hook: Optional[Hook]
    route_traffic_hook: Optional[Hook]
    post_route_traffic_hook: Optional[Hook]
    on_success_or_failure_hook: Optional[OnSuccessOrFailureHook]
    on_failure_hook: Optional[Hook]
    on_success_hook: Optional[Hook]
    run_once_deployment_strategy: Optional[RunOnceDeploymentStrategy]
    rolling_deployment_strategy: Optional[RollingDeploymentStrategy]
    canary_deployment_strategy: Optional[CanaryDeploymentStrategy]
    canary_deployment_increments: Optional[CanaryDeploymentIncrements]
    phases: Optional[DefinitionsPhases]
    phase: Optional[Phase]
    phase_queue_target: Optional[PhaseQueueTarget]
    phase_server_target: Optional[PhaseServerTarget]
    phase_target_demands: Optional[PhaseTargetDemands]
    phase_target_workspace: Optional[PhaseTargetWorkspace]
    phase_target_matrix: Optional[PhaseTargetMatrix]
    steps_template: Optional[StepsTemplate]
    steps: Optional[BranchFilterArray]
    step: Optional[Step]
    step_target: Optional[StepTarget]
    variable_restrictions: Optional[VariableRestrictions]
    job_decorator_steps: Optional[JobDecoratorSteps]
    tasks: Optional[BranchFilterArray]
    task_base: Optional[TaskBase]
    job_continue_on_error: Optional[JobContinueOnError]
    job_depends_on: Optional[JobDependsOn]
    reference_name: Optional[LegacyRepoResourceAlias]
    template_context: Optional[JobServices]
    boolean: Optional[Boolean]
    string_allow_expressions: Optional[JobContinueOnError]
    non_empty_string: Optional[JobContinueOnError]
    sequence_of_non_empty_string: Optional[CanaryDeploymentIncrements]
    sequence_of_string_allow_expressions: Optional[BranchFilterArray]
    mapping_of_string_string: Optional[JobServices]
    any_allow_expressions: Optional[AnyAllowExpressions]
    task: Optional[DefinitionsTask]

    def __init__(self, string: Optional[JobContinueOnError], sequence: Optional[BranchFilterArray], mapping: Optional[JobServices], any: Optional[AnyClass], pipeline: Optional[Pipeline], pipeline_base: Optional[PipelineBase], pipeline_trigger: Optional[PipelineAnyBaseClass], pipeline_parameters: Optional[PipelineAnyBaseClass], pipeline_pr: Optional[PipelineAnyBaseClass], pipeline_schedules: Optional[PipelineAnyBaseClass], pipeline_any_base: Optional[PipelineAnyBaseClass], pr: Optional[PR], trigger: Optional[DefinitionsTrigger], include_exclude_filters: Optional[IncludeExcludeFilters], include_exclude_string_filters: Optional[IncludeExcludeStringFilters], branch_filter_array: Optional[BranchFilterArray], branch_filter: Optional[BranchFilter], template_parameters: Optional[TemplateParameters], template_parameter: Optional[TemplateParameter], template_parameter_type: Optional[BuildResourceTrigger], pipeline_template_parameters: Optional[BranchFilterArray], pipeline_template_parameter: Optional[TemplateParameter], pipeline_template_parameter_type: Optional[BuildResourceTrigger], schedules: Optional[BranchFilterArray], schedule: Optional[Schedule], resources: Optional[Resources], build_resources: Optional[BranchFilterArray], build_resource: Optional[BuildResource], build_resource_trigger: Optional[BuildResourceTrigger], package_resources: Optional[BranchFilterArray], package_resource: Optional[PackageResource], package_resource_trigger: Optional[BuildResourceTrigger], container_resources: Optional[BranchFilterArray], container_resource: Optional[ContainerResource], container_artifact_type: Optional[Boolean], container_resource_trigger: Optional[ContainerResourceTrigger], pipeline_resources: Optional[BranchFilterArray], pipeline_resource: Optional[PipelineResource], pipeline_resource_trigger: Optional[PipelineResourceTrigger], trigger_branch_filter: Optional[TriggerBranchFilter], repository_resources: Optional[BranchFilterArray], repository_resource: Optional[RepositoryResource], repository_checkout_options: Optional[RepositoryCheckoutOptions], legacy_resource: Optional[LegacyResource], legacy_repo_resource_alias: Optional[LegacyRepoResourceAlias], webhook_resources: Optional[BranchFilterArray], webhook_resource: Optional[WebhookResource], webhook_filters: Optional[BranchFilterArray], webhook_filter: Optional[WebhookFilter], variables_template: Optional[VariablesTemplate], variables: Optional[Variables], variable: Optional[Variable], stages_template: Optional[StagesTemplate], stages: Optional[BranchFilterArray], stage: Optional[Stage], lock_behavior: Optional[BuildResourceTrigger], stage_trigger: Optional[BuildResourceTrigger], extends_parameters: Optional[BranchFilterArray], extends_template: Optional[ExtendsTemplate], extends_template_base: Optional[ExtendsTemplateBase], parameters_template: Optional[ParametersTemplate], extends: Optional[Extends], jobs_template: Optional[JobsTemplate], jobs: Optional[BranchFilterArray], job: Optional[Job], explicit_resources: Optional[ExplicitResources], pool: Optional[Pool], pool_demands: Optional[PoolDemands], job_container: Optional[JobContainer], container_base: Optional[ContainerBase], read_only_mounts: Optional[ReadOnlyMounts], job_services: Optional[JobServices], job_workspace: Optional[JobWorkspace], job_strategy: Optional[JobStrategy], job_matrix: Optional[JobMatrix], matrix_properties: Optional[MatrixProperties], deployment_environment: Optional[DeploymentEnvironment], deployment_strategy: Optional[DeploymentStrategy], pre_deploy_hook: Optional[Hook], deploy_hook: Optional[Hook], route_traffic_hook: Optional[Hook], post_route_traffic_hook: Optional[Hook], on_success_or_failure_hook: Optional[OnSuccessOrFailureHook], on_failure_hook: Optional[Hook], on_success_hook: Optional[Hook], run_once_deployment_strategy: Optional[RunOnceDeploymentStrategy], rolling_deployment_strategy: Optional[RollingDeploymentStrategy], canary_deployment_strategy: Optional[CanaryDeploymentStrategy], canary_deployment_increments: Optional[CanaryDeploymentIncrements], phases: Optional[DefinitionsPhases], phase: Optional[Phase], phase_queue_target: Optional[PhaseQueueTarget], phase_server_target: Optional[PhaseServerTarget], phase_target_demands: Optional[PhaseTargetDemands], phase_target_workspace: Optional[PhaseTargetWorkspace], phase_target_matrix: Optional[PhaseTargetMatrix], steps_template: Optional[StepsTemplate], steps: Optional[BranchFilterArray], step: Optional[Step], step_target: Optional[StepTarget], variable_restrictions: Optional[VariableRestrictions], job_decorator_steps: Optional[JobDecoratorSteps], tasks: Optional[BranchFilterArray], task_base: Optional[TaskBase], job_continue_on_error: Optional[JobContinueOnError], job_depends_on: Optional[JobDependsOn], reference_name: Optional[LegacyRepoResourceAlias], template_context: Optional[JobServices], boolean: Optional[Boolean], string_allow_expressions: Optional[JobContinueOnError], non_empty_string: Optional[JobContinueOnError], sequence_of_non_empty_string: Optional[CanaryDeploymentIncrements], sequence_of_string_allow_expressions: Optional[BranchFilterArray], mapping_of_string_string: Optional[JobServices], any_allow_expressions: Optional[AnyAllowExpressions], task: Optional[DefinitionsTask]) -> None:
        self.string = string
        self.sequence = sequence
        self.mapping = mapping
        self.any = any
        self.pipeline = pipeline
        self.pipeline_base = pipeline_base
        self.pipeline_trigger = pipeline_trigger
        self.pipeline_parameters = pipeline_parameters
        self.pipeline_pr = pipeline_pr
        self.pipeline_schedules = pipeline_schedules
        self.pipeline_any_base = pipeline_any_base
        self.pr = pr
        self.trigger = trigger
        self.include_exclude_filters = include_exclude_filters
        self.include_exclude_string_filters = include_exclude_string_filters
        self.branch_filter_array = branch_filter_array
        self.branch_filter = branch_filter
        self.template_parameters = template_parameters
        self.template_parameter = template_parameter
        self.template_parameter_type = template_parameter_type
        self.pipeline_template_parameters = pipeline_template_parameters
        self.pipeline_template_parameter = pipeline_template_parameter
        self.pipeline_template_parameter_type = pipeline_template_parameter_type
        self.schedules = schedules
        self.schedule = schedule
        self.resources = resources
        self.build_resources = build_resources
        self.build_resource = build_resource
        self.build_resource_trigger = build_resource_trigger
        self.package_resources = package_resources
        self.package_resource = package_resource
        self.package_resource_trigger = package_resource_trigger
        self.container_resources = container_resources
        self.container_resource = container_resource
        self.container_artifact_type = container_artifact_type
        self.container_resource_trigger = container_resource_trigger
        self.pipeline_resources = pipeline_resources
        self.pipeline_resource = pipeline_resource
        self.pipeline_resource_trigger = pipeline_resource_trigger
        self.trigger_branch_filter = trigger_branch_filter
        self.repository_resources = repository_resources
        self.repository_resource = repository_resource
        self.repository_checkout_options = repository_checkout_options
        self.legacy_resource = legacy_resource
        self.legacy_repo_resource_alias = legacy_repo_resource_alias
        self.webhook_resources = webhook_resources
        self.webhook_resource = webhook_resource
        self.webhook_filters = webhook_filters
        self.webhook_filter = webhook_filter
        self.variables_template = variables_template
        self.variables = variables
        self.variable = variable
        self.stages_template = stages_template
        self.stages = stages
        self.stage = stage
        self.lock_behavior = lock_behavior
        self.stage_trigger = stage_trigger
        self.extends_parameters = extends_parameters
        self.extends_template = extends_template
        self.extends_template_base = extends_template_base
        self.parameters_template = parameters_template
        self.extends = extends
        self.jobs_template = jobs_template
        self.jobs = jobs
        self.job = job
        self.explicit_resources = explicit_resources
        self.pool = pool
        self.pool_demands = pool_demands
        self.job_container = job_container
        self.container_base = container_base
        self.read_only_mounts = read_only_mounts
        self.job_services = job_services
        self.job_workspace = job_workspace
        self.job_strategy = job_strategy
        self.job_matrix = job_matrix
        self.matrix_properties = matrix_properties
        self.deployment_environment = deployment_environment
        self.deployment_strategy = deployment_strategy
        self.pre_deploy_hook = pre_deploy_hook
        self.deploy_hook = deploy_hook
        self.route_traffic_hook = route_traffic_hook
        self.post_route_traffic_hook = post_route_traffic_hook
        self.on_success_or_failure_hook = on_success_or_failure_hook
        self.on_failure_hook = on_failure_hook
        self.on_success_hook = on_success_hook
        self.run_once_deployment_strategy = run_once_deployment_strategy
        self.rolling_deployment_strategy = rolling_deployment_strategy
        self.canary_deployment_strategy = canary_deployment_strategy
        self.canary_deployment_increments = canary_deployment_increments
        self.phases = phases
        self.phase = phase
        self.phase_queue_target = phase_queue_target
        self.phase_server_target = phase_server_target
        self.phase_target_demands = phase_target_demands
        self.phase_target_workspace = phase_target_workspace
        self.phase_target_matrix = phase_target_matrix
        self.steps_template = steps_template
        self.steps = steps
        self.step = step
        self.step_target = step_target
        self.variable_restrictions = variable_restrictions
        self.job_decorator_steps = job_decorator_steps
        self.tasks = tasks
        self.task_base = task_base
        self.job_continue_on_error = job_continue_on_error
        self.job_depends_on = job_depends_on
        self.reference_name = reference_name
        self.template_context = template_context
        self.boolean = boolean
        self.string_allow_expressions = string_allow_expressions
        self.non_empty_string = non_empty_string
        self.sequence_of_non_empty_string = sequence_of_non_empty_string
        self.sequence_of_string_allow_expressions = sequence_of_string_allow_expressions
        self.mapping_of_string_string = mapping_of_string_string
        self.any_allow_expressions = any_allow_expressions
        self.task = task


class OneOf:
    ref: Optional[str]
    type: Optional[BranchFilterType]
    pattern: Optional[str]

    def __init__(self, ref: Optional[str], type: Optional[BranchFilterType], pattern: Optional[str]) -> None:
        self.ref = ref
        self.type = type
        self.pattern = pattern


class GeneratedModels:
    schema: Optional[str]
    id: Optional[str]
    comment: Optional[str]
    title: Optional[str]
    description: Optional[str]
    one_of: Optional[List[OneOf]]
    definitions: Optional[Definitions]

    def __init__(self, schema: Optional[str], id: Optional[str], comment: Optional[str], title: Optional[str], description: Optional[str], one_of: Optional[List[OneOf]], definitions: Optional[Definitions]) -> None:
        self.schema = schema
        self.id = id
        self.comment = comment
        self.title = title
        self.description = description
        self.one_of = one_of
        self.definitions = definitions