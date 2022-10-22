"""It does the calculations to generate the IPIP-NEO results based on the questions and answers."""

from enum import Enum, IntEnum

from big5.utility import assert_ipip_neo_answers

__author__ = "Ederson Corbari, Neural-7"
__email__ = "e@neural7.io"
__status__ = "planning"


class QuestionNumber(IntEnum):
    """Questionnaire types."""

    IPIP_300 = 300
    IPIP_120 = 120


class FacetScale(IntEnum):
    """Facet scale."""

    IPIP_MAX = 30
    IPIP_300 = 10
    IPIP_120 = 4


class NormCubic(float, Enum):
    """Cubic approximation of percentiles."""

    CONST1 = 210.335958661391
    CONST2 = 16.7379362643389
    CONST3 = 0.405936512733332
    CONST4 = 0.00270624341822222


class Norm:
    """Norms-120 item version."""

    def __new__(self, sex: str, age: int) -> dict:
        """
        Based on sex and age returns range with norms.

        Args:
            - sex: Gender of the individual (male or female).
            - age: The age of the individual.
        """
        if sex == 'male' and age < 21:
            return {
                'id': 1,
                'ns': [
                    0,
                    67.84,
                    80.70,
                    85.98,
                    81.98,
                    79.66,
                    15.83,
                    15.37,
                    12.37,
                    14.66,
                    14.49,
                    11.72,
                    11.93,
                    10.58,
                    12.38,
                    11.67,
                    9.63,
                    3.76,
                    4.41,
                    4.25,
                    3.83,
                    3.25,
                    3.38,
                    13.76,
                    12.23,
                    14.06,
                    11.54,
                    14.67,
                    14.41,
                    3.78,
                    4.17,
                    3.66,
                    3.15,
                    3.38,
                    3.68,
                    16.68,
                    14.51,
                    14.52,
                    12.84,
                    15.47,
                    11.86,
                    2.96,
                    3.87,
                    3.31,
                    3.16,
                    3.50,
                    3.17,
                    13.18,
                    14.85,
                    15.37,
                    12.73,
                    12.01,
                    13.96,
                    3.69,
                    3.44,
                    3.10,
                    4.05,
                    3.94,
                    3.35,
                    15.31,
                    10.97,
                    15.22,
                    13.61,
                    12.35,
                    12.08,
                    2.55,
                    3.93,
                    2.92,
                    3.65,
                    3.24,
                    4.02,
                ],
                'category': 'men under 21 years old',
            }

        if sex == 'male' and age > 20 and age < 41:
            return {
                'id': 2,
                'ns': [
                    0,
                    66.97,
                    78.90,
                    86.51,
                    84.22,
                    85.50,
                    16.48,
                    15.21,
                    12.65,
                    13.10,
                    14.27,
                    11.44,
                    11.75,
                    10.37,
                    12.11,
                    12.18,
                    9.13,
                    3.76,
                    4.30,
                    4.12,
                    3.81,
                    3.52,
                    3.48,
                    13.31,
                    11.34,
                    14.58,
                    12.07,
                    13.34,
                    14.30,
                    3.80,
                    3.99,
                    3.58,
                    3.23,
                    3.43,
                    3.53,
                    15.94,
                    14.94,
                    14.60,
                    13.14,
                    16.11,
                    11.66,
                    3.18,
                    3.63,
                    3.19,
                    3.39,
                    3.25,
                    3.72,
                    12.81,
                    15.93,
                    15.37,
                    14.58,
                    11.43,
                    13.77,
                    3.69,
                    3.18,
                    2.92,
                    3.70,
                    3.57,
                    3.29,
                    15.80,
                    12.05,
                    15.68,
                    15.36,
                    13.27,
                    13.31,
                    2.44,
                    4.26,
                    2.76,
                    3.39,
                    3.31,
                    4.03,
                ],
                'category': 'men between 21 and 40 years old',
            }

        if sex == 'male' and age > 40 and age < 61:
            return {
                'id': 3,
                'ns': [
                    0,
                    64.11,
                    77.06,
                    83.04,
                    88.33,
                    91.27,
                    16.04,
                    14.31,
                    13.05,
                    11.76,
                    13.35,
                    10.79,
                    11.60,
                    9.78,
                    11.85,
                    11.24,
                    8.81,
                    3.56,
                    4.16,
                    3.94,
                    3.62,
                    3.55,
                    3.35,
                    13.22,
                    10.45,
                    14.95,
                    12.27,
                    11.82,
                    14.32,
                    3.71,
                    3.68,
                    3.44,
                    3.30,
                    3.23,
                    3.29,
                    14.65,
                    14.66,
                    14.76,
                    12.69,
                    15.40,
                    11.04,
                    3.35,
                    3.59,
                    3.02,
                    3.44,
                    3.43,
                    3.93,
                    13.42,
                    16.94,
                    15.65,
                    15.66,
                    11.96,
                    14.21,
                    3.49,
                    2.83,
                    2.88,
                    3.33,
                    3.34,
                    3.17,
                    16.19,
                    13.33,
                    16.56,
                    16.51,
                    14.05,
                    14.60,
                    2.25,
                    4.32,
                    2.50,
                    2.93,
                    3.13,
                    3.78,
                ],
                'category': 'men between 41 and 60 years of age',
            }

        if sex == 'male' and age > 60:
            return {
                'id': 4,
                'ns': [
                    0,
                    58.42,
                    79.73,
                    79.78,
                    90.20,
                    95.31,
                    15.48,
                    13.63,
                    12.21,
                    11.73,
                    11.99,
                    9.81,
                    11.46,
                    8.18,
                    11.08,
                    9.91,
                    8.24,
                    3.54,
                    4.31,
                    3.59,
                    3.82,
                    3.36,
                    3.28,
                    14.55,
                    11.19,
                    15.29,
                    12.81,
                    11.03,
                    15.02,
                    3.47,
                    3.58,
                    3.10,
                    3.25,
                    2.88,
                    3.16,
                    14.06,
                    14.22,
                    14.34,
                    12.42,
                    14.61,
                    10.11,
                    3.13,
                    3.64,
                    2.90,
                    3.20,
                    3.89,
                    4.02,
                    13.96,
                    17.74,
                    15.76,
                    16.18,
                    11.87,
                    14.00,
                    3.13,
                    2.39,
                    2.74,
                    3.41,
                    3.50,
                    3.11,
                    16.32,
                    14.41,
                    17.54,
                    16.65,
                    14.98,
                    15.18,
                    2.31,
                    4.49,
                    2.30,
                    2.68,
                    2.76,
                    3.61,
                ],
                'category': 'men between 41 and 60 years old',
            }

        if sex == 'female' and age < 21:
            return {
                'id': 5,
                'ns': [
                    0,
                    73.41,
                    84.26,
                    89.01,
                    89.14,
                    81.27,
                    15.61,
                    14.98,
                    11.84,
                    13.21,
                    14.38,
                    13.31,
                    13.09,
                    11.05,
                    12.11,
                    12.48,
                    11.30,
                    3.62,
                    4.18,
                    4.20,
                    3.82,
                    3.30,
                    3.47,
                    14.47,
                    13.12,
                    14.03,
                    12.67,
                    14.69,
                    15.34,
                    3.60,
                    4.13,
                    3.68,
                    3.09,
                    3.48,
                    3.42,
                    16.86,
                    15.93,
                    16.02,
                    12.95,
                    15.06,
                    12.17,
                    2.89,
                    3.44,
                    2.95,
                    3.24,
                    3.51,
                    3.02,
                    13.46,
                    16.11,
                    16.66,
                    13.73,
                    13.23,
                    15.70,
                    3.72,
                    2.94,
                    2.69,
                    4.14,
                    3.79,
                    2.84,
                    15.30,
                    11.11,
                    15.62,
                    14.69,
                    12.73,
                    11.82,
                    2.54,
                    4.17,
                    2.76,
                    3.37,
                    3.19,
                    4.01,
                ],
                'category': 'women under 21 years old',
            }

        if sex == 'female' and age > 20 and age < 41:
            return {
                'id': 6,
                'ns': [
                    0,
                    72.14,
                    80.78,
                    88.25,
                    91.91,
                    87.57,
                    16.16,
                    14.64,
                    12.15,
                    11.39,
                    13.87,
                    13.08,
                    12.72,
                    10.79,
                    12.20,
                    12.71,
                    10.69,
                    3.68,
                    4.13,
                    4.07,
                    3.79,
                    3.58,
                    3.64,
                    14.05,
                    11.92,
                    14.25,
                    12.77,
                    12.84,
                    14.96,
                    3.66,
                    4.05,
                    3.61,
                    3.24,
                    3.53,
                    3.31,
                    15.64,
                    15.97,
                    16.41,
                    12.84,
                    15.28,
                    12.06,
                    3.34,
                    3.30,
                    2.69,
                    3.44,
                    3.47,
                    3.46,
                    13.15,
                    17.34,
                    16.81,
                    15.57,
                    12.98,
                    15.52,
                    3.71,
                    2.61,
                    2.53,
                    3.50,
                    3.57,
                    2.87,
                    16.02,
                    12.67,
                    16.36,
                    16.11,
                    13.56,
                    12.91,
                    2.34,
                    4.51,
                    2.54,
                    3.05,
                    3.23,
                    4.18,
                ],
                'category': 'women between 21 and 40 years old',
            }

        if sex == 'female' and age > 40 and age < 61:
            return {
                'id': 7,
                'ns': [
                    0,
                    67.38,
                    78.62,
                    86.15,
                    95.73,
                    93.45,
                    16.10,
                    14.19,
                    12.62,
                    9.84,
                    12.94,
                    12.05,
                    11.19,
                    10.07,
                    12.07,
                    11.98,
                    10.07,
                    3.72,
                    4.03,
                    3.97,
                    3.73,
                    3.69,
                    3.56,
                    14.10,
                    10.84,
                    14.51,
                    13.03,
                    11.08,
                    15.00,
                    3.72,
                    3.86,
                    3.50,
                    3.46,
                    3.42,
                    3.26,
                    14.43,
                    16.00,
                    16.37,
                    12.58,
                    14.87,
                    11.85,
                    3.49,
                    3.20,
                    2.58,
                    3.45,
                    3.65,
                    3.74,
                    13.79,
                    18.16,
                    17.04,
                    17.02,
                    13.41,
                    15.82,
                    3.52,
                    2.21,
                    2.40,
                    2.88,
                    3.30,
                    2.71,
                    16.50,
                    13.68,
                    17.29,
                    17.16,
                    14.35,
                    14.41,
                    2.16,
                    4.51,
                    2.27,
                    2.73,
                    3.13,
                    3.86,
                ],
                'category': 'women between 41 and 61 years old',
            }

        if sex == 'female' and age > 60:
            return {
                'id': 8,
                'ns': [
                    0,
                    63.48,
                    78.22,
                    81.56,
                    97.17,
                    96.44,
                    14.92,
                    12.73,
                    12.66,
                    9.52,
                    12.43,
                    11.39,
                    10.52,
                    9.10,
                    12.00,
                    10.21,
                    9.87,
                    3.61,
                    3.82,
                    3.68,
                    3.61,
                    3.58,
                    3.44,
                    14.85,
                    10.93,
                    14.19,
                    12.76,
                    10.08,
                    15.65,
                    3.43,
                    3.70,
                    3.64,
                    3.26,
                    3.20,
                    3.04,
                    13.15,
                    15.95,
                    15.73,
                    11.80,
                    14.21,
                    10.81,
                    3.71,
                    3.12,
                    2.74,
                    3.26,
                    3.47,
                    3.89,
                    14.19,
                    18.64,
                    17.13,
                    17.98,
                    13.58,
                    15.83,
                    3.39,
                    1.90,
                    2.18,
                    2.56,
                    3.38,
                    2.85,
                    16.50,
                    15.15,
                    18.34,
                    17.19,
                    14.70,
                    15.11,
                    2.24,
                    4.07,
                    1.81,
                    2.49,
                    3.15,
                    3.66,
                ],
                'category': 'women over 60 years old',
            }

    @staticmethod
    def calc(domain: dict, norm: dict) -> dict:
        """Add comments."""
        N = (10 * (domain.get('N', 0) - norm.get('ns')[1]) / norm.get('ns')[6]) + 50
        E = (10 * (domain.get('E', 0) - norm.get('ns')[2]) / norm.get('ns')[7]) + 50
        O = (10 * (domain.get('O', 0) - norm.get('ns')[3]) / norm.get('ns')[8]) + 50
        A = (10 * (domain.get('A', 0) - norm.get('ns')[4]) / norm.get('ns')[9]) + 50
        C = (10 * (domain.get('C', 0) - norm.get('ns')[5]) / norm.get('ns')[10]) + 50
        return {'O': O, 'C': C, 'E': E, 'A': A, 'N': N}

    @staticmethod
    def percent(normc: dict) -> dict:
        """Add comments."""
        N = int(
            NormCubic.CONST1.value
            - (NormCubic.CONST2.value * normc.get('N', 0))
            + (NormCubic.CONST3.value * normc.get('N', 0) ** 2)
            - (NormCubic.CONST4.value * normc.get('N', 0) ** 3)
        )
        E = int(
            NormCubic.CONST1.value
            - (NormCubic.CONST2.value * normc.get('E', 0))
            + (NormCubic.CONST3.value * normc.get('E', 0) ** 2)
            - (NormCubic.CONST4.value * normc.get('E', 0) ** 3)
        )
        O = int(
            NormCubic.CONST1.value
            - (NormCubic.CONST2.value * normc.get('O', 0))
            + (NormCubic.CONST3.value * normc.get('O', 0) ** 2)
            - (NormCubic.CONST4.value * normc.get('O', 0) ** 3)
        )
        A = int(
            NormCubic.CONST1.value
            - (NormCubic.CONST2.value * normc.get('A', 0))
            + (NormCubic.CONST3.value * normc.get('A', 0) ** 2)
            - (NormCubic.CONST4.value * normc.get('A', 0) ** 3)
        )
        C = int(
            NormCubic.CONST1.value
            - (NormCubic.CONST2.value * normc.get('C', 0))
            + (NormCubic.CONST3.value * normc.get('C', 0) ** 2)
            - (NormCubic.CONST4.value * normc.get('C', 0) ** 3)
        )
        return {'O': O, 'C': C, 'E': E, 'A': A, 'N': N}

    @staticmethod
    def normalize(normc: dict, percent: dict) -> dict:
        """Add comments."""

        N = 1 if normc.get('N', 0) < 32 else percent.get('N', 0)
        E = 1 if normc.get('E', 0) < 32 else percent.get('E', 0)
        O = 1 if normc.get('O', 0) < 32 else percent.get('O', 0)
        A = 1 if normc.get('A', 0) < 32 else percent.get('A', 0)
        C = 1 if normc.get('C', 0) < 32 else percent.get('C', 0)

        N = 99 if normc.get('N', 0) > 73 else percent.get('N', 0)
        E = 99 if normc.get('E', 0) > 73 else percent.get('E', 0)
        O = 99 if normc.get('O', 0) > 73 else percent.get('O', 0)
        A = 99 if normc.get('A', 0) > 73 else percent.get('A', 0)
        C = 99 if normc.get('C', 0) > 73 else percent.get('C', 0)

        return {'O': O, 'C': C, 'E': E, 'A': A, 'N': N}


class Facet:
    """Class with facet information."""

    def __init__(self, nquestion: IntEnum) -> None | BaseException:
        """
        Initialize the class.

        Args:
            - nquestion: Enum with question type.
        """
        if nquestion == 300:
            self._scale = FacetScale.IPIP_300.value
        elif nquestion == 120:
            self._scale = FacetScale.IPIP_120.value
        else:
            raise BaseException(f'The available questions are: {list(QuestionNumber)}')

    def score(self, answers: list) -> list | BaseException:
        """
        Score facet scales are created.

        Args:
            - answers: The list with the answers.
        """
        answers.insert(0, 0)
        ss = [0] * len(answers)
        try:
            for j in range(FacetScale.IPIP_MAX.value):
                for i in range(self._scale):
                    ss[1 + j] += answers[1 + i * FacetScale.IPIP_MAX.value + j]
        except IndexError as e:
            raise BaseException(f'The number of questions setting is wrong: {str(e)}')

        return ss

    def b5create(self, score: list) -> dict:
        """
        Numbers each facet set from 1 to 6 to create the Big-Five (OCEAN).

        Args:
            - score: The facet score result.
        """
        ss, j = score, 0

        N = [0] * len(ss)
        E = [0] * len(ss)
        O = [0] * len(ss)
        A = [0] * len(ss)
        C = [0] * len(ss)

        for i in range(1, 7):
            N[i] = ss[i + j]
            E[i] = ss[i + j + 1]
            O[i] = ss[i + j + 2]
            A[i] = ss[i + j + 3]
            C[i] = ss[i + j + 4]
            j = j + 4

        return {'O': O, 'C': C, 'E': E, 'A': A, 'N': N}

    def domain(self, score: list) -> dict:
        """
        Create the Big-Five (OCEAN) domain score.

        Args:
            - score: The facet score result.
        """
        N = score[1] + score[6] + score[11] + score[16] + score[21] + score[26]
        E = score[2] + score[7] + score[12] + score[17] + score[22] + score[27]
        O = score[3] + score[8] + score[13] + score[18] + score[23] + score[28]
        A = score[4] + score[9] + score[14] + score[19] + score[24] + score[29]
        C = score[5] + score[10] + score[15] + score[20] + score[25] + score[30]

        return {'O': O, 'C': C, 'E': E, 'A': A, 'N': N}

    def distrib(self, size: int, b5: dict, norm: dict) -> list:
        """Distrib."""
        N = [0] * size
        E = [0] * size
        O = [0] * size
        A = [0] * size
        C = [0] * size

        for i in range(1, 7):
            N[i] = 50 + (
                10 * (b5.get('N')[i] - norm.get('ns')[i + 10]) / norm.get('ns')[i + 16]
            )
            E[i] = 50 + (
                10 * (b5.get('E')[i] - norm.get('ns')[i + 22]) / norm.get('ns')[i + 28]
            )
            O[i] = 50 + (
                10 * (b5.get('O')[i] - norm.get('ns')[i + 34]) / norm.get('ns')[i + 40]
            )
            A[i] = 50 + (
                10 * (b5.get('A')[i] - norm.get('ns')[i + 46]) / norm.get('ns')[i + 52]
            )
            C[i] = 50 + (
                10 * (b5.get('C')[i] - norm.get('ns')[i + 58]) / norm.get('ns')[i + 64]
            )

        return {'O': O, 'C': C, 'E': E, 'A': A, 'N': N}


class IpipNeo(Facet):
    """Class that calculates IPIP-NEO answers."""

    def __init__(self, nquestion: IntEnum) -> None | BaseException:
        """
        Initialize the class.

        Args:
            - nquestion: Enum with question type.
        """
        super().__init__(nquestion=nquestion)
        self._nquestion = nquestion

    def compute(self, sex: str, age: int, answers: list):
        """Desc."""
        assert_ipip_neo_answers(answers=answers, nquestion=self._nquestion)

        score = self.score(answers=answers)
        print('1', score)

        b5 = self.b5create(score=score)
        print('2', b5)

        domain = self.domain(score=score)
        print('3', domain)

        norm = Norm(sex=sex, age=age)
        print('4', norm)

        normc = Norm.calc(domain=domain, norm=norm)
        print('5', normc)

        distrib = self.distrib(size=len(score), b5=b5, norm=norm)
        print('6', distrib)

        percent = Norm.percent(normc=normc)
        print('7', percent)

        normalize = Norm.normalize(normc=normc, percent=percent)
        print('8', normalize)
