"""Unit tests for IpipNeo."""

import json
import unittest

from ipipneo.ipipneo import IpipNeo


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

        self.assertEqual(personalities[0]["Openness"].get("O"), 13.262383714475419)
        self.assertEqual(
            personalities[1]["Conscientiousness"].get("C"), 18.62283542366208
        )
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 34.10779114957646)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 1.9889215690788262)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 58.6632925696303)

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

        self.assertEqual(personalities[0]["Openness"].get("O"), 8.876064362586419)
        self.assertEqual(
            personalities[1]["Conscientiousness"].get("C"), 13.877369975064141
        )
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 29.240137885780882)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 1)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 47.49034742252866)
