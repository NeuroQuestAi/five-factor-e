"""Unit tests for Facet."""

import json
import unittest

from big5.facet import Facet
from big5.norm import Norm
from big5.utility import organize_list_json


def load_mock_answers() -> dict:
    with open("test/mock/answers-test-1.json") as f:
        data = json.load(f)
    return data


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

        score = facet.score(answers=organize_list_json(load_mock_answers()))
        assert isinstance(score, list), "score must be a list"
        self.assertEqual(len(score), 121)

    def test_b5create(self) -> None:
        facet = Facet(nquestion=120)

        with self.assertRaises(BaseException) as e:
            facet.b5create(score=[0, 0, 0])
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list index out of range",
        )

        b5 = facet.b5create(
            score=facet.score(answers=organize_list_json(load_mock_answers()))
        )
        assert isinstance(b5, dict), "b5 must be a dict"

        self.assertEqual(len(b5.get("O")), 121)
        self.assertEqual(len(b5.get("C")), 121)
        self.assertEqual(len(b5.get("E")), 121)
        self.assertEqual(len(b5.get("A")), 121)
        self.assertEqual(len(b5.get("N")), 121)

        self.assertEqual(b5.get("O")[0], 0)
        self.assertEqual(b5.get("C")[0], 0)
        self.assertEqual(b5.get("E")[0], 0)
        self.assertEqual(b5.get("A")[0], 0)
        self.assertEqual(b5.get("N")[0], 0)

    def test_domain(self) -> None:
        facet = Facet(nquestion=120)

        with self.assertRaises(BaseException) as e:
            facet.domain(score=[-1, -1, -1])
        self.assertEqual(
            str(e.exception),
            "Invalid position in the score array: list index out of range",
        )

        domain = facet.domain(
            score=facet.score(answers=organize_list_json(load_mock_answers()))
        )
        assert isinstance(domain, dict), "domain must be a dict"

        self.assertEqual(domain.get("O"), 78)
        self.assertEqual(domain.get("C"), 102)
        self.assertEqual(domain.get("E"), 66)
        self.assertEqual(domain.get("A"), 87)
        self.assertEqual(domain.get("N"), 61)

    def test_distrib(self) -> None:
        facet = Facet(nquestion=120)

        with self.assertRaises(TypeError):
            facet.distrib(size=0, b5={}, norm={})

        b5 = facet.b5create(
            score=facet.score(answers=organize_list_json(load_mock_answers()))
        )
        assert isinstance(b5, dict), "b5 must be a dict"

        domain = facet.domain(
            score=facet.score(answers=organize_list_json(load_mock_answers()))
        )
        assert isinstance(domain, dict), "domain must be a dict"

        with self.assertRaises(BaseException) as e:
            facet.distrib(size=0, b5=b5, norm=Norm(sex="M", age=40))
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list assignment index out of range",
        )

        distrib = facet.distrib(size=7, b5=b5, norm=Norm(sex="M", age=40))
        assert isinstance(distrib, dict), "distrib must be a dict"

        self.assertEqual(distrib.get("O")[0], 0)
        self.assertEqual(distrib.get("C")[0], 0)
        self.assertEqual(distrib.get("E")[0], 0)
        self.assertEqual(distrib.get("A")[0], 0)
        self.assertEqual(distrib.get("N")[0], 0)

        self.assertEqual(distrib.get("O")[1], 31.320754716981135)
        self.assertEqual(distrib.get("O")[2], 39.146005509641874)
        self.assertEqual(distrib.get("O")[3], 41.84952978056427)
        self.assertEqual(distrib.get("O")[4], 58.43657817109144)
        self.assertEqual(distrib.get("O")[5], 43.50769230769231)
        self.assertEqual(distrib.get("O")[6], 58.97849462365591)

        self.assertEqual(distrib.get("C")[1], 54.91803278688524)
        self.assertEqual(distrib.get("C")[2], 68.66197183098592)
        self.assertEqual(distrib.get("C")[3], 51.15942028985507)
        self.assertEqual(distrib.get("C")[4], 60.73746312684366)
        self.assertEqual(distrib.get("C")[5], 64.29003021148037)
        self.assertEqual(distrib.get("C")[6], 46.749379652605455)

        self.assertEqual(distrib.get("E")[1], 41.28947368421052)
        self.assertEqual(distrib.get("E")[2], 36.61654135338346)
        self.assertEqual(distrib.get("E")[3], 42.79329608938548)
        self.assertEqual(distrib.get("E")[4], 55.975232198142415)
        self.assertEqual(distrib.get("E")[5], 46.0932944606414)
        self.assertEqual(distrib.get("E")[6], 43.48441926345609)

        self.assertEqual(distrib.get("A")[1], 55.9349593495935)
        self.assertEqual(distrib.get("A")[2], 62.79874213836478)
        self.assertEqual(distrib.get("A")[3], 41.88356164383562)
        self.assertEqual(distrib.get("A")[4], 53.83783783783784)
        self.assertEqual(distrib.get("A")[5], 51.596638655462186)
        self.assertEqual(distrib.get("A")[6], 41.58054711246201)

        self.assertEqual(distrib.get("N")[1], 51.48936170212766)
        self.assertEqual(distrib.get("N")[2], 50.58139534883721)
        self.assertEqual(distrib.get("N")[3], 44.247572815533985)
        self.assertEqual(distrib.get("N")[4], 47.08661417322835)
        self.assertEqual(distrib.get("N")[5], 43.80681818181818)
        self.assertEqual(distrib.get("N")[6], 46.75287356321839)

        distrib = facet.distrib(size=7, b5=b5, norm=Norm(sex="F", age=30))
        assert isinstance(distrib, dict), "distrib must be a dict"

        self.assertEqual(distrib.get("O")[1], 33.113772455089816)
        self.assertEqual(distrib.get("O")[2], 34.93939393939394)
        self.assertEqual(distrib.get("O")[3], 33.605947955390334)
        self.assertEqual(distrib.get("O")[4], 59.18604651162791)
        self.assertEqual(distrib.get("O")[5], 46.31123919308357)
        self.assertEqual(distrib.get("O")[6], 58.49710982658959)

        self.assertEqual(distrib.get("C")[1], 54.18803418803419)
        self.assertEqual(distrib.get("C")[2], 66.25277161862527)
        self.assertEqual(distrib.get("C")[3], 48.58267716535433)
        self.assertEqual(distrib.get("C")[4], 59.47540983606558)
        self.assertEqual(distrib.get("C")[5], 63.74613003095975)
        self.assertEqual(distrib.get("C")[6], 47.822966507177036)

        self.assertEqual(distrib.get("E")[1], 38.9344262295082)
        self.assertEqual(distrib.get("E")[2], 35.382716049382715)
        self.assertEqual(distrib.get("E")[3], 43.767313019390585)
        self.assertEqual(distrib.get("E")[4], 53.7962962962963)
        self.assertEqual(distrib.get("E")[5], 47.62039660056657)
        self.assertEqual(distrib.get("E")[6], 41.05740181268882)

        self.assertEqual(distrib.get("A")[1], 54.98652291105121)
        self.assertEqual(distrib.get("A")[2], 60.191570881226056)
        self.assertEqual(distrib.get("A")[3], 34.940711462450594)
        self.assertEqual(distrib.get("A")[4], 51.22857142857143)
        self.assertEqual(distrib.get("A")[5], 47.25490196078431)
        self.assertEqual(distrib.get("A")[6], 34.250871080139376)

        self.assertEqual(distrib.get("N")[1], 47.065217391304344)
        self.assertEqual(distrib.get("N")[2], 48.256658595641646)
        self.assertEqual(distrib.get("N")[3], 43.14496314496315)
        self.assertEqual(distrib.get("N")[4], 46.83377308707124)
        self.assertEqual(distrib.get("N")[5], 42.43016759776536)
        self.assertEqual(distrib.get("N")[6], 42.60989010989011)
