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


def load_mock_answers_300_1() -> dict:
    with open("test/mock/answers-test-7.json") as f:
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

        # 1. O
        self.assertEqual(personalities[0]["openness"].get("O"), 13.262383714475419)
        self.assertEqual(personalities[0]["openness"].get("score"), "low")

        # 1.1. O. Traits
        self.assertEqual(
            personalities[0]["openness"]["traits"][0].get("imagination"), 1
        )
        self.assertEqual(personalities[0]["openness"]["traits"][0].get("score"), "low")

        self.assertEqual(
            personalities[0]["openness"]["traits"][1].get("artistic_interests"),
            14.832308817371768,
        )
        self.assertEqual(personalities[0]["openness"]["traits"][1].get("score"), "low")

        self.assertEqual(
            personalities[0]["openness"]["traits"][2].get("emotionality"),
            22.458638690321635,
        )
        self.assertEqual(personalities[0]["openness"]["traits"][2].get("score"), "low")

        self.assertEqual(
            personalities[0]["openness"]["traits"][3].get("adventurousness"),
            19.18624143043911,
        )
        self.assertEqual(personalities[0]["openness"]["traits"][3].get("score"), "low")

        self.assertEqual(
            personalities[0]["openness"]["traits"][4].get("intellect"), 27.6351617847169
        )
        self.assertEqual(personalities[0]["openness"]["traits"][4].get("score"), "low")

        self.assertEqual(
            personalities[0]["openness"]["traits"][5].get("liberalism"),
            79.99472618213304,
        )
        ##self.assertEqual(personalities[0]["openness"]["traits"][5].get("score"), "high")

        # 2. C
        self.assertEqual(
            personalities[1]["conscientiousness"].get("C"), 18.62283542366208
        )
        self.assertEqual(personalities[1]["conscientiousness"].get("score"), "low")

        # 2.1. C. Traits
        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][0].get("self_efficacy"),
            67.18081968991703,
        )
        # self.assertEqual(
        #    personalities[1]["conscientiousness"]["traits"][0].get("score"), "average"
        # )

        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][1].get("orderliness"),
            18.490917605991513,
        )
        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][1].get("score"), "low"
        )

        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][2].get("dutifulness"),
            28.94752897386354,
        )
        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][2].get("score"), "low"
        )

        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][3].get(
                "achievement_striving"
            ),
            9.985264466537785,
        )
        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][3].get("score"), "low"
        )

        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][4].get("self_discipline"),
            17.450496278627668,
        )
        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][4].get("score"), "low"
        )

        self.assertEqual(
            personalities[1]["conscientiousness"]["traits"][5].get("cautiousness"),
            38.524355262005315,
        )
        # self.assertEqual(
        #    personalities[1]["conscientiousness"]["traits"][5].get("score"), "average"
        # )

        # 3. E
        self.assertEqual(personalities[2]["extraversion"].get("E"), 34.10779114957646)
        self.assertEqual(personalities[2]["extraversion"].get("score"), "low")

        # 3.1. E. Traits
        self.assertEqual(
            personalities[2]["extraversion"]["traits"][0].get("friendliness"),
            37.84207122476397,
        )
        # self.assertEqual(
        #    personalities[2]["extraversion"]["traits"][0].get("score"), "average"
        # )

        self.assertEqual(
            personalities[2]["extraversion"]["traits"][1].get("gregariousness"),
            55.874636258650355,
        )
        # self.assertEqual(
        #    personalities[2]["extraversion"]["traits"][1].get("score"), "average"
        # )

        self.assertEqual(
            personalities[2]["extraversion"]["traits"][2].get("assertiveness"),
            10.136565617726376,
        )
        self.assertEqual(
            personalities[2]["extraversion"]["traits"][2].get("score"), "low"
        )

        self.assertEqual(
            personalities[2]["extraversion"]["traits"][3].get("activity_level"),
            70.68785093930268,
        )
        # self.assertEqual(
        #    personalities[2]["extraversion"]["traits"][3].get("score"), "high"
        # )

        self.assertEqual(
            personalities[2]["extraversion"]["traits"][4].get("excitement_seeking"),
            36.25782829248527,
        )
        # self.assertEqual(
        #    personalities[2]["extraversion"]["traits"][4].get("score"), "average"
        # )

        self.assertEqual(
            personalities[2]["extraversion"]["traits"][5].get("cheerfulness"),
            27.560328329400278,
        )
        self.assertEqual(
            personalities[2]["extraversion"]["traits"][5].get("score"), "low"
        )

        # 4. A
        self.assertEqual(personalities[3]["agreeableness"].get("A"), 1.9889215690788262)
        self.assertEqual(personalities[3]["agreeableness"].get("score"), "low")

        # 4.1. A. Traits
        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][0].get("trust"),
            51.83212101876228,
        )
        # self.assertEqual(
        #    personalities[3]["agreeableness"]["traits"][0].get("score"), "average"
        # )

        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][1].get("morality"), 1
        )
        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][1].get("score"), "low"
        )

        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][2].get("altruism"),
            22.561476501041227,
        )
        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][2].get("score"), "low"
        )

        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][3].get("cooperation"),
            1.930347015846948,
        )
        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][3].get("score"), "low"
        )

        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][4].get("modesty"),
            55.67124528467815,
        )
        # self.assertEqual(
        #    personalities[3]["agreeableness"]["traits"][4].get("score"), "average"
        # )

        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][5].get("sympathy"),
            21.651269458084244,
        )
        self.assertEqual(
            personalities[3]["agreeableness"]["traits"][5].get("score"), "low"
        )

        # 5. N
        self.assertEqual(personalities[4]["neuroticism"].get("N"), 58.6632925696303)
        self.assertEqual(personalities[4]["neuroticism"].get("score"), "high")

        # 5.1. N Traits
        self.assertEqual(
            personalities[4]["neuroticism"]["traits"][0].get("anxiety"),
            55.29153291804727,
        )
        # self.assertEqual(
        #    personalities[4]["neuroticism"]["traits"][0].get("score"), "average"
        # )

        self.assertEqual(
            personalities[4]["neuroticism"]["traits"][1].get("anger"), 68.23438372956855
        )
        # self.assertEqual(
        #    personalities[4]["neuroticism"]["traits"][1].get("score"), "high"
        # )

        self.assertEqual(
            personalities[4]["neuroticism"]["traits"][2].get("depression"),
            63.91248592040063,
        )
        # self.assertEqual(
        #    personalities[4]["neuroticism"]["traits"][2].get("score"), "average"
        # )

        self.assertEqual(
            personalities[4]["neuroticism"]["traits"][3].get("self_consciousness"),
            22.421630518162374,
        )
        self.assertEqual(
            personalities[4]["neuroticism"]["traits"][3].get("score"), "low"
        )

        self.assertEqual(
            personalities[4]["neuroticism"]["traits"][4].get("immoderation"),
            48.1804752623172,
        )
        # self.assertEqual(
        #    personalities[4]["neuroticism"]["traits"][4].get("score"), "average"
        # )

        self.assertEqual(
            personalities[4]["neuroticism"]["traits"][5].get("vulnerability"),
            77.83259998736844,
        )
        # self.assertEqual(
        #    personalities[4]["neuroticism"]["traits"][5].get("score"), "high"
        # )

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

        self.assertEqual(personalities[0]["openness"].get("O"), 8.876064362586419)
        self.assertEqual(
            personalities[1]["conscientiousness"].get("C"), 13.877369975064141
        )
        self.assertEqual(personalities[2]["extraversion"].get("E"), 29.240137885780882)
        self.assertEqual(personalities[3]["agreeableness"].get("A"), 1)
        self.assertEqual(personalities[4]["neuroticism"].get("N"), 47.49034742252866)

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

        self.assertEqual(personalities[0]["openness"].get("O"), 24.29091080263288)
        self.assertEqual(personalities[1]["conscientiousness"].get("C"), 1)
        self.assertEqual(personalities[2]["extraversion"].get("E"), 32.92660962191414)
        self.assertEqual(personalities[3]["agreeableness"].get("A"), 1)
        self.assertEqual(personalities[4]["neuroticism"].get("N"), 67.59105722337824)

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

        self.assertEqual(personalities[0]["openness"].get("O"), 38.846625568407774)
        self.assertEqual(
            personalities[1]["conscientiousness"].get("C"), 4.6266733183044835
        )
        self.assertEqual(personalities[2]["extraversion"].get("E"), 58.00148636052478)
        self.assertEqual(personalities[3]["agreeableness"].get("A"), 11.934721812005705)
        self.assertEqual(personalities[4]["neuroticism"].get("N"), 78.82240987792443)

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

        self.assertEqual(personalities[0]["openness"].get("O"), 28.963387129747275)
        self.assertEqual(personalities[1]["conscientiousness"].get("C"), 1)
        self.assertEqual(personalities[2]["extraversion"].get("E"), 54.26151488253112)
        self.assertEqual(personalities[3]["agreeableness"].get("A"), 1)
        self.assertEqual(personalities[4]["neuroticism"].get("N"), 71.14096931653722)

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

        self.assertEqual(personalities[0]["openness"].get("O"), 28.963387129747275)
        self.assertEqual(personalities[1]["conscientiousness"].get("C"), 1)
        self.assertEqual(personalities[2]["extraversion"].get("E"), 54.26151488253112)
        self.assertEqual(personalities[3]["agreeableness"].get("A"), 1)
        self.assertEqual(personalities[4]["neuroticism"].get("N"), 71.14096931653722)

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

    def test_compute_test_custom_120_reversed(self) -> None:
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

        self.assertEqual(personalities[0]["openness"].get("O"), 17.42235805055492)
        self.assertEqual(
            personalities[1]["conscientiousness"].get("C"), 18.62283542366208
        )
        self.assertEqual(personalities[2]["extraversion"].get("E"), 34.10779114957646)
        self.assertEqual(personalities[3]["agreeableness"].get("A"), 6.331832993524202)
        self.assertEqual(personalities[4]["neuroticism"].get("N"), 58.6632925696303)

    def test_facet_scale_level(self) -> None:
        ipip = IpipNeo(question=120)

        low, high = ipip.get_current_scale_level()
        self.assertEqual(low, 45)
        self.assertEqual(high, 55)

        ipip.set_new_facet_level(low_min=40, high_max=90)
        low, high = ipip.get_current_scale_level()
        self.assertEqual(low, 40)
        self.assertEqual(high, 90)

        with self.assertRaises(BaseException) as e:
            IpipNeo(question=120).set_new_facet_level(low_min="40", high_max=None)
        self.assertEqual(
            str(e.exception),
            "The (low_min) field must be an int!",
        )

        with self.assertRaises(BaseException) as e:
            IpipNeo(question=300).set_new_facet_level(low_min=40, high_max="89")
        self.assertEqual(
            str(e.exception),
            "The (high_max) field must be an int!",
        )

        ipip.set_new_facet_level(low_min=10, high_max=70)
        low, high = ipip.get_current_scale_level()
        self.assertEqual(low, 10)
        self.assertEqual(high, 70)

        ipip = IpipNeo(question=120)

        low, high = ipip.get_current_scale_level()
        self.assertEqual(low, 45)
        self.assertEqual(high, 55)

        ipip = IpipNeo(question=300)

        low, high = ipip.get_current_scale_level()
        self.assertEqual(low, 45)
        self.assertEqual(high, 55)

    def test_new_norm_scale(self) -> None:
        with self.assertRaises(BaseException) as e:
            IpipNeo(question=120).set_new_norm_scale(scale_min="-", scale_max=75)
        self.assertEqual(
            str(e.exception),
            "The (scale_min) field must be an int!",
        )

        with self.assertRaises(BaseException) as e:
            IpipNeo(question=120).set_new_norm_scale(scale_min=1, scale_max=None)
        self.assertEqual(
            str(e.exception),
            "The (scale_max) field must be an int!",
        )

        ipip = IpipNeo(question=120)

        scale_min, scale_max = ipip.get_current_norm()
        self.assertEqual(scale_min, 32)
        self.assertEqual(scale_max, 73)

        ipip.set_new_norm_scale(scale_min=27, scale_max=73)
        scale_min, scale_max = ipip.get_current_norm()
        self.assertEqual(scale_min, 27)
        self.assertEqual(scale_max, 73)

        ipip.set_new_norm_scale(scale_min=15, scale_max=60)
        scale_min, scale_max = ipip.get_current_norm()
        self.assertEqual(scale_min, 15)
        self.assertEqual(scale_max, 60)

        ipip = IpipNeo(question=300)

        scale_min, scale_max = ipip.get_current_norm()
        self.assertEqual(scale_min, 32)
        self.assertEqual(scale_max, 73)

        ipip = IpipNeo(question=300)

        result = ipip.compute(
            sex="M", age=40, answers=load_mock_answers_300_1(), compare=False
        )

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(personalities[0]["openness"].get("O"), 20.534815840469236)
        self.assertEqual(
            personalities[0]["openness"]["traits"][0].get("imagination"),
            1,
        )

        ipip.set_new_norm_scale(scale_min=25, scale_max=75)
        scale_min, scale_max = ipip.get_current_norm()
        self.assertEqual(scale_min, 25)
        self.assertEqual(scale_max, 75)

        result = ipip.compute(
            sex="M", age=40, answers=load_mock_answers_300_1(), compare=False
        )

        personalities = result.get("person").get("result").get("personalities")
        self.assertEqual(personalities[0]["openness"].get("O"), 20.534815840469236)
        self.assertEqual(
            personalities[0]["openness"]["traits"][0].get("imagination"),
            0.35632569430614325,
        )

    def test_compute_test_custom_300_reversed(self) -> None:
        def d(compare_original: list, compare_reverse: list):
            differences = []
            for original, reversed in zip(compare_original, compare_reverse):
                if original["id_select"] != reversed["id_select"]:
                    differences.append(
                        {
                            "id_question": original["id_question"],
                            "id_select_original": original["id_select"],
                            "id_select_reversed": reversed["id_select"],
                        }
                    )
            return differences or []

        #############################################
        # 1. Test with 40 year old man.
        #############################################
        result = IpipNeo(question=300).compute(
            sex="M", age=40, answers=load_mock_answers_300(), compare=True
        )

        compare_original = result["person"]["result"]["compare"][
            "user_answers_original"
        ]
        compare_reverse = result["person"]["result"]["compare"]["user_answers_reversed"]

        self.assertEqual(
            len(d(compare_original=compare_original, compare_reverse=compare_reverse)),
            121,
        )

        #############################################
        # 2. Test with 40 year old man.
        #############################################
        result = IpipNeo(question=300).compute(
            sex="M", age=40, answers=load_mock_answers_300_1(), compare=True
        )

        compare_original = result["person"]["result"]["compare"][
            "user_answers_original"
        ]
        compare_reverse = result["person"]["result"]["compare"]["user_answers_reversed"]

        self.assertEqual(
            len(d(compare_original=compare_original, compare_reverse=compare_reverse)),
            144,
        )

        #############################################
        # 3. Test with 20 year old man.
        #############################################
        result = IpipNeo(question=300).compute(
            sex="M", age=20, answers=load_mock_answers_300_1(), compare=True
        )

        compare_original = result["person"]["result"]["compare"][
            "user_answers_original"
        ]
        compare_reverse = result["person"]["result"]["compare"]["user_answers_reversed"]

        self.assertEqual(
            len(d(compare_original=compare_original, compare_reverse=compare_reverse)),
            144,
        )

        #############################################
        # 4. Test with 18 year old woman.
        #############################################
        result = IpipNeo(question=300).compute(
            sex="F", age=18, answers=load_mock_answers_300_1(), compare=True
        )

        compare_original = result["person"]["result"]["compare"][
            "user_answers_original"
        ]
        compare_reverse = result["person"]["result"]["compare"]["user_answers_reversed"]

        self.assertEqual(
            len(d(compare_original=compare_original, compare_reverse=compare_reverse)),
            144,
        )

        #############################################
        # 5. Test with 29 year old woman.
        #############################################
        result = IpipNeo(question=300).compute(
            sex="F", age=29, answers=load_mock_answers_300(), compare=True
        )

        compare_original = result["person"]["result"]["compare"][
            "user_answers_original"
        ]
        compare_reverse = result["person"]["result"]["compare"]["user_answers_reversed"]

        self.assertEqual(
            len(d(compare_original=compare_original, compare_reverse=compare_reverse)),
            121,
        )

        #############################################
        # 6. Test with 40 year old man.
        #############################################
        ipip = IpipNeo(question=300)
        result = ipip.compute(
            sex="M", age=40, answers=load_mock_answers_300_1(), compare=True
        )

        compare_original = result["person"]["result"]["compare"][
            "user_answers_original"
        ]
        compare_reverse = result["person"]["result"]["compare"]["user_answers_reversed"]

        self.assertEqual(
            len(d(compare_original=compare_original, compare_reverse=compare_reverse)),
            144,
        )
