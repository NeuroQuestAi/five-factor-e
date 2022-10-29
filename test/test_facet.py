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

    def test_personality(self) -> None:
        facet = Facet(nquestion=120)

        with self.assertRaises(BaseException) as e:
            facet.personality(size=1, big5={}, traits={}, label="")
        self.assertEqual(
            str(e.exception),
            "The Big-Five label is invalid!",
        )

        with self.assertRaises(BaseException) as e:
            facet.personality(size=1, big5={}, traits={}, label="OCEAN")
        self.assertEqual(
            str(e.exception),
            "The Big-Five label is invalid!",
        )

        with self.assertRaises(BaseException) as e:
            facet.personality(size=1, big5={}, traits={}, label="N")
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list index out of range",
        )

        score = facet.score(answers=organize_list_json(load_mock_answers()))
        assert isinstance(score, list), "distrib must be a list"
        self.assertEqual(len(score), 121)

        b5 = facet.b5create(score=score)
        assert isinstance(b5, dict), "b5 must be a dict"

        domain = facet.domain(score=score)
        assert isinstance(domain, dict), "domain must be a dict"

        norm = Norm(sex="M", age=40)
        assert isinstance(norm, dict), "norm must be a dict"

        normc = Norm.calc(domain=domain, norm=norm)
        assert isinstance(normc, dict), "normc must be a dict"

        distrib = facet.distrib(size=len(score), b5=b5, norm=norm)
        assert isinstance(distrib, dict), "distrib must be a dict"

        percent = Norm.percent(normc=normc)
        assert isinstance(percent, dict), "percent must be a dict"

        normalize = Norm.normalize(normc=normc, percent=percent)
        assert isinstance(normalize, dict), "normalize must be a dict"

        #############################################
        # 1. Neuroticism with its facets.
        #############################################
        N = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="N"
        )
        assert isinstance(N, dict), "N must be a dict"
        assert isinstance(N.get("traits"), list), "traits must be a list"

        self.assertEqual(N.get("N"), 37.23631660596993)

        self.assertEqual(N.get("traits")[0]["trait"], 1)
        self.assertEqual(N.get("traits")[0]["Anxiety"], 55.29153291804727)
        self.assertEqual(N.get("traits")[0]["score"], "average")

        self.assertEqual(N.get("traits")[1]["trait"], 2)
        self.assertEqual(N.get("traits")[1]["Anger"], 52.068589887460575)
        self.assertEqual(N.get("traits")[1]["score"], "average")

        self.assertEqual(N.get("traits")[2]["trait"], 3)
        self.assertEqual(N.get("traits")[2]["Depression"], 30.04288206625688)
        self.assertEqual(N.get("traits")[2]["score"], "low")

        self.assertEqual(N.get("traits")[3]["trait"], 4)
        self.assertEqual(N.get("traits")[3]["Self-Consciousness"], 39.69850290396829)
        self.assertEqual(N.get("traits")[3]["score"], "average")

        self.assertEqual(N.get("traits")[4]["trait"], 5)
        self.assertEqual(N.get("traits")[4]["Immoderation"], 28.601999121511483)
        self.assertEqual(N.get("traits")[4]["score"], "low")

        self.assertEqual(N.get("traits")[5]["trait"], 6)
        self.assertEqual(N.get("traits")[5]["Vulnerability"], 38.536490293892996)
        self.assertEqual(N.get("traits")[5]["score"], "average")

        #############################################
        # 2. Extraversion with its facets.
        #############################################
        E = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="E"
        )
        assert isinstance(N, dict), "E must be a dict"
        assert isinstance(N.get("traits"), list), "traits must be a list"

        self.assertEqual(E.get("E"), 21.46713047820697)

        self.assertEqual(E.get("traits")[0]["trait"], 1)
        self.assertEqual(E.get("traits")[0]["Friendliness"], 20.788746198012063)
        self.assertEqual(E.get("traits")[0]["score"], "low")

        self.assertEqual(E.get("traits")[1]["trait"], 2)
        self.assertEqual(E.get("traits")[1]["Gregariousness"], 8.857170154068399)
        self.assertEqual(E.get("traits")[1]["score"], "low")

        self.assertEqual(E.get("traits")[2]["trait"], 3)
        self.assertEqual(E.get("traits")[2]["Assertiveness"], 25.365062122504668)
        self.assertEqual(E.get("traits")[2]["score"], "low")

        self.assertEqual(E.get("traits")[3]["trait"], 4)
        self.assertEqual(E.get("traits")[3]["Activity-Level"], 70.68785093930268)
        self.assertEqual(E.get("traits")[3]["score"], "high")

        self.assertEqual(E.get("traits")[4]["trait"], 5)
        self.assertEqual(E.get("traits")[4]["Excitement-Seeking"], 36.25782829248527)
        self.assertEqual(E.get("traits")[4]["score"], "average")

        self.assertEqual(E.get("traits")[5]["trait"], 6)
        self.assertEqual(E.get("traits")[5]["Cheerfulness"], 27.560328329400278)
        self.assertEqual(E.get("traits")[5]["score"], "low")

        #############################################
        # 3. Openness with its facets.
        #############################################
        O = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="O"
        )
        assert isinstance(O, dict), "O must be a dict"
        assert isinstance(O.get("traits"), list), "traits must be a list"

        self.assertEqual(O.get("O"), 26.882298529738506)

        self.assertEqual(O.get("traits")[0]["trait"], 1)
        self.assertEqual(O.get("traits")[0]["Imagination"], 1)
        self.assertEqual(O.get("traits")[0]["score"], "low")

        self.assertEqual(O.get("traits")[1]["trait"], 2)
        self.assertEqual(O.get("traits")[1]["Artistic-Interests"], 14.832308817371768)
        self.assertEqual(O.get("traits")[1]["score"], "low")

        self.assertEqual(O.get("traits")[2]["trait"], 3)
        self.assertEqual(O.get("traits")[2]["Emotionality"], 22.458638690321635)
        self.assertEqual(O.get("traits")[2]["score"], "low")

        self.assertEqual(O.get("traits")[3]["trait"], 4)
        self.assertEqual(O.get("traits")[3]["Adventurousness"], 78.39980163147527)
        self.assertEqual(O.get("traits")[3]["score"], "high")

        self.assertEqual(O.get("traits")[4]["trait"], 5)
        self.assertEqual(O.get("traits")[4]["Intellect"], 27.6351617847169)
        self.assertEqual(O.get("traits")[4]["score"], "low")

        self.assertEqual(O.get("traits")[5]["trait"], 6)
        self.assertEqual(O.get("traits")[5]["Liberalism"], 79.99472618213304)
        self.assertEqual(O.get("traits")[5]["score"], "high")

        #############################################
        # 4. Agreeableness with its facets.
        #############################################
        A = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="A"
        )
        assert isinstance(A, dict), "A must be a dict"
        assert isinstance(A.get("traits"), list), "traits must be a list"

        self.assertEqual(A.get("A"), 57.52658875205816)

        self.assertEqual(A.get("traits")[0]["trait"], 1)
        self.assertEqual(A.get("traits")[0]["Trust"], 70.5561195632738)
        self.assertEqual(A.get("traits")[0]["score"], "high")

        self.assertEqual(A.get("traits")[1]["trait"], 2)
        self.assertEqual(A.get("traits")[1]["Morality"], 89.87557658724631)
        self.assertEqual(A.get("traits")[1]["score"], "high")

        self.assertEqual(A.get("traits")[2]["trait"], 3)
        self.assertEqual(A.get("traits")[2]["Altruism"], 22.561476501041227)
        self.assertEqual(A.get("traits")[2]["score"], "low")

        self.assertEqual(A.get("traits")[3]["trait"], 4)
        self.assertEqual(A.get("traits")[3]["Cooperation"], 63.50546308998889)
        self.assertEqual(A.get("traits")[3]["score"], "average")

        self.assertEqual(A.get("traits")[4]["trait"], 5)
        self.assertEqual(A.get("traits")[4]["Modesty"], 55.67124528467815)
        self.assertEqual(A.get("traits")[4]["score"], "average")

        self.assertEqual(A.get("traits")[5]["trait"], 6)
        self.assertEqual(A.get("traits")[5]["Sympathy"], 21.651269458084244)
        self.assertEqual(A.get("traits")[5]["score"], "low")

        #############################################
        # 5. Conscientiousness with its facets.
        #############################################
        C = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="C"
        )
        assert isinstance(C, dict), "C must be a dict"
        assert isinstance(C.get("traits"), list), "traits must be a list"

        self.assertEqual(C.get("C"), 86.96687032595662)

        self.assertEqual(C.get("traits")[0]["trait"], 1)
        self.assertEqual(C.get("traits")[0]["Self-Efficacy"], 67.18081968991703)
        self.assertEqual(C.get("traits")[0]["score"], "average")

        self.assertEqual(C.get("traits")[1]["trait"], 2)
        self.assertEqual(C.get("traits")[1]["Orderliness"], 98.82696217870512)
        self.assertEqual(C.get("traits")[1]["score"], "high")

        self.assertEqual(C.get("traits")[2]["trait"], 3)
        self.assertEqual(C.get("traits")[2]["Dutifulness"], 54.122030713014226)
        self.assertEqual(C.get("traits")[2]["score"], "average")

        self.assertEqual(C.get("traits")[3]["trait"], 4)
        self.assertEqual(C.get("traits")[3]["Achievement-Striving"], 84.86323430898972)
        self.assertEqual(C.get("traits")[3]["score"], "high")

        self.assertEqual(C.get("traits")[4]["trait"], 5)
        self.assertEqual(C.get("traits")[4]["Self-Discipline"], 92.95956099997227)
        self.assertEqual(C.get("traits")[4]["score"], "high")

        self.assertEqual(C.get("traits")[5]["trait"], 6)
        self.assertEqual(C.get("traits")[5]["Cautiousness"], 38.524355262005315)
        self.assertEqual(C.get("traits")[5]["score"], "average")
