#!/usr/bin/env python3

import sys
import typing
from arcaflow_plugin_sdk import plugin
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
import ansible_runner

from .metadata_schema import (
    InputParams,
    SuccessOutput,
    ErrorOutput,
    selected_facts_schema,
)


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
            private_data_dir="/tmp",
            host_pattern=ansible_host,
            module="gather_facts",
            quiet=True,
        )
        host_ansible_facts = r.get_fact_cache(ansible_host)

        for fact, value in host_ansible_facts.items():
            new_fact = fact[len("ansible_"):]
            if new_fact in selected_facts_schema.properties:
                selected_facts.update({new_fact: value})

        # Convert to dict
        output = convert_to_supported_type(selected_facts)

        return "success", SuccessOutput(selected_facts_schema.unserialize(output))
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
