#!/usr/bin/env python3
import unittest
import metadata_plugin
from arcaflow_plugin_sdk import plugin


class HelloWorldTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            metadata_plugin.InputParams()
        )

        plugin.test_object_serialization(
            metadata_plugin.SuccessOutput(
                metadata= {
                    "env": {
                        "SHELL": "/bin/bash",
                    },
                    "system": "linux",
                    "processor_count": 1,
                    "system_capabilities": []
                }
            )
        )

        plugin.test_object_serialization(
            metadata_plugin.ErrorOutput(
                error="This is an error"
            )
        )

    def test_functional(self):
        input = metadata_plugin.InputParams()

        output_id, output_data = metadata_plugin.collect_metadata(input)

        self.assertEqual("success", output_id)
        self.assertIsInstance(output_data.metadata, dict)
        self.assertGreaterEqual(
            len(output_data.metadata),
            1
        )
        # Some expected keys in the dict
        self.assertTrue("env" in output_data.metadata)
        self.assertTrue("distribution" in output_data.metadata)


if __name__ == '__main__':
    unittest.main()
