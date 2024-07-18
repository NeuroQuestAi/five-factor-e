"""Unit tests for Utility."""

import json
import unittest

from ipipneo.utility import (add_dict_footer, answers_is_valid,
                             big5_ocean_is_valid, big5_target,
                             create_big5_dict, organize_list_json,
                             raise_if_age_is_invalid, raise_if_sex_is_invalid,
                             reverse_scored)

LIB_CURRENT_VERSION = "1.12.0"


def load_mock_answers(idx: int) -> dict:
    if idx == 1:
        name = "answers-test-1.json"
    elif idx == 2:
        name = "answers-test-2.json"
    with open(f"test/mock/{name}") as f:
        data = json.load(f)
    return data


class TestUtility(unittest.TestCase):
    maxDiff = None

    def test_raise_if_sex_is_invalid(self) -> None:
        with self.assertRaises(BaseException):
            raise_if_sex_is_invalid(sex="")

        with self.assertRaises(AssertionError):
            raise_if_sex_is_invalid(sex="m")

        with self.assertRaises(AssertionError):
            raise_if_sex_is_invalid(sex="f")

        with self.assertRaises(AssertionError):
            raise_if_sex_is_invalid(sex="male")

        with self.assertRaises(AssertionError):
            raise_if_sex_is_invalid(sex="female")

        self.assertEqual(raise_if_sex_is_invalid(sex="M"), True)
        self.assertEqual(raise_if_sex_is_invalid(sex="F"), True)

    def test_raise_if_age_is_invalid(self) -> None:
        with self.assertRaises(BaseException):
            raise_if_age_is_invalid(age="")

        with self.assertRaises(AssertionError):
            raise_if_age_is_invalid(age="40")

        with self.assertRaises(AssertionError):
            raise_if_age_is_invalid(age=-1)

        with self.assertRaises(AssertionError):
            raise_if_age_is_invalid(age=5)

        with self.assertRaises(AssertionError):
            raise_if_age_is_invalid(age=121)

        with self.assertRaises(AssertionError):
            raise_if_age_is_invalid(age=150)

        with self.assertRaises(AssertionError):
            raise_if_age_is_invalid(age=300)

        self.assertEqual(raise_if_age_is_invalid(age=10), True)
        self.assertEqual(raise_if_age_is_invalid(age=13), True)
        self.assertEqual(raise_if_age_is_invalid(age=15), True)
        self.assertEqual(raise_if_age_is_invalid(age=17), True)
        self.assertEqual(raise_if_age_is_invalid(age=18), True)
        self.assertEqual(raise_if_age_is_invalid(age=21), True)
        self.assertEqual(raise_if_age_is_invalid(age=25), True)
        self.assertEqual(raise_if_age_is_invalid(age=30), True)
        self.assertEqual(raise_if_age_is_invalid(age=35), True)
        self.assertEqual(raise_if_age_is_invalid(age=40), True)
        self.assertEqual(raise_if_age_is_invalid(age=49), True)
        self.assertEqual(raise_if_age_is_invalid(age=50), True)
        self.assertEqual(raise_if_age_is_invalid(age=61), True)
        self.assertEqual(raise_if_age_is_invalid(age=80), True)
        self.assertEqual(raise_if_age_is_invalid(age=90), True)
        self.assertEqual(raise_if_age_is_invalid(age=100), True)
        self.assertEqual(raise_if_age_is_invalid(age=105), True)
        self.assertEqual(raise_if_age_is_invalid(age=110), True)

    def test_answers_is_valid(self) -> None:
        with self.assertRaises(BaseException):
            answers_is_valid(answers="")

        with self.assertRaises(BaseException):
            answers_is_valid(answers=[])

        with self.assertRaises(BaseException):
            answers_is_valid(answers=["A"])

        with self.assertRaises(BaseException):
            answers_is_valid(answers=[1, 2, 3, 4, 5])

        with self.assertRaises(BaseException):
            answers_is_valid(answers=[-1, -2, -3, -4, -5])

        with self.assertRaises(BaseException):
            answers_is_valid(answers=[0, 5, 10])

        with self.assertRaises(BaseException):
            answers_is_valid(answers=list(range(1, 121)))

        self.assertEqual(
            answers_is_valid(
                answers=[
                    1,
                    2,
                    3,
                    4,
                    3,
                    2,
                    2,
                    3,
                    3,
                    2,
                    3,
                    3,
                    3,
                    2,
                    3,
                    2,
                    1,
                    1,
                    4,
                    3,
                    4,
                    4,
                    5,
                    1,
                    4,
                    2,
                    3,
                    3,
                    3,
                    2,
                    4,
                    4,
                    1,
                    3,
                    3,
                    2,
                    4,
                    1,
                    3,
                    3,
                    5,
                    5,
                    4,
                    4,
                    3,
                    2,
                    3,
                    4,
                    2,
                    1,
                    3,
                    4,
                    1,
                    2,
                    3,
                    5,
                    2,
                    3,
                    4,
                    3,
                    2,
                    3,
                    2,
                    3,
                    3,
                    2,
                    3,
                    3,
                    3,
                    4,
                    3,
                    1,
                    3,
                    3,
                    3,
                    2,
                    3,
                    5,
                    2,
                    1,
                    2,
                    3,
                    2,
                    1,
                    4,
                    1,
                    3,
                    2,
                    1,
                    3,
                    2,
                    3,
                    5,
                    2,
                    4,
                    1,
                    3,
                    4,
                    3,
                    3,
                    2,
                    4,
                    3,
                    4,
                    4,
                    3,
                    2,
                    1,
                    2,
                    3,
                    3,
                    4,
                    1,
                    4,
                    4,
                    3,
                    3,
                    3,
                    4,
                    3,
                ]
            ),
            True,
        )

        a = [
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

        b = organize_list_json(answers=load_mock_answers(idx=1))
        assert isinstance(b, list), "b must be a list"
        self.assertEqual(a, b)

        c = organize_list_json(answers=load_mock_answers(idx=2))
        assert isinstance(c, list), "c must be a list"
        self.assertEqual(c, b)

    def test_organize_list_json(self) -> None:
        with self.assertRaises(AssertionError):
            organize_list_json(answers="")

        with self.assertRaises(BaseException):
            organize_list_json(answers={"A": []})

        with self.assertRaises(BaseException):
            organize_list_json(answers={"answers": []})

        with self.assertRaises(BaseException):
            organize_list_json(answers={"answers": [{"id_question": 1}]})

        with self.assertRaises(BaseException):
            organize_list_json(answers={"answers": [{"id_select": 1}]})

        data = {
            "answers": [
                {"id_question": 1, "id_select": 1},
                {"id_question": 2, "id_select": 2},
                {"id_question": 3, "id_select": 3},
                {"id_question": 4, "id_select": 4},
                {"id_question": 5, "id_select": 5},
            ]
        }

        answers = organize_list_json(answers=data)
        assert isinstance(answers, list), "answers must be a list"
        self.assertEqual(len(answers), 5)

    def test_big5_ocean_is_valid(self) -> None:
        with self.assertRaises(BaseException) as e:
            big5_ocean_is_valid(label="")
        self.assertEqual(str(e.exception), "The Big-Five label is invalid!")

        with self.assertRaises(BaseException) as e:
            big5_ocean_is_valid(label="OCEAN")
        self.assertEqual(str(e.exception), "The Big-Five label is invalid!")

        self.assertEqual(big5_ocean_is_valid(label="O"), True)
        self.assertEqual(big5_ocean_is_valid(label="C"), True)
        self.assertEqual(big5_ocean_is_valid(label="E"), True)
        self.assertEqual(big5_ocean_is_valid(label="A"), True)
        self.assertEqual(big5_ocean_is_valid(label="N"), True)

    def test_big5_target(self) -> None:
        with self.assertRaises(BaseException) as e:
            big5_target(label="")
        self.assertEqual(str(e.exception), "The Big-Five label is invalid!")

        O = list(map(str, big5_target(label="O")))
        C = list(map(str, big5_target(label="C")))
        E = list(map(str, big5_target(label="E")))
        A = list(map(str, big5_target(label="A")))
        N = list(map(str, big5_target(label="N")))

        self.assertEqual(len(O), 6)
        self.assertEqual(len(C), 6)
        self.assertEqual(len(E), 6)
        self.assertEqual(len(A), 6)
        self.assertEqual(len(N), 6)

    def test_create_big5_dict(self) -> None:
        N = {
            "label": "N",
            "big5": 37.23631660596993,
            "x": [
                0,
                55.29153291804727,
                52.068589887460575,
                30.04288206625688,
                39.69850290396829,
                28.601999121511483,
                38.536490293892996,
            ],
            "y": [
                0,
                "average",
                "average",
                "low",
                "average",
                "low",
                "average",
            ],
        }
        N = create_big5_dict(
            label=N.get("label"), big5=N.get("big5"), x=N.get("x"), y=N.get("y")
        )
        assert isinstance(N, dict), "N must be a dict"
        self.assertEqual(N.get("N"), 37.23631660596993)
        assert isinstance(N.get("traits"), list), "traits must be a list"

        E = {
            "label": "E",
            "big5": 21.46713047820697,
            "x": [
                0,
                20.788746198012063,
                8.857170154068399,
                25.365062122504668,
                70.68785093930268,
                36.25782829248527,
                27.560328329400278,
            ],
            "y": [
                0,
                "low",
                "low",
                "low",
                "high",
                "average",
                "low",
            ],
        }

        E = create_big5_dict(
            label=E.get("label"), big5=E.get("big5"), x=E.get("x"), y=E.get("y")
        )
        assert isinstance(E, dict), "N must be a dict"
        self.assertEqual(E.get("E"), 21.46713047820697)
        assert isinstance(E.get("traits"), list), "traits must be a list"

        O = {
            "label": "O",
            "big5": 26.882298529738506,
            "x": [
                0,
                1,
                14.832308817371768,
                22.458638690321635,
                78.39980163147527,
                27.6351617847169,
                79.99472618213304,
            ],
            "y": [
                0,
                "low",
                "low",
                "low",
                "high",
                "low",
                "high",
            ],
        }

        O = create_big5_dict(
            label=O.get("label"), big5=O.get("big5"), x=O.get("x"), y=O.get("y")
        )
        assert isinstance(O, dict), "O must be a dict"
        self.assertEqual(O.get("O"), 26.882298529738506)
        assert isinstance(O.get("traits"), list), "traits must be a list"

        A = {
            "label": "A",
            "big5": 57.52658875205816,
            "x": [
                0,
                70.5561195632738,
                89.87557658724631,
                22.561476501041227,
                63.50546308998889,
                55.67124528467815,
                21.651269458084244,
            ],
            "y": [
                0,
                "high",
                "high",
                "low",
                "average",
                "average",
                "low",
            ],
        }

        A = create_big5_dict(
            label=A.get("label"), big5=A.get("big5"), x=A.get("x"), y=A.get("y")
        )
        assert isinstance(A, dict), "A must be a dict"
        self.assertEqual(A.get("A"), 57.52658875205816)
        assert isinstance(A.get("traits"), list), "traits must be a list"

        C = {
            "label": "C",
            "big5": 86.96687032595662,
            "x": [
                0,
                67.18081968991703,
                98.82696217870512,
                54.122030713014226,
                84.86323430898972,
                92.95956099997227,
                38.524355262005315,
            ],
            "y": [
                0,
                "average",
                "high",
                "average",
                "high",
                "high",
                "average",
            ],
        }

        C = create_big5_dict(
            label=C.get("label"), big5=C.get("big5"), x=C.get("x"), y=C.get("y")
        )
        assert isinstance(C, dict), "A must be a dict"
        self.assertEqual(C.get("C"), 86.96687032595662)
        assert isinstance(C.get("traits"), list), "traits must be a list"

    def test_reverse_scored(self) -> None:
        with self.assertRaises(TypeError) as e:
            reverse_scored(a=1)

        with self.assertRaises(BaseException) as e:
            reverse_scored(select=900)
        self.assertEqual(
            str(e.exception), "Something wrong in the selection option: 900"
        )

        self.assertEqual(reverse_scored(select=1), 5)
        self.assertEqual(reverse_scored(select=2), 4)
        self.assertEqual(reverse_scored(select=3), 3)
        self.assertEqual(reverse_scored(select=4), 2)
        self.assertEqual(reverse_scored(select=5), 1)

    def test_add_dict_footer(self) -> None:
        footer = add_dict_footer()
        assert isinstance(footer, dict), "footer must be a dict"

        self.assertEqual(footer.get("library"), "five-factor-e")
        self.assertEqual(footer.get("version"), LIB_CURRENT_VERSION)
