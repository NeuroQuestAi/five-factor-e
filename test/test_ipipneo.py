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

        with self.assertRaises(BaseException):
            IpipNeo(question="")

        with self.assertRaises(BaseException):
            IpipNeo(question="OCEAN")

        with self.assertRaises(BaseException):
            IpipNeo(question=0)

        self.assertEqual(IpipNeo(question=120).__class__.__name__, "IpipNeo")
        self.assertEqual(IpipNeo(question=300).__class__.__name__, "IpipNeo")

    def test_compute(self) -> None:
        big5 = IpipNeo(question=120)

        with self.assertRaises(TypeError):
            big5.compute(sex="")

        with self.assertRaises(TypeError):
            big5.compute("")

        #############################################
        # 1. Test with 40 year old man.
        #############################################
        result = big5.compute(sex="M", age=40, answers=load_mock_answers())

        self.assertTrue(len(result.get("id")))
        self.assertTrue(len(result.get("theory")))
        self.assertTrue(len(result.get("model")))

        self.assertEqual(result.get("question"), 120)
        self.assertEqual(result.get("person").get("sex"), "M")
        self.assertEqual(result.get("person").get("age"), 40)

        self.assertTrue(len(result.get("person").get("result")))
        self.assertTrue(len(result.get("person").get("result").get("personalities")))

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(len(personalities), 5)

        self.assertEqual(personalities[0]["Openness"].get("O"), 26.882298529738506)
        self.assertEqual(
            personalities[1]["Conscientiousness"].get("C"), 86.96687032595662
        )
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 21.46713047820697)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 57.52658875205816)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 37.23631660596993)

        #############################################
        # 1. Test with 30 year old woman.
        #############################################
        result = big5.compute(sex="F", age=30, answers=load_mock_answers())

        self.assertTrue(len(result.get("id")))
        self.assertTrue(len(result.get("theory")))
        self.assertTrue(len(result.get("model")))

        self.assertEqual(result.get("question"), 120)
        self.assertEqual(result.get("person").get("sex"), "F")
        self.assertEqual(result.get("person").get("age"), 30)

        self.assertTrue(len(result.get("person").get("result")))
        self.assertTrue(len(result.get("person").get("result").get("personalities")))

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(len(personalities), 5)

        self.assertEqual(personalities[0]["Openness"].get("O"), 21.601284007758267)
        self.assertEqual(
            personalities[1]["Conscientiousness"].get("C"), 83.97834295105292
        )
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 16.85540168264683)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 34.87513390061565)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 26.35310712596734)
