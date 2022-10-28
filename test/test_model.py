"""Unit tests for Model."""

import unittest

from big5.model import (
    QuestionNumber,
    FacetScale,
    FacetLevel,
    NormScale,
    NormCubic,
    Big5Neuroticism,
    Big5Extraversion,
    Big5Openness,
    Big5Agreeableness,
    Big5Conscientiousness,
)


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

        self.assertEqual(model.TRAIT1, 'Anxiety')
        self.assertEqual(model.TRAIT1.value, 'Anxiety')

        self.assertEqual(model.TRAIT2, 'Anger')
        self.assertEqual(model.TRAIT2.value, 'Anger')

        self.assertEqual(model.TRAIT3, 'Depression')
        self.assertEqual(model.TRAIT3.value, 'Depression')

        self.assertEqual(model.TRAIT4, 'Self-Consciousness')
        self.assertEqual(model.TRAIT4.value, 'Self-Consciousness')

        self.assertEqual(model.TRAIT5, 'Immoderation')
        self.assertEqual(model.TRAIT5.value, 'Immoderation')

        self.assertEqual(model.TRAIT6, 'Vulnerability')
        self.assertEqual(model.TRAIT6.value, 'Vulnerability')

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)

    def test_big5_extraversion(self) -> None:
        model = Big5Extraversion

        self.assertEqual(model.TRAIT1, 'Friendliness')
        self.assertEqual(model.TRAIT1.value, 'Friendliness')

        self.assertEqual(model.TRAIT2, 'Gregariousness')
        self.assertEqual(model.TRAIT2.value, 'Gregariousness')

        self.assertEqual(model.TRAIT3, 'Assertiveness')
        self.assertEqual(model.TRAIT3.value, 'Assertiveness')

        self.assertEqual(model.TRAIT4, 'Activity-Level')
        self.assertEqual(model.TRAIT4.value, 'Activity-Level')

        self.assertEqual(model.TRAIT5, 'Excitement-Seeking')
        self.assertEqual(model.TRAIT5.value, 'Excitement-Seeking')

        self.assertEqual(model.TRAIT6, 'Cheerfulness')
        self.assertEqual(model.TRAIT6.value, 'Cheerfulness')

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)

    def test_big5_openness(self) -> None:
        model = Big5Openness

        self.assertEqual(model.TRAIT1, 'Imagination')
        self.assertEqual(model.TRAIT1.value, 'Imagination')

        self.assertEqual(model.TRAIT2, 'Artistic-Interests')
        self.assertEqual(model.TRAIT2.value, 'Artistic-Interests')

        self.assertEqual(model.TRAIT3, 'Emotionality')
        self.assertEqual(model.TRAIT3.value, 'Emotionality')

        self.assertEqual(model.TRAIT4, 'Adventurousness')
        self.assertEqual(model.TRAIT4.value, 'Adventurousness')

        self.assertEqual(model.TRAIT5, 'Intellect')
        self.assertEqual(model.TRAIT5.value, 'Intellect')

        self.assertEqual(model.TRAIT6, 'Liberalism')
        self.assertEqual(model.TRAIT6.value, 'Liberalism')

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)

    def test_big5_agreeableness(self) -> None:
        model = Big5Agreeableness

        self.assertEqual(model.TRAIT1, 'Trust')
        self.assertEqual(model.TRAIT1.value, 'Trust')

        self.assertEqual(model.TRAIT2, 'Morality')
        self.assertEqual(model.TRAIT2.value, 'Morality')

        self.assertEqual(model.TRAIT3, 'Altruism')
        self.assertEqual(model.TRAIT3.value, 'Altruism')

        self.assertEqual(model.TRAIT4, 'Cooperation')
        self.assertEqual(model.TRAIT4.value, 'Cooperation')

        self.assertEqual(model.TRAIT5, 'Modesty')
        self.assertEqual(model.TRAIT5.value, 'Modesty')

        self.assertEqual(model.TRAIT6, 'Sympathy')
        self.assertEqual(model.TRAIT6.value, 'Sympathy')

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)

    def test_big5_conscientiousness(self) -> None:
        model = Big5Conscientiousness

        self.assertEqual(model.TRAIT1, 'Self-Efficacy')
        self.assertEqual(model.TRAIT1.value, 'Self-Efficacy')

        self.assertEqual(model.TRAIT2, 'Orderliness')
        self.assertEqual(model.TRAIT2.value, 'Orderliness')

        self.assertEqual(model.TRAIT3, 'Dutifulness')
        self.assertEqual(model.TRAIT3.value, 'Dutifulness')

        self.assertEqual(model.TRAIT4, 'Achievement-Striving')
        self.assertEqual(model.TRAIT4.value, 'Achievement-Striving')

        self.assertEqual(model.TRAIT5, 'Self-Discipline')
        self.assertEqual(model.TRAIT5.value, 'Self-Discipline')

        self.assertEqual(model.TRAIT6, 'Cautiousness')
        self.assertEqual(model.TRAIT6.value, 'Cautiousness')

        x1 = list(map(str, model))
        self.assertEqual(len(x1), 6)
