"""Unit tests for Facet."""

import unittest

from big5.facet import Facet


class TestFacet(unittest.TestCase):
    def test_invalid_params(self) -> None:
        with self.assertRaises(TypeError):
            facet = Facet()

        with self.assertRaises(BaseException):
            facet = Facet(nquestion="")

        with self.assertRaises(BaseException):
            facet = Facet(nquestion=0)

        self.assertEqual(Facet(nquestion=120).__class__.__name__, "Facet")
        self.assertEqual(Facet(nquestion=300).__class__.__name__, "Facet")

    def test_score(self) -> None:
        facet = Facet(nquestion=120)

        with self.assertRaises(AttributeError):
            facet.score(answers="")

        with self.assertRaises(TypeError):
            facet.score(answers=["A", "B"])

        with self.assertRaises(BaseException) as e:
            facet.score(answers=[0, 1])
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list index out of range",
        )

        answers = [
            5,
            2,
            3,
            2,
            5,
            4,
            1,
            3,
            5,
            5,
            3,
            2,
            2,
            4,
            5,
            2,
            5,
            4,
            2,
            5,
            2,
            4,
            5,
            2,
            4,
            1,
            2,
            5,
            4,
            4,
            2,
            3,
            4,
            5,
            5,
            4,
            2,
            2,
            5,
            5,
            2,
            2,
            4,
            3,
            4,
            4,
            4,
            4,
            5,
            4,
            2,
            4,
            3,
            3,
            4,
            5,
            2,
            4,
            1,
            3,
            1,
            3,
            1,
            4,
            4,
            2,
            2,
            3,
            5,
            5,
            2,
            4,
            4,
            4,
            3,
            1,
            2,
            4,
            5,
            5,
            3,
            2,
            2,
            2,
            5,
            1,
            4,
            4,
            2,
            1,
            4,
            2,
            2,
            4,
            3,
            2,
            1,
            3,
            5,
            5,
            1,
            4,
            2,
            2,
            4,
            4,
            3,
            4,
            4,
            5,
            3,
            2,
            4,
            5,
            5,
            1,
            4,
            2,
            4,
            4,
        ]

        score = facet.score(answers=answers)
        assert isinstance(score, list), "score must be a list"
        self.assertEqual(len(score), 121)
