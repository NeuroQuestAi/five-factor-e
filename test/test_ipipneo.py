"""Unit tests for IpipNeo."""

import json
import unittest

from ipipneo.ipipneo import IpipNeo


def load_mock_answers_120() -> dict:
    with open("test/mock/answers-test-1.json") as f:
        data = json.load(f)
    return data


def load_mock_answers_300() -> dict:
    with open("test/mock/answers-test-4.json") as f:
        data = json.load(f)
    return data


def load_mock_answers_custom() -> dict:
    with open(f"test/mock/answers-test-6.json") as f:
        data = json.load(f)
    return data


class TestIpipNeo(unittest.TestCase):

    maxDiff = None

    def test_invalid_params(self) -> None:
        with self.assertRaises(BaseException):
            IpipNeo(question="")

        with self.assertRaises(BaseException):
            IpipNeo(question="OCEAN")

        with self.assertRaises(BaseException):
            IpipNeo(question=0)

        self.assertEqual(IpipNeo(question=120).__class__.__name__, "IpipNeo")
        self.assertEqual(IpipNeo(question=300).__class__.__name__, "IpipNeo")
        self.assertEqual(IpipNeo(question=120, test=True).__class__.__name__, "IpipNeo")
        self.assertEqual(IpipNeo(question=300, test=True).__class__.__name__, "IpipNeo")

    def test_compute_120(self) -> None:
        big5 = IpipNeo(question=120)

        with self.assertRaises(TypeError):
            big5.compute(sex="")

        with self.assertRaises(TypeError):
            big5.compute("")

        big5 = None

        #############################################
        # 1. Test with 40 year old man.
        #############################################
        result = IpipNeo(question=120).compute(
            sex="M", age=40, answers=load_mock_answers_120()
        )

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
        # 2. Test with 30 year old woman.
        #############################################
        result = IpipNeo(question=120).compute(
            sex="F", age=30, answers=load_mock_answers_120()
        )

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

        #############################################
        # 3. Test with 65 year old woman.
        #############################################
        result = IpipNeo(question=120).compute(
            sex="F", age=65, answers=load_mock_answers_120(), compare=True
        )

        self.assertIn("id", result)
        self.assertIn("theory", result)
        self.assertIn("model", result)
        self.assertIn("question", result)
        self.assertIn("person", result)

        self.assertIn("sex", result.get("person"))
        self.assertIn("age", result.get("person"))

        self.assertTrue(len(result.get("id")))
        self.assertTrue(len(result.get("theory")))
        self.assertTrue(len(result.get("model")))

        self.assertEqual(result.get("question"), 120)
        self.assertEqual(result.get("person").get("sex"), "F")
        self.assertEqual(result.get("person").get("age"), 65)

        self.assertTrue(len(result.get("person").get("result")))
        self.assertTrue(len(result.get("person").get("result").get("personalities")))
        self.assertTrue(len(result.get("person").get("result").get("compare")))

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(len(personalities), 5)

        compare = result.get("person").get("result").get("compare")
        self.assertIn("user_answers_original", compare)
        self.assertIn("user_answers_reversed", compare)

        self.assertEqual(personalities[0]["Openness"].get("O"), 24.29091080263288)
        self.assertEqual(personalities[1]["Conscientiousness"].get("C"), 1)
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 32.92660962191414)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 1)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 67.59105722337824)

        original = (
            result.get("person")
            .get("result")
            .get("compare")
            .get("user_answers_original")
        )
        assert isinstance(original, list), "original must be a list"
        self.assertEqual(len(original), 120)

        reversed = (
            result.get("person")
            .get("result")
            .get("compare")
            .get("user_answers_reversed")
        )
        assert isinstance(reversed, list), "reversed must be a list"
        self.assertEqual(len(reversed), 120)

        a = [x.get("id_select") for x in original]
        assert isinstance(original, list), "reversed must be a list"

        b = [x.get("id_select") for x in reversed]
        assert isinstance(reversed, list), "reversed must be a list"

        self.assertNotEqual(a, b)

        self.assertEqual(a[0], b[0])
        self.assertEqual(a[1], b[1])
        self.assertEqual(a[2], b[2])
        self.assertEqual(a[3], b[3])
        self.assertEqual(a[4], b[4])
        self.assertEqual(a[5], b[5])
        self.assertEqual(a[6], b[6])
        self.assertEqual(a[7], b[7])

        self.assertNotEqual(a[8], b[8])
        self.assertEqual(a[8], 5)
        self.assertEqual(b[8], 1)

        self.assertNotEqual(a[18], b[18])
        self.assertEqual(a[18], 2)
        self.assertEqual(b[18], 4)

        self.assertNotEqual(a[23], b[23])
        self.assertEqual(a[23], 2)
        self.assertEqual(b[23], 4)

        self.assertNotEqual(a[29], b[29])
        self.assertEqual(a[29], 4)
        self.assertEqual(b[29], 2)

        self.assertNotEqual(a[38], b[38])
        self.assertEqual(a[38], 5)
        self.assertEqual(b[38], 1)

        self.assertNotEqual(a[39], b[39])
        self.assertEqual(a[39], 5)
        self.assertEqual(b[39], 1)

        self.assertNotEqual(a[47], b[47])
        self.assertEqual(a[47], 4)
        self.assertEqual(b[47], 2)

        self.assertNotEqual(a[48], b[48])
        self.assertEqual(a[48], 5)
        self.assertEqual(b[48], 1)

        self.assertNotEqual(a[50], b[50])
        self.assertEqual(a[50], 2)
        self.assertEqual(b[50], 4)

        self.assertNotEqual(a[66], b[66])
        self.assertEqual(a[66], 2)
        self.assertEqual(b[66], 4)

    def test_compute_300(self) -> None:
        #############################################
        # 1. Test with 40 year old man.
        #############################################
        result = IpipNeo(question=300).compute(
            sex="M", age=40, answers=load_mock_answers_300()
        )

        self.assertTrue(len(result.get("id")))
        self.assertTrue(len(result.get("theory")))
        self.assertTrue(len(result.get("model")))

        self.assertEqual(result.get("question"), 300)
        self.assertEqual(result.get("person").get("sex"), "M")
        self.assertEqual(result.get("person").get("age"), 40)

        self.assertTrue(len(result.get("person").get("result")))
        self.assertTrue(len(result.get("person").get("result").get("personalities")))

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(len(personalities), 5)

        self.assertEqual(personalities[0]["Openness"].get("O"), 38.846625568407774)
        self.assertEqual(
            personalities[1]["Conscientiousness"].get("C"), 4.6266733183044835
        )
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 58.00148636052478)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 11.934721812005705)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 78.82240987792443)

        #############################################
        # 2. Test with 30 year old woman.
        #############################################
        result = IpipNeo(question=300).compute(
            sex="F", age=30, answers=load_mock_answers_300()
        )

        self.assertTrue(len(result.get("id")))
        self.assertTrue(len(result.get("theory")))
        self.assertTrue(len(result.get("model")))

        self.assertEqual(result.get("question"), 300)
        self.assertEqual(result.get("person").get("sex"), "F")
        self.assertEqual(result.get("person").get("age"), 30)

        self.assertTrue(len(result.get("person").get("result")))
        self.assertTrue(len(result.get("person").get("result").get("personalities")))

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(len(personalities), 5)

        self.assertEqual(personalities[0]["Openness"].get("O"), 28.963387129747275)
        self.assertEqual(personalities[1]["Conscientiousness"].get("C"), 1)
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 54.26151488253112)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 1)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 71.14096931653722)

        #############################################
        # 3. Test with 65 year old woman.
        #############################################
        result = IpipNeo(question=300).compute(
            sex="F", age=65, answers=load_mock_answers_300(), compare=True
        )

        self.assertIn("id", result)
        self.assertIn("theory", result)
        self.assertIn("model", result)
        self.assertIn("question", result)
        self.assertIn("person", result)

        self.assertIn("sex", result.get("person"))
        self.assertIn("age", result.get("person"))

        self.assertTrue(len(result.get("id")))
        self.assertTrue(len(result.get("theory")))
        self.assertTrue(len(result.get("model")))

        self.assertEqual(result.get("question"), 300)
        self.assertEqual(result.get("person").get("sex"), "F")
        self.assertEqual(result.get("person").get("age"), 65)

        self.assertTrue(len(result.get("person").get("result")))
        self.assertTrue(len(result.get("person").get("result").get("personalities")))
        self.assertTrue(len(result.get("person").get("result").get("compare")))

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(len(personalities), 5)

        compare = result.get("person").get("result").get("compare")
        self.assertIn("user_answers_original", compare)
        self.assertIn("user_answers_reversed", compare)

        self.assertEqual(personalities[0]["Openness"].get("O"), 28.963387129747275)
        self.assertEqual(personalities[1]["Conscientiousness"].get("C"), 1)
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 54.26151488253112)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 1)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 71.14096931653722)

        original = (
            result.get("person")
            .get("result")
            .get("compare")
            .get("user_answers_original")
        )
        assert isinstance(original, list), "original must be a list"
        self.assertEqual(len(original), 300)

        reversed = (
            result.get("person")
            .get("result")
            .get("compare")
            .get("user_answers_reversed")
        )
        assert isinstance(reversed, list), "reversed must be a list"
        self.assertEqual(len(reversed), 300)

        a = [x.get("id_select") for x in original]
        assert isinstance(original, list), "reversed must be a list"

        b = [x.get("id_select") for x in reversed]
        assert isinstance(reversed, list), "reversed must be a list"

        self.assertNotEqual(a, b)

    def test_compute_test_custom_reversed(self) -> None:
        #############################################
        # 1. Test with 40 year old man.
        #############################################
        result = IpipNeo(question=120, test=True).compute(
            sex="M", age=40, answers=load_mock_answers_custom(), compare=True
        )

        self.assertIn("id", result)
        self.assertIn("theory", result)
        self.assertIn("model", result)
        self.assertIn("version", result)
        self.assertIn("test", result)
        self.assertIn("question", result)
        self.assertIn("person", result)

        self.assertIn("sex", result.get("person"))
        self.assertIn("age", result.get("person"))

        self.assertTrue(len(result.get("id")))
        self.assertTrue(len(result.get("theory")))
        self.assertTrue(len(result.get("model")))

        self.assertEqual(result.get("question"), 120)
        self.assertEqual(result.get("test"), True)
        self.assertEqual(result.get("person").get("sex"), "M")
        self.assertEqual(result.get("person").get("age"), 40)

        self.assertTrue(len(result.get("person").get("result")))
        self.assertTrue(len(result.get("person").get("result").get("personalities")))
        self.assertTrue(len(result.get("person").get("result").get("compare")))

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(len(personalities), 5)

        compare = result.get("person").get("result").get("compare")
        self.assertIn("user_answers_original", compare)
        self.assertIn("user_answers_reversed", compare)

        select1 = [
            x.get("reverse_scored") for x in compare.get("user_answers_original", [])
        ]
        assert isinstance(select1, list), "select1 must be a list"

        self.assertEqual(select1.count(0), 67)
        self.assertEqual(select1.count(1), 53)

        select2 = [
            x.get("reverse_scored") for x in compare.get("user_answers_reversed", [])
        ]
        assert isinstance(select2, list), "select2 must be a list"

        self.assertEqual(select2.count(0), select1.count(0))
        self.assertEqual(select2.count(1), select1.count(1))

        self.assertEqual(personalities[0]["Openness"].get("O"), 17.42235805055492)
        self.assertEqual(
            personalities[1]["Conscientiousness"].get("C"), 18.62283542366208
        )
        self.assertEqual(personalities[2]["Extraversion"].get("E"), 34.10779114957646)
        self.assertEqual(personalities[3]["Agreeableness"].get("A"), 6.331832993524202)
        self.assertEqual(personalities[4]["Neuroticism"].get("N"), 58.6632925696303)
