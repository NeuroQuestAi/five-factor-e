"""Unit tests for IpipNeo."""

import json
import unittest

from big5.ipipneo import IpipNeo


def load_mock_answers() -> dict:
    with open("test/mock/answers-test-1.json") as f:
        data = json.load(f)
    return data


class TestIpipNeo(unittest.TestCase):
    def test_invalid_params(self) -> None:

        """
        with self.assertRaises(TypeError):
            facet = Facet()
        """

        big5 = IpipNeo(question=120)

        result = big5.compute(sex="M", age=40, answers=load_mock_answers())

        # # print(res)
        print(json.dumps(result, indent=4, sort_keys=False))
