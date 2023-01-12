#!/usr/bin/env python3

import typing
from dataclasses import dataclass, field
from arcaflow_plugin_sdk import plugin


@dataclass
class InputParams:
    """
    This is the data structure for the input parameters of the step defined
    below.
    """


@dataclass
class SelectedFacts:
    """
    These are the selected facts from ansible gather_facts that we return.
    The 'ansible_' prefix is stripped here from the fact names.
    """

    architecture: str = field(
        metadata={
            "name": "ansible architecture",
            "description": "The system architecture",
        }
    )

    # Distribution info comes from the container and isn't valuable
    # distribution: str = field(
    #     metadata={
    #         "name": "ansible distribution",
    #         "description": "The system OS distribution",
    #     }
    # )

    # distribution_major_version: str = field(
    #     metadata={
    #         "name": "ansible distribution major version",
    #         "description": "The system OS distribution major version",
    #     }
    # )

    # distribution_version: str = field(
    #     metadata={
    #         "name": "ansible distribution version",
    #         "description": "The system OS distribution verion",
    #     }
    # )

    # distribution_release: str = field(
    #     metadata={
    #         "name": "ansible distribution release",
    #         "description": "The system OS distribution release",
    #     }
    # )

    fqdn: str = field(
        metadata={
            "name": "ansible fqdn",
            "description": "The system fully-qualified domain name",
        }
    )

    kernel: str = field(
        metadata={
            "name": "ansible kernel",
            "description": "The system OS kernel",
        }
    )

    machine_id: str = field(
        metadata={
            "name": "ansible machine ID",
            "description": "The system machine ID",
        }
    )

    memtotal_mb: int = field(
        metadata={
            "name": "ansible memtotal MB",
            "description": "The system total memory in MB",
        }
    )

    swaptotal_mb: int = field(
        metadata={
            "name": "ansible swaptotal mb",
            "description": "The system swap size in MB",
        }
    )

    processor_cores: int = field(
        metadata={
            "name": "ansible processor cores",
            "description": "The system total processor cores",
        }
    )

    processor_count: int = field(
        metadata={
            "name": "ansible processor count",
            "description": "The system total processor count",
        }
    )

    processor_threads_per_core: int = field(
        metadata={
            "name": "ansible processor threads per core",
            "description": "The system threads per processor core",
        }
    )

    product_name: str = field(
        metadata={
            "name": "ansible product name",
            "description": "The system product name",
        }
    )

    product_version: str = field(
        metadata={
            "name": "ansible product version",
            "description": "The system product version",
        }
    )

    system_vendor: str = field(
        metadata={
            "name": "ansible system vendor",
            "description": "The system vendor",
        }
    )

    product_name: str = field(
        metadata={
            "name": "ansible product name",
            "description": "The system product name",
        }
    )

    processor: typing.List[str] = field(
        metadata={
            "name": "ansible processor",
            "description": "The system processor list",
        }
    )

    env: typing.Dict[str, str] = field(
        metadata={
            "name": "ansible env",
            "description": "The system environment variables",
        }
    )

    uptime_seconds: int = field(
        metadata={
            "name": "ansible uptime seconds",
            "description": "The system uptime in seconds",
        }
    )


selected_facts_schema = plugin.build_object_schema(SelectedFacts)


@dataclass
class SuccessOutput:
    """
    This is the output data structure for the success case.
    """

    metadata: SelectedFacts


@dataclass
class ErrorOutput:
    """
    This is the output data structure in the error  case.
    """

    error: str
