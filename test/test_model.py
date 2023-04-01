"""Unit tests for Model."""

import unittest

from ipipneo.model import (Big5Agreeableness, Big5Conscientiousness,
                           Big5Extraversion, Big5Neuroticism, Big5Openness,
                           FacetLevel, FacetScale, NormCubic, NormScale,
                           QuestionNumber)


class TestModel(unittest.TestCase):
    def test_question_number(self) -> None:
        model = QuestionNumber

        self.assertEqual(model.IPIP_120, 120)
        self.assertEqual(model.IPIP_120.value, 120)

        self.assertEqual(model.IPIP_300, 300)
        self.assertEqual(model.IPIP_300.value, 300)

        x1 = list(map(int, model))
        self.assertEqual(len(x1), 2)

    def test_facet_scale(self) -> None:
        model = FacetScale

        self.assertEqual(model.IPIP_MAX, 30)
        self.assertEqual(model.IPIP_MAX.value, 30)

        self.assertEqual(model.IPIP_300, 10)
        self.assertEqual(model.IPIP_300.value, 10)

        self.assertEqual(model.IPIP_120, 4)
        self.assertEqual(model.IPIP_120.value, 4)

        x1 = list(map(int, model))
        self.assertEqual(len(x1), 3)

    def test_facet_level(self) -> None:
        model = FacetLevel

        self.assertEqual(model.HIGH, 55)
        self.assertEqual(model.HIGH.value, 55)

        self.assertEqual(model.LOW, 45)
        self.assertEqual(model.LOW.value, 45)

        x1 = list(map(int, model))
        self.assertEqual(len(x1), 2)

    def test_norm_scale(self) -> None:
        model = NormScale

        self.assertEqual(model.CONST_MAX, 73)
        self.assertEqual(model.CONST_MAX.value, 73)

        self.assertEqual(model.CONST_MIN, 32)
        self.assertEqual(model.CONST_MIN.value, 32)

        x1 = list(map(int, model))
        self.assertEqual(len(x1), 2)

    def test_norm_cubic(self) -> None:
        model = NormCubic

        self.assertEqual(model.CONST1, 210.335958661391)
        self.assertEqual(model.CONST1.value, 210.335958661391)

        self.assertEqual(model.CONST2, 16.7379362643389)
        self.assertEqual(model.CONST2.value, 16.7379362643389)

        self.assertEqual(model.CONST3, 0.405936512733332)
        self.assertEqual(model.CONST3.value, 0.405936512733332)

        self.assertEqual(model.CONST4, 0.00270624341822222)
        self.assertEqual(model.CONST4.value, 0.00270624341822222)

        x1 = list(map(int, model))
        self.assertEqual(len(x1), 4)

    def test_big5_neuroticism(self) -> None:
        model = Big5Neuroticism

        self.assertEqual(model.TRAIT1, "anxiety")
        self.assertEqual(model.TRAIT1.value, "anxiety")

        self.assertEqual(model.TRAIT2, "anger")
        self.assertEqual(model.TRAIT2.value, "anger")

        self.assertEqual(model.TRAIT3, "depression")
        self.assertEqual(model.TRAIT3.value, "depression")

        self.assertEqual(model.TRAIT4, "self_consciousness")
        self.assertEqual(model.TRAIT4.value, "self_consciousness")

        self.assertEqual(model.TRAIT5, "immoderation")
        self.assertEqual(model.TRAIT5.value, "immoderation")

        self.assertEqual(model.TRAIT6, "vulnerability")
        self.assertEqual(model.TRAIT6.value, "vulnerability")

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)

    def test_big5_extraversion(self) -> None:
        model = Big5Extraversion

        self.assertEqual(model.TRAIT1, "friendliness")
        self.assertEqual(model.TRAIT1.value, "friendliness")

        self.assertEqual(model.TRAIT2, "gregariousness")
        self.assertEqual(model.TRAIT2.value, "gregariousness")

        self.assertEqual(model.TRAIT3, "assertiveness")
        self.assertEqual(model.TRAIT3.value, "assertiveness")

        self.assertEqual(model.TRAIT4, "activity_level")
        self.assertEqual(model.TRAIT4.value, "activity_level")

        self.assertEqual(model.TRAIT5, "excitement_seeking")
        self.assertEqual(model.TRAIT5.value, "excitement_seeking")

        self.assertEqual(model.TRAIT6, "cheerfulness")
        self.assertEqual(model.TRAIT6.value, "cheerfulness")

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)

    def test_big5_openness(self) -> None:
        model = Big5Openness

        self.assertEqual(model.TRAIT1, "imagination")
        self.assertEqual(model.TRAIT1.value, "imagination")

        self.assertEqual(model.TRAIT2, "artistic_interests")
        self.assertEqual(model.TRAIT2.value, "artistic_interests")

        self.assertEqual(model.TRAIT3, "emotionality")
        self.assertEqual(model.TRAIT3.value, "emotionality")

        self.assertEqual(model.TRAIT4, "adventurousness")
        self.assertEqual(model.TRAIT4.value, "adventurousness")

        self.assertEqual(model.TRAIT5, "intellect")
        self.assertEqual(model.TRAIT5.value, "intellect")

        self.assertEqual(model.TRAIT6, "liberalism")
        self.assertEqual(model.TRAIT6.value, "liberalism")

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)

    def test_big5_agreeableness(self) -> None:
        model = Big5Agreeableness

        self.assertEqual(model.TRAIT1, "trust")
        self.assertEqual(model.TRAIT1.value, "trust")

        self.assertEqual(model.TRAIT2, "morality")
        self.assertEqual(model.TRAIT2.value, "morality")

        self.assertEqual(model.TRAIT3, "altruism")
        self.assertEqual(model.TRAIT3.value, "altruism")

        self.assertEqual(model.TRAIT4, "cooperation")
        self.assertEqual(model.TRAIT4.value, "cooperation")

        self.assertEqual(model.TRAIT5, "modesty")
        self.assertEqual(model.TRAIT5.value, "modesty")

        self.assertEqual(model.TRAIT6, "sympathy")
        self.assertEqual(model.TRAIT6.value, "sympathy")

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)

    def test_big5_conscientiousness(self) -> None:
        model = Big5Conscientiousness

        self.assertEqual(model.TRAIT1, "self_efficacy")
        self.assertEqual(model.TRAIT1.value, "self_efficacy")

        self.assertEqual(model.TRAIT2, "orderliness")
        self.assertEqual(model.TRAIT2.value, "orderliness")

        self.assertEqual(model.TRAIT3, "dutifulness")
        self.assertEqual(model.TRAIT3.value, "dutifulness")

        self.assertEqual(model.TRAIT4, "achievement_striving")
        self.assertEqual(model.TRAIT4.value, "achievement_striving")

        self.assertEqual(model.TRAIT5, "self_discipline")
        self.assertEqual(model.TRAIT5.value, "self_discipline")

        self.assertEqual(model.TRAIT6, "cautiousness")
        self.assertEqual(model.TRAIT6.value, "cautiousness")

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)
