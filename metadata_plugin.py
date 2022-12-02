#!/usr/bin/env python3

import sys
import typing
from dataclasses import dataclass, field
from arcaflow_plugin_sdk import plugin
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
import ansible_runner


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

    #Distribution info comes from the container and isn't valuable
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


@plugin.step(
    id="collect-metadata",
    name="Collect Metadata",
    description="Collects ansible facts metadata",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def collect_metadata(
    params: InputParams,
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:

    ansible_host = "localhost"
    selected_facts = {}

    try:
        r = ansible_runner.run(
            private_data_dir="/tmp", host_pattern=ansible_host, module="gather_facts"
        )
        host_ansible_facts = r.get_fact_cache(ansible_host)
        
        for fact, value in host_ansible_facts.items():
            new_fact = fact[len("ansible_"):]
            if new_fact in selected_facts_schema.properties:
                selected_facts.update({new_fact: value})

        # Convert to dict
        output = convert_to_supported_type(selected_facts)

        return "success", SuccessOutput(
            selected_facts_schema.unserialize(output)
        )
    except KeyError:
        return "error", ErrorOutput("missing a key in ansible facts")


def convert_to_supported_type(ansible_value) -> typing.Dict:
    type_of_val = type(ansible_value)
    if type_of_val == list:
        new_list = []
        for i in ansible_value:
            new_list.append(convert_to_supported_type(i))
        # A list needs to be of a consistent type or it will
        # not be indexible into a system like Elasticsearch
        return convert_to_homogenous_list(new_list)
    elif type_of_val == dict:
        result = {}
        for k in ansible_value:
            result[convert_to_supported_type(k)] = convert_to_supported_type(
                ansible_value[k]
            )
        return result
    elif type_of_val in (float, int, str, bool):
        return ansible_value
    elif isinstance(type_of_val, type(None)):
        return str("")
    elif type_of_val == AnsibleUnsafeText:
        return str(ansible_value)
    else:
        print("Unknown type", type_of_val, "with val", str(ansible_value))
        return str(ansible_value)


def convert_to_homogenous_list(input_list: list):
    # To make all types in list homogeneous, we upconvert them
    # to the least commom type.
    # int -> float -> str
    # bool + None -> str
    list_type = str()
    for j in input_list:
        if type(j) in (str, bool, type(None)):
            list_type = str()
            break
        elif type(j) == float:
            list_type = float()
        elif type(j) == int and type(list_type) != float:
            list_type = int()
    return list(map(type(list_type), input_list))


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                # List your step functions here:
                collect_metadata,
            )
        )
    )
