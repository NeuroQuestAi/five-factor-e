"""Unit tests for Norm."""

import unittest

from ipipneo.norm import Norm


class TestNorm(unittest.TestCase):
    def test_invalid_params(self) -> None:
        with self.assertRaises(TypeError):
            Norm()

        with self.assertRaises(TypeError):
            Norm(sex="M")

        with self.assertRaises(TypeError):
            Norm(age=0)

        with self.assertRaises(TypeError):
            Norm(sex="M", age=1)

        with self.assertRaises(AssertionError):
            Norm(sex="-", age=1, nquestion=1)

        with self.assertRaises(AssertionError):
            Norm(sex="F", age=121, nquestion=51)

        with self.assertRaises(AssertionError):
            Norm(sex="5", age=5, nquestion=121)

        with self.assertRaises(BaseException) as e:
            Norm(sex="M", age=20, nquestion=121)
        self.assertEqual(str(e.exception), "Type question 121 is invalid!")

        with self.assertRaises(BaseException) as e:
            Norm(sex="F", age=39, nquestion=301)
        self.assertEqual(str(e.exception), "Type question 301 is invalid!")

    def test_norm_output(self) -> None:
        def check(d: dict) -> bool:
            assert isinstance(d, dict), "norm must be a dict"

            self.assertIn("id", d.keys())
            self.assertIn("ns", d.keys())
            self.assertIn("category", d.keys())
            self.assertEqual(len(d), 3)

            assert isinstance(d.get("ns"), list), "norm must be a list"
            self.assertEqual(len(d.get("ns")), 71)
            return True

        #############################################
        # 1. Tests with the IPIP-120 norms.
        #############################################
        norm = Norm(sex="M", age=18, nquestion=120)
        assert check(d=norm), "common failed check 1"
        self.assertEqual(norm.get("id"), 1)
        self.assertEqual(norm.get("category"), "men under 21 years old")

        norm = Norm(sex="F", age=18, nquestion=120)
        assert check(d=norm), "common failed check 2"
        self.assertEqual(norm.get("id"), 5)
        self.assertEqual(norm.get("category"), "women under 21 years old")

        norm = Norm(sex="M", age=21, nquestion=120)
        assert check(d=norm), "common failed check 3"
        self.assertEqual(norm.get("id"), 2)
        self.assertEqual(norm.get("category"), "men between 21 and 40 years old")

        norm = Norm(sex="F", age=30, nquestion=120)
        assert check(d=norm), "common failed check 4"
        self.assertEqual(norm.get("id"), 6)
        self.assertEqual(norm.get("category"), "women between 21 and 40 years old")

        norm = Norm(sex="M", age=41, nquestion=120)
        assert check(d=norm), "common failed check 5"
        self.assertEqual(norm.get("id"), 3)
        self.assertEqual(norm.get("category"), "men between 41 and 60 years of age")

        norm = Norm(sex="F", age=41, nquestion=120)
        assert check(d=norm), "common failed check 6"
        self.assertEqual(norm.get("id"), 7)
        self.assertEqual(norm.get("category"), "women between 41 and 61 years old")

        norm = Norm(sex="M", age=60, nquestion=120)
        assert check(d=norm), "common failed check 7"
        self.assertEqual(norm.get("id"), 3)
        self.assertEqual(norm.get("category"), "men between 41 and 60 years of age")

        norm = Norm(sex="F", age=60, nquestion=120)
        assert check(d=norm), "common failed check 8"
        self.assertEqual(norm.get("id"), 7)
        self.assertEqual(norm.get("category"), "women between 41 and 61 years old")

        norm = Norm(sex="M", age=61, nquestion=120)
        assert check(d=norm), "common failed check 9"
        self.assertEqual(norm.get("id"), 4)
        self.assertEqual(norm.get("category"), "men over 60 years old")

        norm = Norm(sex="F", age=61, nquestion=120)
        assert check(d=norm), "common failed check 10"
        self.assertEqual(norm.get("id"), 8)
        self.assertEqual(norm.get("category"), "women over 60 years old")

        norm = Norm(sex="M", age=80, nquestion=120)
        assert check(d=norm), "common failed check 11"
        self.assertEqual(norm.get("id"), 4)
        self.assertEqual(norm.get("category"), "men over 60 years old")

        norm = Norm(sex="F", age=80, nquestion=120)
        assert check(d=norm), "common failed check 10"
        self.assertEqual(norm.get("id"), 8)
        self.assertEqual(norm.get("category"), "women over 60 years old")

        norm = Norm(sex="M", age=90, nquestion=120)
        assert check(d=norm), "common failed check 11"
        self.assertEqual(norm.get("id"), 4)
        self.assertEqual(norm.get("category"), "men over 60 years old")

        norm = Norm(sex="F", age=90, nquestion=120)
        assert check(d=norm), "common failed check 12"
        self.assertEqual(norm.get("id"), 8)
        self.assertEqual(norm.get("category"), "women over 60 years old")

        #############################################
        # 2. Tests with the IPIP-300 norms.
        #############################################
        norm = Norm(sex="M", age=18, nquestion=300)
        assert check(d=norm), "common failed check 13"
        self.assertEqual(norm.get("id"), 1)
        self.assertEqual(norm.get("category"), "men of traditional college age")

        norm = Norm(sex="M", age=25, nquestion=300)
        assert check(d=norm), "common failed check 14"
        self.assertEqual(norm.get("id"), 2)
        self.assertEqual(norm.get("category"), "adult men")

        norm = Norm(sex="F", age=18, nquestion=300)
        assert check(d=norm), "common failed check 15"
        self.assertEqual(norm.get("id"), 3)
        self.assertEqual(norm.get("category"), "women of traditional college age")

        norm = Norm(sex="F", age=25, nquestion=300)
        assert check(d=norm), "common failed check 16"
        self.assertEqual(norm.get("id"), 4)
        self.assertEqual(norm.get("category"), "adult women")

    def test_calc_120(self):
        normc = Norm.calc(
            domain={"O": 0, "C": 0, "E": 0, "A": 0, "N": 0},
            norm=Norm(sex="M", age=40, nquestion=120),
        )

        assert isinstance(normc, dict), "normc must be a dict"

        self.assertEqual(round(normc.get("O"), 2), -18.39)
        self.assertEqual(round(normc.get("C"), 2), -9.92)
        self.assertEqual(round(normc.get("E"), 2), -1.87)
        self.assertEqual(round(normc.get("A"), 2), -14.29)
        self.assertEqual(round(normc.get("N"), 2), 9.36)

        normc = Norm.calc(
            domain={"O": 99, "C": 99, "E": 99, "A": 99, "N": 99},
            norm=Norm(sex="M", age=40, nquestion=120),
        )

        self.assertGreaterEqual(normc.get("O"), 59)
        self.assertGreaterEqual(normc.get("C"), 59)
        self.assertGreaterEqual(normc.get("E"), 63)
        self.assertGreaterEqual(normc.get("A"), 61)
        self.assertGreaterEqual(normc.get("N"), 69)

        normc = Norm.calc(
            domain={"O": 150, "C": 150, "E": 150, "A": 150, "N": 150},
            norm=Norm(sex="F", age=25, nquestion=120),
        )

        self.assertGreaterEqual(normc.get("O"), 100)
        self.assertGreaterEqual(normc.get("C"), 95)
        self.assertGreaterEqual(normc.get("E"), 97)
        self.assertGreaterEqual(normc.get("A"), 101)
        self.assertGreaterEqual(normc.get("N"), 98)

        a = Norm.calc(
            domain={"N": 61, "A": 87, "C": 102, "E": 66, "O": 78},
            norm=Norm(sex="M", age=40, nquestion=120),
        )

        b = Norm.calc(
            domain={"O": 78, "C": 102, "E": 66, "A": 87, "N": 61},
            norm=Norm(sex="M", age=40, nquestion=120),
        )

        self.assertEqual(a, b)
        self.assertEqual(round(a.get("O"), 2), 43.27)
        self.assertEqual(round(b.get("C"), 2), 61.56)
        self.assertEqual(round(a.get("E"), 2), 41.52)
        self.assertEqual(round(b.get("A"), 2), 52.12)
        self.assertEqual(round(a.get("N"), 2), 46.38)

    def test_calc_300(self):
        normc = Norm.calc(
            domain={"O": 0, "C": 0, "E": 0, "A": 0, "N": 0},
            norm=Norm(sex="M", age=40, nquestion=300),
        )

        assert isinstance(normc, dict), "normc must be a dict"

        self.assertEqual(round(normc.get("O"), 2), -32.11)
        self.assertEqual(round(normc.get("C"), 2), -19.9)
        self.assertEqual(round(normc.get("E"), 2), -10.44)
        self.assertEqual(round(normc.get("A"), 2), -24.29)
        self.assertEqual(round(normc.get("N"), 2), 8.19)

        normc = Norm.calc(
            domain={"O": 99, "C": 99, "E": 99, "A": 99, "N": 99},
            norm=Norm(sex="M", age=40, nquestion=300),
        )

        self.assertGreaterEqual(normc.get("O"), 5)
        self.assertGreaterEqual(normc.get("C"), 12)
        self.assertGreaterEqual(normc.get("E"), 20)
        self.assertGreaterEqual(normc.get("A"), 11)
        self.assertGreaterEqual(normc.get("N"), 33)

        normc = Norm.calc(
            domain={"O": 150, "C": 150, "E": 150, "A": 150, "N": 150},
            norm=Norm(sex="F", age=25, nquestion=300),
        )

        self.assertGreaterEqual(normc.get("O"), 21)
        self.assertGreaterEqual(normc.get("C"), 26)
        self.assertGreaterEqual(normc.get("E"), 35)
        self.assertGreaterEqual(normc.get("A"), 23)
        self.assertGreaterEqual(normc.get("N"), 43)

        a = Norm.calc(
            domain={"N": 61, "A": 87, "C": 102, "E": 66, "O": 78},
            norm=Norm(sex="M", age=40, nquestion=300),
        )

        b = Norm.calc(
            domain={"O": 78, "C": 102, "E": 66, "A": 87, "N": 61},
            norm=Norm(sex="M", age=40, nquestion=300),
        )

        self.assertEqual(a, b)
        self.assertEqual(round(a.get("O"), 2), -2.78)
        self.assertEqual(round(b.get("C"), 2), 13.21)
        self.assertEqual(round(a.get("E"), 2), 10.25)
        self.assertEqual(round(b.get("A"), 2), 7.58)
        self.assertEqual(round(a.get("N"), 2), 23.95)

    def test_percent_120(self):
        normc = Norm.calc(
            domain={"N": 61, "A": 87, "C": 102, "E": 66, "O": 78},
            norm=Norm(sex="M", age=40, nquestion=120),
        )

        assert isinstance(normc, dict), "normc must be a dict"

        self.assertEqual(round(normc.get("O"), 2), 43.27)
        self.assertEqual(round(normc.get("C"), 2), 61.56)
        self.assertEqual(round(normc.get("E"), 2), 41.52)
        self.assertEqual(round(normc.get("A"), 2), 52.12)
        self.assertEqual(round(normc.get("N"), 2), 46.38)

        percent = Norm.percent(normc=normc)

        assert isinstance(percent, dict), "percent must be a dict"

        self.assertEqual(round(percent.get("O"), 2), 26.88)
        self.assertEqual(round(percent.get("C"), 2), 86.97)
        self.assertEqual(round(percent.get("E"), 2), 21.47)
        self.assertEqual(round(percent.get("A"), 2), 57.53)
        self.assertEqual(round(percent.get("N"), 2), 37.24)

        normc = Norm.calc(
            domain={"N": 61, "A": 87, "C": 102, "E": 66, "O": 78},
            norm=Norm(sex="F", age=40, nquestion=120),
        )

        percent = Norm.percent(normc=normc)

        self.assertEqual(round(percent.get("O"), 2), 21.6)
        self.assertEqual(round(percent.get("C"), 2), 83.98)
        self.assertEqual(round(percent.get("E"), 2), 16.86)
        self.assertEqual(round(percent.get("A"), 2), 34.88)
        self.assertEqual(round(percent.get("N"), 2), 26.35)

        percent = Norm.percent(normc={"O": 0, "C": 0, "E": 0, "A": 0, "N": 0})

        self.assertGreaterEqual(percent.get("O"), 210)
        self.assertGreaterEqual(percent.get("C"), 210)
        self.assertGreaterEqual(percent.get("E"), 210)
        self.assertGreaterEqual(percent.get("A"), 210)
        self.assertGreaterEqual(percent.get("N"), 210)

        percent = Norm.percent(normc={"O": 1, "C": 1, "E": 1, "A": 1, "N": 1})

        self.assertGreaterEqual(percent.get("O"), 194)
        self.assertGreaterEqual(percent.get("C"), 194)
        self.assertGreaterEqual(percent.get("E"), 194)
        self.assertGreaterEqual(percent.get("A"), 194)
        self.assertGreaterEqual(percent.get("N"), 194)

        percent = Norm.percent(
            normc={"O": 99.99, "C": 99.99, "E": 99.99, "A": 99.99, "N": 99.99}
        )

        self.assertLessEqual(percent.get("O"), -110)
        self.assertLessEqual(percent.get("C"), 8647)
        self.assertLessEqual(percent.get("E"), -110)
        self.assertLessEqual(percent.get("A"), -110)
        self.assertLessEqual(percent.get("N"), 210)

    def test_percent_300(self):
        normc = Norm.calc(
            domain={"N": 61, "A": 87, "C": 102, "E": 66, "O": 78},
            norm=Norm(sex="M", age=40, nquestion=300),
        )

        assert isinstance(normc, dict), "normc must be a dict"

        self.assertEqual(round(normc.get("O"), 2), -2.78)
        self.assertEqual(round(normc.get("C"), 2), 13.21)
        self.assertEqual(round(normc.get("E"), 2), 10.25)
        self.assertEqual(round(normc.get("A"), 2), 7.58)
        self.assertEqual(round(normc.get("N"), 2), 23.95)

        percent = Norm.percent(normc=normc)

        assert isinstance(percent, dict), "percent must be a dict"

        self.assertEqual(round(percent.get("O"), 2), 260.1)
        self.assertEqual(round(percent.get("C"), 2), 53.8)
        self.assertEqual(round(percent.get("E"), 2), 78.5)
        self.assertEqual(round(percent.get("A"), 2), 105.58)
        self.assertEqual(round(percent.get("N"), 2), 5.12)

        normc = Norm.calc(
            domain={"N": 61, "A": 87, "C": 102, "E": 66, "O": 78},
            norm=Norm(sex="F", age=40, nquestion=300),
        )

        percent = Norm.percent(normc=normc)

        self.assertEqual(round(percent.get("O"), 2), 311.62)
        self.assertEqual(round(percent.get("C"), 2), 79.27)
        self.assertEqual(round(percent.get("E"), 2), 91.34)
        self.assertEqual(round(percent.get("A"), 2), 236.4)
        self.assertEqual(round(percent.get("N"), 2), 17.44)

    def test_normalize_120(self):
        normc = Norm.calc(
            domain={"N": 61, "A": 87, "C": 102, "E": 66, "O": 78},
            norm=Norm(sex="M", age=40, nquestion=120),
        )

        assert isinstance(normc, dict), "normc must be a dict"

        percent = Norm.percent(normc=normc)

        assert isinstance(percent, dict), "percent must be a dict"

        normalize = Norm.normalize(normc=normc, percent=percent)

        assert isinstance(normalize, dict), "normalize must be a dict"

        self.assertEqual(percent, normalize)
        self.assertEqual(round(percent.get("O"), 2), 26.88)
        self.assertEqual(round(normalize.get("C"), 2), 86.97)
        self.assertEqual(round(percent.get("E"), 2), 21.47)
        self.assertEqual(round(normalize.get("A"), 2), 57.53)
        self.assertEqual(round(percent.get("N"), 2), 37.24)

    def test_normalize_300(self):
        normc = Norm.calc(
            domain={"N": 61, "A": 87, "C": 102, "E": 66, "O": 78},
            norm=Norm(sex="M", age=40, nquestion=300),
        )

        assert isinstance(normc, dict), "normc must be a dict"

        percent = Norm.percent(normc=normc)

        assert isinstance(percent, dict), "percent must be a dict"

        normalize = Norm.normalize(normc=normc, percent=percent)

        assert isinstance(normalize, dict), "normalize must be a dict"

        self.assertEqual(round(percent.get("O"), 2), 260.1)
        self.assertEqual(round(normalize.get("C"), 2), 1)
        self.assertEqual(round(percent.get("E"), 2), 78.5)
        self.assertEqual(round(normalize.get("A"), 2), 1)
        self.assertEqual(round(percent.get("N"), 2), 5.12)
