"""Unit tests for Facet."""

import json
import unittest

from ipipneo.facet import Facet
from ipipneo.norm import Norm
from ipipneo.utility import organize_list_json


def load_mock_answers_120() -> dict:
    with open("test/mock/answers-test-1.json") as f:
        data = json.load(f)
    return data


def load_mock_answers_300() -> dict:
    with open("test/mock/answers-test-4.json") as f:
        data = json.load(f)
    return data


class TestFacet(unittest.TestCase):
    def test_invalid_params(self) -> None:
        with self.assertRaises(TypeError):
            Facet()

        with self.assertRaises(BaseException):
            Facet(nquestion="")

        with self.assertRaises(BaseException):
            Facet(nquestion=0)

        self.assertEqual(Facet(nquestion=120).__class__.__name__, "Facet")
        self.assertEqual(Facet(nquestion=300).__class__.__name__, "Facet")

    def test_score_120(self) -> None:
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

        score = facet.score(answers=organize_list_json(load_mock_answers_120()))
        assert isinstance(score, list), "score must be a list"
        self.assertEqual(len(score), 121)

    def test_score_300(self) -> None:
        facet = Facet(nquestion=300)

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

        with self.assertRaises(BaseException) as e:
            facet.score(answers=organize_list_json(load_mock_answers_120()))
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list index out of range",
        )

        score = facet.score(answers=organize_list_json(load_mock_answers_300()))
        assert isinstance(score, list), "score must be a list"
        self.assertEqual(len(score), 301)

    def test_b5create_120(self) -> None:
        facet = Facet(nquestion=120)

        with self.assertRaises(BaseException) as e:
            facet.b5create(score=[0, 0, 0])
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list index out of range",
        )

        b5 = facet.b5create(
            score=facet.score(answers=organize_list_json(load_mock_answers_120()))
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

    def test_b5create_300(self) -> None:
        facet = Facet(nquestion=300)

        with self.assertRaises(BaseException) as e:
            facet.b5create(score=[0, 0, 0])
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list index out of range",
        )

        b5 = facet.b5create(
            score=facet.score(answers=organize_list_json(load_mock_answers_300()))
        )
        assert isinstance(b5, dict), "b5 must be a dict"

        self.assertEqual(len(b5.get("O")), 301)
        self.assertEqual(len(b5.get("C")), 301)
        self.assertEqual(len(b5.get("E")), 301)
        self.assertEqual(len(b5.get("A")), 301)
        self.assertEqual(len(b5.get("N")), 301)

        self.assertEqual(b5.get("O")[0], 0)
        self.assertEqual(b5.get("C")[0], 0)
        self.assertEqual(b5.get("E")[0], 0)
        self.assertEqual(b5.get("A")[0], 0)
        self.assertEqual(b5.get("N")[0], 0)

    def test_domain_120(self) -> None:
        facet = Facet(nquestion=120)

        with self.assertRaises(BaseException) as e:
            facet.domain(score=[-1, -1, -1])
        self.assertEqual(
            str(e.exception),
            "Invalid position in the score array: list index out of range",
        )

        domain = facet.domain(
            score=facet.score(answers=organize_list_json(load_mock_answers_120()))
        )
        assert isinstance(domain, dict), "domain must be a dict"

        self.assertEqual(domain.get("O"), 78)
        self.assertEqual(domain.get("C"), 102)
        self.assertEqual(domain.get("E"), 66)
        self.assertEqual(domain.get("A"), 87)
        self.assertEqual(domain.get("N"), 61)

    def test_domain_300(self) -> None:
        facet = Facet(nquestion=300)

        with self.assertRaises(BaseException) as e:
            facet.domain(score=[-1, -1, -1])
        self.assertEqual(
            str(e.exception),
            "Invalid position in the score array: list index out of range",
        )

        domain = facet.domain(
            score=facet.score(answers=organize_list_json(load_mock_answers_300()))
        )
        assert isinstance(domain, dict), "domain must be a dict"

        self.assertEqual(domain.get("O"), 180)
        self.assertEqual(domain.get("C"), 183)
        self.assertEqual(domain.get("E"), 188)
        self.assertEqual(domain.get("A"), 188)
        self.assertEqual(domain.get("N"), 187)

    def test_distrib_120(self) -> None:
        facet = Facet(nquestion=120)

        with self.assertRaises(TypeError):
            facet.distrib(size=0, b5={}, norm={})

        b5 = facet.b5create(
            score=facet.score(answers=organize_list_json(load_mock_answers_120()))
        )
        assert isinstance(b5, dict), "b5 must be a dict"

        domain = facet.domain(
            score=facet.score(answers=organize_list_json(load_mock_answers_120()))
        )
        assert isinstance(domain, dict), "domain must be a dict"

        with self.assertRaises(BaseException) as e:
            facet.distrib(size=0, b5=b5, norm=Norm(sex="M", age=40, nquestion=120))
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list assignment index out of range",
        )

        distrib = facet.distrib(
            size=7, b5=b5, norm=Norm(sex="M", age=40, nquestion=120)
        )
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

        distrib = facet.distrib(
            size=7, b5=b5, norm=Norm(sex="F", age=30, nquestion=120)
        )
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

    def test_distrib_300(self) -> None:
        facet = Facet(nquestion=300)

        with self.assertRaises(TypeError):
            facet.distrib(size=0, b5={}, norm={})

        b5 = facet.b5create(
            score=facet.score(answers=organize_list_json(load_mock_answers_300()))
        )
        assert isinstance(b5, dict), "b5 must be a dict"

        domain = facet.domain(
            score=facet.score(answers=organize_list_json(load_mock_answers_300()))
        )
        assert isinstance(domain, dict), "domain must be a dict"

        with self.assertRaises(BaseException) as e:
            facet.distrib(size=0, b5=b5, norm=Norm(sex="M", age=40, nquestion=300))
        self.assertEqual(
            str(e.exception),
            "The number of questions setting is wrong: list assignment index out of range",
        )

        distrib = facet.distrib(
            size=7, b5=b5, norm=Norm(sex="M", age=40, nquestion=300)
        )
        assert isinstance(distrib, dict), "distrib must be a dict"

        self.assertEqual(distrib.get("O")[0], 0)
        self.assertEqual(distrib.get("C")[0], 0)
        self.assertEqual(distrib.get("E")[0], 0)
        self.assertEqual(distrib.get("A")[0], 0)
        self.assertEqual(distrib.get("N")[0], 0)

        self.assertEqual(distrib.get("O")[1], 33.18181818181818)
        self.assertEqual(distrib.get("O")[2], 40.735294117647065)
        self.assertEqual(distrib.get("O")[3], 52.38805970149254)
        self.assertEqual(distrib.get("O")[4], 41.21212121212122)
        self.assertEqual(distrib.get("O")[5], 32.23880597014926)
        self.assertEqual(distrib.get("O")[6], 44.074074074074076)

        self.assertEqual(distrib.get("C")[1], 39.99999999999999)
        self.assertEqual(distrib.get("C")[2], 46.15384615384615)
        self.assertEqual(distrib.get("C")[3], 22.931034482758616)
        self.assertEqual(distrib.get("C")[4], 34.776119402985074)
        self.assertEqual(distrib.get("C")[5], 49.64285714285714)
        self.assertEqual(distrib.get("C")[6], 53.561643835616444)

        self.assertEqual(distrib.get("E")[1], 49.876543209876544)
        self.assertEqual(distrib.get("E")[2], 52.098765432098766)
        self.assertEqual(distrib.get("E")[3], 49.199999999999996)
        self.assertEqual(distrib.get("E")[4], 50.666666666666664)
        self.assertEqual(distrib.get("E")[5], 45.0)
        self.assertEqual(distrib.get("E")[6], 46.57142857142858)

        self.assertEqual(distrib.get("A")[1], 51.84210526315789)
        self.assertEqual(distrib.get("A")[2], 40.3125)
        self.assertEqual(distrib.get("A")[3], 44.375)
        self.assertEqual(distrib.get("A")[4], 51.884057971014485)
        self.assertEqual(distrib.get("A")[5], 56.52173913043478)
        self.assertEqual(distrib.get("A")[6], 32.05882352941176)

        self.assertEqual(distrib.get("N")[1], 51.75)
        self.assertEqual(distrib.get("N")[2], 50.0)
        self.assertEqual(distrib.get("N")[3], 57.55102040816326)
        self.assertEqual(distrib.get("N")[4], 52.89473684210526)
        self.assertEqual(distrib.get("N")[5], 51.23287671232877)
        self.assertEqual(distrib.get("N")[6], 68.10810810810811)

    def test_personality_120(self) -> None:
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

        score = facet.score(answers=organize_list_json(load_mock_answers_120()))
        assert isinstance(score, list), "distrib must be a list"
        self.assertEqual(len(score), 121)

        b5 = facet.b5create(score=score)
        assert isinstance(b5, dict), "b5 must be a dict"

        domain = facet.domain(score=score)
        assert isinstance(domain, dict), "domain must be a dict"

        norm = Norm(sex="M", age=40, nquestion=120)
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
        self.assertEqual(N.get("traits")[0]["anxiety"], 55.29153291804727)
        # self.assertEqual(N.get("traits")[0]["score"], "average")

        self.assertEqual(N.get("traits")[1]["trait"], 2)
        self.assertEqual(N.get("traits")[1]["anger"], 52.068589887460575)
        # self.assertEqual(N.get("traits")[1]["score"], "average")

        self.assertEqual(N.get("traits")[2]["trait"], 3)
        self.assertEqual(N.get("traits")[2]["depression"], 30.04288206625688)
        # self.assertEqual(N.get("traits")[2]["score"], "low")

        self.assertEqual(N.get("traits")[3]["trait"], 4)
        self.assertEqual(N.get("traits")[3]["self_consciousness"], 39.69850290396829)
        # self.assertEqual(N.get("traits")[3]["score"], "average")

        self.assertEqual(N.get("traits")[4]["trait"], 5)
        self.assertEqual(N.get("traits")[4]["immoderation"], 28.601999121511483)
        # self.assertEqual(N.get("traits")[4]["score"], "low")

        self.assertEqual(N.get("traits")[5]["trait"], 6)
        self.assertEqual(N.get("traits")[5]["vulnerability"], 38.536490293892996)
        # self.assertEqual(N.get("traits")[5]["score"], "average")

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
        self.assertEqual(E.get("traits")[0]["friendliness"], 20.788746198012063)
        # self.assertEqual(E.get("traits")[0]["score"], "low")

        self.assertEqual(E.get("traits")[1]["trait"], 2)
        self.assertEqual(E.get("traits")[1]["gregariousness"], 8.857170154068399)
        # self.assertEqual(E.get("traits")[1]["score"], "low")

        self.assertEqual(E.get("traits")[2]["trait"], 3)
        self.assertEqual(E.get("traits")[2]["assertiveness"], 25.365062122504668)
        # self.assertEqual(E.get("traits")[2]["score"], "low")

        self.assertEqual(E.get("traits")[3]["trait"], 4)
        self.assertEqual(E.get("traits")[3]["activity_level"], 70.68785093930268)
        # self.assertEqual(E.get("traits")[3]["score"], "high")

        self.assertEqual(E.get("traits")[4]["trait"], 5)
        self.assertEqual(E.get("traits")[4]["excitement_seeking"], 36.25782829248527)
        # self.assertEqual(E.get("traits")[4]["score"], "average")

        self.assertEqual(E.get("traits")[5]["trait"], 6)
        self.assertEqual(E.get("traits")[5]["cheerfulness"], 27.560328329400278)
        # self.assertEqual(E.get("traits")[5]["score"], "low")

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
        self.assertEqual(O.get("traits")[0]["imagination"], 1)
        # self.assertEqual(O.get("traits")[0]["score"], "low")

        self.assertEqual(O.get("traits")[1]["trait"], 2)
        self.assertEqual(O.get("traits")[1]["artistic_interests"], 14.832308817371768)
        # self.assertEqual(O.get("traits")[1]["score"], "low")

        self.assertEqual(O.get("traits")[2]["trait"], 3)
        self.assertEqual(O.get("traits")[2]["emotionality"], 22.458638690321635)
        # self.assertEqual(O.get("traits")[2]["score"], "low")

        self.assertEqual(O.get("traits")[3]["trait"], 4)
        self.assertEqual(O.get("traits")[3]["adventurousness"], 78.39980163147527)
        # self.assertEqual(O.get("traits")[3]["score"], "high")

        self.assertEqual(O.get("traits")[4]["trait"], 5)
        self.assertEqual(O.get("traits")[4]["intellect"], 27.6351617847169)
        # self.assertEqual(O.get("traits")[4]["score"], "low")

        self.assertEqual(O.get("traits")[5]["trait"], 6)
        self.assertEqual(O.get("traits")[5]["liberalism"], 79.99472618213304)
        # self.assertEqual(O.get("traits")[5]["score"], "high")

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
        self.assertEqual(A.get("traits")[0]["trust"], 70.5561195632738)
        # self.assertEqual(A.get("traits")[0]["score"], "high")

        self.assertEqual(A.get("traits")[1]["trait"], 2)
        self.assertEqual(A.get("traits")[1]["morality"], 89.87557658724631)
        # self.assertEqual(A.get("traits")[1]["score"], "high")

        self.assertEqual(A.get("traits")[2]["trait"], 3)
        self.assertEqual(A.get("traits")[2]["altruism"], 22.561476501041227)
        # self.assertEqual(A.get("traits")[2]["score"], "low")

        self.assertEqual(A.get("traits")[3]["trait"], 4)
        self.assertEqual(A.get("traits")[3]["cooperation"], 63.50546308998889)
        # self.assertEqual(A.get("traits")[3]["score"], "average")

        self.assertEqual(A.get("traits")[4]["trait"], 5)
        self.assertEqual(A.get("traits")[4]["modesty"], 55.67124528467815)
        # self.assertEqual(A.get("traits")[4]["score"], "average")

        self.assertEqual(A.get("traits")[5]["trait"], 6)
        self.assertEqual(A.get("traits")[5]["sympathy"], 21.651269458084244)
        # self.assertEqual(A.get("traits")[5]["score"], "low")

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
        self.assertEqual(C.get("traits")[0]["self_efficacy"], 67.18081968991703)
        # self.assertEqual(C.get("traits")[0]["score"], "average")

        self.assertEqual(C.get("traits")[1]["trait"], 2)
        self.assertEqual(C.get("traits")[1]["orderliness"], 98.82696217870512)
        # self.assertEqual(C.get("traits")[1]["score"], "high")

        self.assertEqual(C.get("traits")[2]["trait"], 3)
        self.assertEqual(C.get("traits")[2]["dutifulness"], 54.122030713014226)
        # self.assertEqual(C.get("traits")[2]["score"], "average")

        self.assertEqual(C.get("traits")[3]["trait"], 4)
        self.assertEqual(C.get("traits")[3]["achievement_striving"], 84.86323430898972)
        # self.assertEqual(C.get("traits")[3]["score"], "high")

        self.assertEqual(C.get("traits")[4]["trait"], 5)
        self.assertEqual(C.get("traits")[4]["self_discipline"], 92.95956099997227)
        # self.assertEqual(C.get("traits")[4]["score"], "high")

        self.assertEqual(C.get("traits")[5]["trait"], 6)
        self.assertEqual(C.get("traits")[5]["cautiousness"], 38.524355262005315)
        # self.assertEqual(C.get("traits")[5]["score"], "average")

        #############################################
        # MOCK: High values
        #############################################

        # >> 1
        N = facet.personality(
            size=121,
            big5={"O": 99.99, "C": 99.99, "E": 99.99, "A": 99.99, "N": 99.99},
            traits={
                "N": [
                    0,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                ]
            },
            label="N",
        )
        assert isinstance(N, dict), "N must be a dict"
        self.assertEqual(N.get("N"), 99.99)

        for x in N.get("traits", []):
            self.assertEqual(x.get("score"), "high")

        # >> 2
        E = facet.personality(
            size=121,
            big5={"O": 99.99, "C": 99.99, "E": 99.99, "A": 99.99, "N": 99.99},
            traits={
                "E": [
                    0,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                ]
            },
            label="E",
        )
        assert isinstance(E, dict), "E must be a dict"
        self.assertEqual(E.get("E"), 99.99)

        for x in E.get("traits", []):
            self.assertEqual(x.get("score"), "high")

        # >> 3
        O = facet.personality(
            size=121,
            big5={"O": 99.99, "C": 99.99, "E": 99.99, "A": 99.99, "N": 99.99},
            traits={
                "O": [
                    0,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                ]
            },
            label="O",
        )
        assert isinstance(O, dict), "O must be a dict"
        self.assertEqual(O.get("O"), 99.99)

        for x in O.get("traits", []):
            self.assertEqual(x.get("score"), "high")

        # >> 4
        A = facet.personality(
            size=121,
            big5={"O": 99.99, "C": 99.99, "E": 99.99, "A": 99.99, "N": 99.99},
            traits={
                "A": [
                    0,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                ]
            },
            label="A",
        )
        assert isinstance(A, dict), "A must be a dict"
        self.assertEqual(A.get("A"), 99.99)

        for x in A.get("traits", []):
            self.assertEqual(x.get("score"), "high")

        # >> 5
        C = facet.personality(
            size=121,
            big5={"O": 99.99, "C": 99.99, "E": 99.99, "A": 99.99, "N": 99.99},
            traits={
                "C": [
                    0,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                    99.99,
                ]
            },
            label="C",
        )
        assert isinstance(C, dict), "C must be a dict"
        self.assertEqual(C.get("C"), 99.99)

        for x in C.get("traits", []):
            self.assertEqual(x.get("score"), "high")

        #############################################
        # MOCK: Low values
        #############################################

        # >> 1
        N = facet.personality(
            size=121,
            big5={"O": 0.0, "C": 0.0, "E": 0.0, "A": 0.0, "N": 0.0},
            traits={
                "N": [
                    0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ]
            },
            label="N",
        )
        assert isinstance(N, dict), "N must be a dict"
        self.assertEqual(N.get("N"), 0)

        for x in N.get("traits", []):
            self.assertEqual(x.get("score"), "low")

        # >> 2
        E = facet.personality(
            size=121,
            big5={"O": 0.0, "C": 0.0, "E": 0.0, "A": 0.0, "N": 0.0},
            traits={
                "E": [
                    0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ]
            },
            label="E",
        )
        assert isinstance(E, dict), "E must be a dict"
        self.assertEqual(E.get("E"), 0)

        for x in E.get("traits", []):
            self.assertEqual(x.get("score"), "low")

        # >> 3
        O = facet.personality(
            size=121,
            big5={"O": 0.0, "C": 0.0, "E": 0.0, "A": 0.0, "N": 0.0},
            traits={
                "O": [
                    0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ]
            },
            label="O",
        )
        assert isinstance(O, dict), "O must be a dict"
        self.assertEqual(O.get("O"), 0)

        for x in O.get("traits", []):
            self.assertEqual(x.get("score"), "low")

        # >> 4
        A = facet.personality(
            size=121,
            big5={"O": 0.0, "C": 0.0, "E": 0.0, "A": 0.0, "N": 0.0},
            traits={
                "A": [
                    0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ]
            },
            label="A",
        )
        assert isinstance(A, dict), "A must be a dict"
        self.assertEqual(A.get("A"), 0)

        for x in O.get("traits", []):
            self.assertEqual(x.get("score"), "low")

        # >> 5
        C = facet.personality(
            size=121,
            big5={"O": 0.0, "C": 0.0, "E": 0.0, "A": 0.0, "N": 0.0},
            traits={
                "C": [
                    0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ]
            },
            label="C",
        )
        assert isinstance(C, dict), "C must be a dict"
        self.assertEqual(C.get("C"), 0)

        for x in C.get("traits", []):
            self.assertEqual(x.get("score"), "low")

    def test_personality_300(self) -> None:
        facet = Facet(nquestion=300)

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

        score = facet.score(answers=organize_list_json(load_mock_answers_300()))
        assert isinstance(score, list), "distrib must be a list"
        self.assertEqual(len(score), 301)

        b5 = facet.b5create(score=score)
        assert isinstance(b5, dict), "b5 must be a dict"

        domain = facet.domain(score=score)
        assert isinstance(domain, dict), "domain must be a dict"

        norm = Norm(sex="M", age=40, nquestion=300)
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

        self.assertEqual(N.get("N"), 72.42696555428512)

        self.assertEqual(N.get("traits")[0]["trait"], 1)
        self.assertEqual(N.get("traits")[0]["anxiety"], 56.21355262825239)
        self.assertEqual(N.get("traits")[0]["score"], "average")

        self.assertEqual(N.get("traits")[1]["trait"], 2)
        self.assertEqual(N.get("traits")[1]["anger"], 49.99999999999858)
        self.assertEqual(N.get("traits")[1]["score"], "average")

        self.assertEqual(N.get("traits")[2]["trait"], 3)
        self.assertEqual(N.get("traits")[2]["depression"], 75.7080910490638)
        self.assertEqual(N.get("traits")[2]["score"], "high")

        self.assertEqual(N.get("traits")[3]["trait"], 4)
        self.assertEqual(N.get("traits")[3]["self_consciousness"], 60.2364043211619)
        self.assertEqual(N.get("traits")[3]["score"], "average")

        self.assertEqual(N.get("traits")[4]["trait"], 5)
        self.assertEqual(N.get("traits")[4]["immoderation"], 54.38260045296113)
        self.assertEqual(N.get("traits")[4]["score"], "average")

        self.assertEqual(N.get("traits")[5]["trait"], 6)
        self.assertEqual(N.get("traits")[5]["vulnerability"], 98.37585552257963)
        self.assertEqual(N.get("traits")[5]["score"], "high")

        #############################################
        # 2. Extraversion with its facets.
        #############################################
        E = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="E"
        )
        assert isinstance(N, dict), "E must be a dict"
        assert isinstance(N.get("traits"), list), "traits must be a list"

        self.assertEqual(E.get("E"), 44.65415108872236)

        self.assertEqual(E.get("traits")[0]["trait"], 1)
        self.assertEqual(E.get("traits")[0]["friendliness"], 49.56063603396092)
        self.assertEqual(E.get("traits")[0]["score"], "average")

        self.assertEqual(E.get("traits")[1]["trait"], 2)
        self.assertEqual(E.get("traits")[1]["gregariousness"], 57.44425564700225)
        self.assertEqual(E.get("traits")[1]["score"], "average")

        self.assertEqual(E.get("traits")[2]["trait"], 3)
        self.assertEqual(E.get("traits")[2]["assertiveness"], 47.15427409876639)
        self.assertEqual(E.get("traits")[2]["score"], "average")

        self.assertEqual(E.get("traits")[3]["trait"], 4)
        self.assertEqual(E.get("traits")[3]["activity_level"], 52.371791064982006)
        self.assertEqual(E.get("traits")[3]["score"], "average")

        self.assertEqual(E.get("traits")[4]["trait"], 5)
        self.assertEqual(E.get("traits")[4]["excitement_seeking"], 32.54383356563801)
        self.assertEqual(E.get("traits")[4]["score"], "average")

        self.assertEqual(E.get("traits")[5]["trait"], 6)
        self.assertEqual(E.get("traits")[5]["cheerfulness"], 37.907163869258454)
        self.assertEqual(E.get("traits")[5]["score"], "average")

        #############################################
        # 3. Openness with its facets.
        #############################################
        O = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="O"
        )
        assert isinstance(O, dict), "O must be a dict"
        assert isinstance(O.get("traits"), list), "traits must be a list"

        self.assertEqual(O.get("O"), 6.765261759154043)

        self.assertEqual(O.get("traits")[0]["trait"], 1)
        self.assertEqual(O.get("traits")[0]["imagination"], 3.019669333842657)
        self.assertEqual(O.get("traits")[0]["score"], "low")

        self.assertEqual(O.get("traits")[1]["trait"], 2)
        self.assertEqual(O.get("traits")[1]["artistic_interests"], 19.180033328925163)
        self.assertEqual(O.get("traits")[1]["score"], "low")

        self.assertEqual(O.get("traits")[2]["trait"], 3)
        self.assertEqual(O.get("traits")[2]["emotionality"], 58.46198478449537)
        self.assertEqual(O.get("traits")[2]["score"], "average")

        self.assertEqual(O.get("traits")[3]["trait"], 4)
        self.assertEqual(O.get("traits")[3]["adventurousness"], 20.561530401874762)
        self.assertEqual(O.get("traits")[3]["score"], "low")

        self.assertEqual(O.get("traits")[4]["trait"], 5)
        self.assertEqual(O.get("traits")[4]["intellect"], 1.9528124319700737)
        self.assertEqual(O.get("traits")[4]["score"], "low")

        self.assertEqual(O.get("traits")[5]["trait"], 6)
        self.assertEqual(O.get("traits")[5]["liberalism"], 29.473450015379456)
        self.assertEqual(O.get("traits")[5]["score"], "low")

        #############################################
        # 4. Agreeableness with its facets.
        #############################################
        A = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="A"
        )
        assert isinstance(A, dict), "A must be a dict"
        assert isinstance(A.get("traits"), list), "traits must be a list"

        self.assertEqual(A.get("A"), 31.13757270081055)

        self.assertEqual(A.get("traits")[0]["trait"], 1)
        self.assertEqual(A.get("traits")[0]["trust"], 56.53893235643574)
        self.assertEqual(A.get("traits")[0]["score"], "average")

        self.assertEqual(A.get("traits")[1]["trait"], 2)
        self.assertEqual(A.get("traits")[1]["morality"], 17.983638162857602)
        self.assertEqual(A.get("traits")[1]["score"], "low")

        self.assertEqual(A.get("traits")[2]["trait"], 3)
        self.assertEqual(A.get("traits")[2]["altruism"], 30.46290046715066)
        self.assertEqual(A.get("traits")[2]["score"], "low")

        self.assertEqual(A.get("traits")[3]["trait"], 4)
        self.assertEqual(A.get("traits")[3]["cooperation"], 56.687055095672974)
        self.assertEqual(A.get("traits")[3]["score"], "average")

        self.assertEqual(A.get("traits")[4]["trait"], 5)
        self.assertEqual(A.get("traits")[4]["modesty"], 72.45946413723033)
        self.assertEqual(A.get("traits")[4]["score"], "high")

        self.assertEqual(A.get("traits")[5]["trait"], 6)
        self.assertEqual(A.get("traits")[5]["sympathy"], 1.7779210136593235)
        self.assertEqual(A.get("traits")[5]["score"], "low")

        #############################################
        # 5. Conscientiousness with its facets.
        #############################################
        C = facet.personality(
            size=len(score), big5=normalize, traits=distrib, label="C"
        )
        assert isinstance(C, dict), "C must be a dict"
        assert isinstance(C.get("traits"), list), "traits must be a list"

        self.assertEqual(C.get("C"), 15.799085796472156)

        self.assertEqual(C.get("traits")[0]["trait"], 1)
        self.assertEqual(C.get("traits")[0]["self_efficacy"], 17.11734969494421)
        self.assertEqual(C.get("traits")[0]["score"], "low")

        self.assertEqual(C.get("traits")[1]["trait"], 2)
        self.assertEqual(C.get("traits")[1]["orderliness"], 36.46593774743093)
        self.assertEqual(C.get("traits")[1]["score"], "average")

        self.assertEqual(C.get("traits")[2]["trait"], 3)
        self.assertEqual(C.get("traits")[2]["dutifulness"], 1)
        self.assertEqual(C.get("traits")[2]["score"], "low")

        self.assertEqual(C.get("traits")[3]["trait"], 4)
        self.assertEqual(C.get("traits")[3]["achievement_striving"], 5.368564900396208)
        self.assertEqual(C.get("traits")[3]["score"], "low")

        self.assertEqual(C.get("traits")[4]["trait"], 5)
        self.assertEqual(C.get("traits")[4]["self_discipline"], 48.729091361349106)
        self.assertEqual(C.get("traits")[4]["score"], "average")

        self.assertEqual(C.get("traits")[5]["trait"], 6)
        self.assertEqual(C.get("traits")[5]["cautiousness"], 62.553226842568904)
        self.assertEqual(C.get("traits")[5]["score"], "average")

    def test_big_five_level(self) -> None:
        facet = Facet(nquestion=120)

        O = facet.big_five_level(big5={"O": 10.0}, label="O")
        assert isinstance(O, dict), "O must be a dict 1"

        self.assertIn("score", O.keys())
        self.assertEqual(O.get("score"), "low")

        O = facet.big_five_level(big5={"O": 45.0}, label="O")
        assert isinstance(O, dict), "O must be a dict 2"

        self.assertIn("score", O.keys())
        self.assertEqual(O.get("score"), "average")

        O = facet.big_five_level(big5={"O": 50.0}, label="O")
        assert isinstance(O, dict), "O must be a dict 3"

        self.assertIn("score", O.keys())
        self.assertEqual(O.get("score"), "average")

        O = facet.big_five_level(big5={"O": 55.1}, label="O")
        assert isinstance(O, dict), "O must be a dict 4"

        self.assertIn("score", O.keys())
        self.assertEqual(O.get("score"), "average")

        O = facet.big_five_level(big5={"O": 60.0}, label="O")
        assert isinstance(O, dict), "O must be a dict 5"

        self.assertIn("score", O.keys())
        self.assertEqual(O.get("score"), "high")

        O = facet.big_five_level(big5={"O": 105.99}, label="O")
        assert isinstance(O, dict), "O must be a dict 6"

        self.assertIn("score", O.keys())
        self.assertEqual(O.get("score"), "high")

        A = {
            "A": 13.93553274424201,
            "score": "high",
            "traits": [
                {"trait": 1, "trust": 55.28135202338723, "score": "low"},
                {"trait": 2, "morality": 15.78631677448837, "score": "average"},
                {"trait": 3, "altruism": 1, "score": "high"},
                {"trait": 4, "cooperation": 3.5064568632656545, "score": "high"},
                {"trait": 5, "modesty": 55.58203895537741, "score": "low"},
                {"trait": 6, "sympathy": 42.58820505516337, "score": "high"},
            ],
        }
        A = facet.big_five_level(big5=A, label="A")
        assert isinstance(A, dict), "A must be a dict 6"

        self.assertEqual(A["score"], "low")
        self.assertEqual(A["traits"][0]["score"], "average")
        self.assertEqual(A["traits"][1]["score"], "low")
        self.assertEqual(A["traits"][2]["score"], "low")
        self.assertEqual(A["traits"][3]["score"], "low")
        self.assertEqual(A["traits"][4]["score"], "average")
        self.assertEqual(A["traits"][5]["score"], "low")

        E = {
            "E": 32.92660962191414,
            "score": "high",
            "traits": [
                {"trait": 1, "friendliness": 21.981508523850408, "score": "average"},
                {"trait": 2, "gregariousness": 60.22647281248504, "score": "low"},
                {"trait": 3, "assertiveness": 13.161331704655908, "score": "high"},
                {"trait": 4, "activity_level": 63.387950876213154, "score": "low"},
                {"trait": 5, "excitement_seeking": 70.76878765562839, "score": "high"},
                {"trait": 6, "cheerfulness": 11.953998059108926, "score": "high"},
            ],
        }

        E = facet.big_five_level(big5=E, label="E")
        assert isinstance(E, dict), "E must be a dict 6"

        self.assertEqual(E["score"], "low")
        self.assertEqual(E["traits"][0]["score"], "low")
        self.assertEqual(E["traits"][1]["score"], "high")
        self.assertEqual(E["traits"][2]["score"], "low")
        self.assertEqual(E["traits"][3]["score"], "high")
        self.assertEqual(E["traits"][4]["score"], "high")
        self.assertEqual(E["traits"][5]["score"], "low")

        N = {
            "N": 67.59105722337824,
            "score": "low",
            "traits": [
                {"trait": 1, "anxiety": 56.00057904147229, "score": "low"},
                {"trait": 2, "anger": 80.37525405921429, "score": "low"},
                {"trait": 3, "depression": 76.72120101599137, "score": "low"},
                {
                    "trait": 4,
                    "self_consciousness": 21.97787637601246,
                    "score": "average",
                },
                {"trait": 5, "immoderation": 67.45616643435892, "score": "low"},
                {"trait": 6, "vulnerability": 71.39370970797859, "score": "low"},
            ],
        }

        N = facet.big_five_level(big5=N, label="N")
        assert isinstance(N, dict), "N must be a dict 6"

        self.assertEqual(N["score"], "high")
        self.assertEqual(N["traits"][0]["score"], "high")
        self.assertEqual(N["traits"][1]["score"], "high")
        self.assertEqual(N["traits"][2]["score"], "high")
        self.assertEqual(N["traits"][3]["score"], "low")
        self.assertEqual(N["traits"][4]["score"], "high")
        self.assertEqual(N["traits"][5]["score"], "high")

        N = facet.big_five_level(
            big5=N, label="N", facet_score_level_low=10, facet_score_level_high=75
        )
        assert isinstance(N, dict), "N must be a dict 6"

        self.assertEqual(N["score"], "average")
        self.assertEqual(N["traits"][0]["score"], "average")
        self.assertEqual(N["traits"][1]["score"], "high")
        self.assertEqual(N["traits"][2]["score"], "high")
        self.assertEqual(N["traits"][3]["score"], "average")
        self.assertEqual(N["traits"][4]["score"], "average")
        self.assertEqual(N["traits"][5]["score"], "average")

    def test_score_level(self) -> None:
        facet = Facet(nquestion=120)

        level = facet.score_level(score=-1)
        self.assertEqual(level, "low")

        level = facet.score_level(score=-10)
        self.assertEqual(level, "low")

        level = facet.score_level(score=0)
        self.assertEqual(level, "low")

        level = facet.score_level(score=10)
        self.assertEqual(level, "low")

        level = facet.score_level(score=11.5890)
        self.assertEqual(level, "low")

        level = facet.score_level(score=20)
        self.assertEqual(level, "low")

        level = facet.score_level(score=30)
        self.assertEqual(level, "low")

        level = facet.score_level(score=40)
        self.assertEqual(level, "low")

        level = facet.score_level(score=50)
        self.assertEqual(level, "average")

        level = facet.score_level(score=55)
        self.assertEqual(level, "average")

        level = facet.score_level(score=55.89)
        self.assertEqual(level, "average")

        level = facet.score_level(score=60)
        self.assertEqual(level, "high")

        level = facet.score_level(score=70)
        self.assertEqual(level, "high")

        level = facet.score_level(score=80)
        self.assertEqual(level, "high")

        level = facet.score_level(score=90)
        self.assertEqual(level, "high")

        level = facet.score_level(score=90.50)
        self.assertEqual(level, "high")

        level = facet.score_level(score=100)
        self.assertEqual(level, "high")

        level = facet.score_level(score=110)
        self.assertEqual(level, "high")

        level = facet.score_level(
            score=40, facet_score_level_low=10, facet_score_level_high=50
        )
        self.assertEqual(level, "average")

        level = facet.score_level(
            score=45, facet_score_level_low=70, facet_score_level_high=80
        )
        self.assertEqual(level, "low")

        level = facet.score_level(
            score=80, facet_score_level_low=55, facet_score_level_high=75
        )
        self.assertEqual(level, "high")

        level = Facet(nquestion=300).score_level(score=-1)
        self.assertEqual(level, "low")

        level = Facet(nquestion=300).score_level(score=48)
        self.assertEqual(level, "average")

        level = Facet(nquestion=300).score_level(score=48.5898984)
        self.assertEqual(level, "average")

        level = Facet(nquestion=300).score_level(score=68.140879)
        self.assertEqual(level, "high")

        level = Facet(nquestion=300).score_level(score=99)
        self.assertEqual(level, "high")
