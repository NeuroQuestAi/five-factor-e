"""Unit tests for Utility."""

import json
import unittest

from ipipneo.reverse import ReverseScored120, ReverseScored300


def load_mock_answers_120() -> dict:
    with open(f"test/mock/answers-test-3.json") as f:
        data = json.load(f)
    return data


def load_mock_answers_300() -> dict:
    with open(f"test/mock/answers-test-4.json") as f:
        data = json.load(f)
    return data


class TestReverse(unittest.TestCase):
    def test_reverse_scored_120(self) -> None:
        with self.assertRaises(TypeError):
            ReverseScored120()

        with self.assertRaises(AssertionError) as e:
            ReverseScored120(answers=[])
        self.assertEqual(str(e.exception), "The (answers) field must be a dict!")

        with self.assertRaises(BaseException) as e:
            ReverseScored120(answers={"answers": [{"id_select": 1}]})
        self.assertEqual(str(e.exception), "The key named (id_question) was not found!")

        with self.assertRaises(BaseException) as e:
            ReverseScored120(answers={"answers": [{"id_question": 1}]})
        self.assertEqual(str(e.exception), "The key named (id_select) was not found!")

        a = load_mock_answers_120()
        assert isinstance(a, dict), "a must be a dict"

        b = ReverseScored120(answers=load_mock_answers_120())
        assert isinstance(b, dict), "b must be a dict"
        assert isinstance(b.get("answers", []), list), "b must be a list"

        self.assertNotEqual(a, b)

    def test_reverse_scored_300(self) -> None:
        with self.assertRaises(TypeError):
            ReverseScored300()

        with self.assertRaises(AssertionError) as e:
            ReverseScored300(answers=[])
        self.assertEqual(str(e.exception), "The (answers) field must be a dict!")

        with self.assertRaises(BaseException) as e:
            ReverseScored300(answers={"answers": [{"id_select": 1}]})
        self.assertEqual(str(e.exception), "The key named (id_question) was not found!")

        with self.assertRaises(BaseException) as e:
            ReverseScored300(answers={"answers": [{"id_question": 1}]})
        self.assertEqual(str(e.exception), "The key named (id_select) was not found!")

        a = load_mock_answers_300()
        assert isinstance(a, dict), "a must be a dict"

        b = ReverseScored300(answers=load_mock_answers_300())
        assert isinstance(b, dict), "b must be a dict"
        assert isinstance(b.get("answers", []), list), "b must be a list"

        self.assertNotEqual(a, b)
