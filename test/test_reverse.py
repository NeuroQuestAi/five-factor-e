"""Unit tests for Utility."""

import json
import unittest

from ipipneo.reverse import (ReverseScored120, ReverseScored300,
                             ReverseScoredCustom, IPIP_NEO_ITEMS_REVERSED_120, IPIP_NEO_ITEMS_REVERSED_300)


def load_mock_answers_120() -> dict:
    with open(f"test/mock/answers-test-3.json") as f:
        data = json.load(f)
    return data


def load_mock_answers_300() -> dict:
    with open(f"test/mock/answers-test-4.json") as f:
        data = json.load(f)
    return data


def load_mock_answers_custom() -> dict:
    with open(f"test/mock/answers-test-6.json") as f:
        data = json.load(f)
    return data


class TestReverse(unittest.TestCase):
    def test_reverse_scored_120(self) -> None:
        self.assertEqual(len(IPIP_NEO_ITEMS_REVERSED_120), 55)

        with self.assertRaises(TypeError):
            ReverseScored120()

        with self.assertRaises(AssertionError) as e:
            ReverseScored120(answers=[])
        self.assertEqual(str(e.exception), "The (answers) field must be a dict!")

        with self.assertRaises(BaseException) as e:
            ReverseScored120(answers={})
        self.assertEqual(str(e.exception), "The key named (answers) was not found!")

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
        self.assertEqual(len(IPIP_NEO_ITEMS_REVERSED_300), 148)

        with self.assertRaises(TypeError):
            ReverseScored300()

        with self.assertRaises(AssertionError) as e:
            ReverseScored300(answers=[])
        self.assertEqual(str(e.exception), "The (answers) field must be a dict!")

        with self.assertRaises(BaseException) as e:
            ReverseScored300(answers={})
        self.assertEqual(str(e.exception), "The key named (answers) was not found!")

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

    def test_reverse_scored_custom(self) -> None:
        with self.assertRaises(TypeError):
            ReverseScoredCustom()

        with self.assertRaises(AssertionError) as e:
            ReverseScoredCustom(answers=[])
        self.assertEqual(str(e.exception), "The (answers) field must be a dict!")

        with self.assertRaises(BaseException) as e:
            ReverseScoredCustom(answers={})
        self.assertEqual(str(e.exception), "The key named (answers) was not found!")

        with self.assertRaises(BaseException) as e:
            ReverseScoredCustom(answers={"answers": [{"id_select": 1}]})
        self.assertEqual(str(e.exception), "The key named (id_question) was not found!")

        with self.assertRaises(BaseException) as e:
            ReverseScoredCustom(answers={"answers": [{"id_question": 1}]})
        self.assertEqual(str(e.exception), "The key named (id_select) was not found!")

        with self.assertRaises(BaseException) as e:
            ReverseScoredCustom(
                answers={"answers": [{"id_question": 1, "id_select": 1}]}
            )
        self.assertEqual(
            str(e.exception), "The key named (reverse_scored) was not found!"
        )

        a = load_mock_answers_custom()
        assert isinstance(a, dict), "a must be a dict"

        b = ReverseScoredCustom(answers=load_mock_answers_custom())
        assert isinstance(b, dict), "b must be a dict"
        assert isinstance(b.get("answers", []), list), "b must be a list"

        self.assertEqual(
            a.get("answers")[8].get("id_question"),
            b.get("answers")[8].get("id_question"),
        )
        self.assertEqual(
            a.get("answers")[8].get("reverse_scored"),
            b.get("answers")[8].get("reverse_scored"),
        )
        self.assertEqual(a.get("answers")[8].get("id_select"), 5)
        self.assertEqual(b.get("answers")[8].get("id_select"), 1)
        self.assertNotEqual(
            a.get("answers")[8].get("id_select"), b.get("answers")[8].get("id_select")
        )

        self.assertEqual(
            a.get("answers")[48].get("id_question"),
            b.get("answers")[48].get("id_question"),
        )
        self.assertEqual(
            a.get("answers")[48].get("reverse_scored"),
            b.get("answers")[48].get("reverse_scored"),
        )
        self.assertEqual(a.get("answers")[48].get("id_select"), 5)
        self.assertEqual(b.get("answers")[48].get("id_select"), 1)
        self.assertNotEqual(
            a.get("answers")[48].get("id_select"), b.get("answers")[48].get("id_select")
        )

        self.assertEqual(
            a.get("answers")[119].get("id_question"),
            b.get("answers")[119].get("id_question"),
        )
        self.assertEqual(
            a.get("answers")[119].get("reverse_scored"),
            b.get("answers")[119].get("reverse_scored"),
        )
        self.assertEqual(a.get("answers")[119].get("id_select"), 4)
        self.assertEqual(b.get("answers")[119].get("id_select"), 2)
        self.assertNotEqual(
            a.get("answers")[119].get("id_select"),
            b.get("answers")[119].get("id_select"),
        )

        self.assertNotEqual(a, b)
