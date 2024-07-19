"""Creation and scoring of the facets that make up the Big-Five."""

__author__ = "Ederson Corbari"
__email__ = "e@NeuroQuest.ai"
__copyright__ = "Copyright NeuroQuest 2022-2024, Big 5 Personality Traits"
__credits__ = ["John A. Johnson", "Dhiru Kholia"]
__license__ = "MIT"
__version__ = "1.12.0"
__status__ = "production"

from enum import IntEnum

from ipipneo.model import (FacetLevel, FacetScale, NormCubic, NormScale,
                           QuestionNumber)
from ipipneo.utility import big5_ocean_is_valid, create_big5_dict


class Facet:
    """Creating and scoring facets and Big-Five."""

    def __init__(self, nquestion: IntEnum) -> None:
        """
        Initialize the class.

        Args:
            - nquestion: Enum with question type.
        """
        scale_mapping = {
            300: FacetScale.IPIP_300.value,
            120: FacetScale.IPIP_120.value,
        }

        self._scale = scale_mapping.get(nquestion)

        if self._scale is None:
            raise ValueError(f"The available questions are: {list(QuestionNumber)}")

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
            raise BaseException(f"The number of questions setting is wrong: {str(e)}")

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

        try:
            for i in range(1, 7):
                N[i] = ss[i + j]
                E[i] = ss[i + j + 1]
                O[i] = ss[i + j + 2]
                A[i] = ss[i + j + 3]
                C[i] = ss[i + j + 4]
                j = j + 4
        except IndexError as e:
            raise BaseException(f"The number of questions setting is wrong: {str(e)}")

        return {"O": O, "C": C, "E": E, "A": A, "N": N}

    def domain(self, score: list) -> dict:
        """
        Create the Big-Five (OCEAN) domain score.

        Args:
            - score: The facet score result.
        """
        try:
            calculate_domain_score = lambda x: sum(score[i] for i in x)
            N = calculate_domain_score([1, 6, 11, 16, 21, 26])
            E = calculate_domain_score([2, 7, 12, 17, 22, 27])
            O = calculate_domain_score([3, 8, 13, 18, 23, 28])
            A = calculate_domain_score([4, 9, 14, 19, 24, 29])
            C = calculate_domain_score([5, 10, 15, 20, 25, 30])
        except IndexError as e:
            raise BaseException(f"Invalid position in the score array: {str(e)}")

        return {"O": O, "C": C, "E": E, "A": A, "N": N}

    def distrib(self, size: int, b5: dict, norm: dict) -> list:
        """
        Creation and distribution with weights.

        Args:
            - size: Vector size, must be the same as response size.
            - b5: Dictionary with composition of the Big-Five.
            - norm: Dictionary with the calculation of norms.
        """
        N = [0] * size
        E = [0] * size
        O = [0] * size
        A = [0] * size
        C = [0] * size

        try:
            for i in range(1, 7):
                N[i] = 50 + (
                    10
                    * (b5.get("N")[i] - norm.get("ns")[i + 10])
                    / norm.get("ns")[i + 16]
                )
                E[i] = 50 + (
                    10
                    * (b5.get("E")[i] - norm.get("ns")[i + 22])
                    / norm.get("ns")[i + 28]
                )
                O[i] = 50 + (
                    10
                    * (b5.get("O")[i] - norm.get("ns")[i + 34])
                    / norm.get("ns")[i + 40]
                )
                A[i] = 50 + (
                    10
                    * (b5.get("A")[i] - norm.get("ns")[i + 46])
                    / norm.get("ns")[i + 52]
                )
                C[i] = 50 + (
                    10
                    * (b5.get("C")[i] - norm.get("ns")[i + 58])
                    / norm.get("ns")[i + 64]
                )
        except IndexError as e:
            raise BaseException(f"The number of questions setting is wrong: {str(e)}")

        return {"O": O, "C": C, "E": E, "A": A, "N": N}

    def personality(
        self,
        size: int,
        big5: dict,
        traits: dict,
        label: str,
        norm_scale_min: int = None,
        norm_scale_max: int = None,
        facet_score_level_low: int = None,
        facet_score_level_high: int = None,
    ) -> dict:
        """
        Calculate the personalities / facets for each Big-Five.

        Args:
            - size: Vector size, must be the same as response size.
            - big5: Dictionary of normalized Big-Five.
            - traits: Dictionary with the distribution of personalities.
            - label: Capital letter referring to the Big-Five to be calculated.
            - norm_scale_min: The minimum value of the norm scale.
            - norm_scale_max: The maximum value of the norm scale.
            - facet_score_level_low: The score level is considered low.
            - facet_score_level_high: The score level is considered high.
        """
        big5_ocean_is_valid(label=label)

        big5, traits = big5.get(label, 0), traits.get(label, [])

        norm_min_value = (
            norm_scale_min if norm_scale_min is not None else NormScale.CONST_MIN.value
        )
        norm_max_value = (
            norm_scale_max if norm_scale_max is not None else NormScale.CONST_MAX.value
        )

        facet_score_level_low_value = (
            facet_score_level_low
            if facet_score_level_low is not None
            else FacetLevel.LOW.value
        )
        facet_score_level_high_value = (
            facet_score_level_high
            if facet_score_level_high is not None
            else FacetLevel.HIGH.value
        )

        X = [0] * size
        Y = [0] * size

        try:
            for i in range(1, 7):
                Y[i] = traits[i]

                if int(traits[i]) < facet_score_level_low_value:
                    Y[i] = "low"
                elif (
                    facet_score_level_low_value
                    <= int(traits[i])
                    <= facet_score_level_high_value
                ):
                    Y[i] = "average"
                elif int(traits[i]) > facet_score_level_high_value:
                    Y[i] = "high"

                X[i] = (
                    NormCubic.CONST1.value
                    - (NormCubic.CONST2.value * traits[i])
                    + (NormCubic.CONST3.value * traits[i] ** 2)
                    - (NormCubic.CONST4.value * traits[i] ** 3)
                )

                if traits[i] < norm_min_value:
                    X[i] = 1

                if traits[i] > norm_max_value:
                    X[i] = 99
        except IndexError as e:
            raise BaseException(f"The number of questions setting is wrong: {str(e)}")

        return create_big5_dict(label=label, big5=big5, x=X, y=Y) or {}

    def big_five_level(
        self,
        big5: dict,
        label: str,
        facet_score_level_low: int = None,
        facet_score_level_high: int = None,
    ) -> dict:
        """
        Add the average for each Big-Five.

        Args:
            - big5: Dictionary of personality Big-Five.
            - label: Capital letter referring to the Big-Five to be checked the average.
            - facet_score_level_low: The score level is considered low.
            - facet_score_level_high: The score level is considered high.
        """
        big5_ocean_is_valid(label=label)

        facet_score_level_low_value = (
            facet_score_level_low
            if facet_score_level_low is not None
            else FacetLevel.LOW.value
        )
        facet_score_level_high_value = (
            facet_score_level_high
            if facet_score_level_high is not None
            else FacetLevel.HIGH.value
        )

        for trait in big5.get("traits", []):
            score_value = None
            for key, value in trait.items():
                if key not in ["trait", "score"] and isinstance(value, (int, float)):
                    score_value = value
                    break

            if score_value:
                trait["score"] = self.score_level(
                    score=score_value,
                    facet_score_level_low=facet_score_level_low_value,
                    facet_score_level_high=facet_score_level_high_value,
                )

        score = big5.get(label, 0)
        big5["score"] = self.score_level(
            score=score,
            facet_score_level_low=facet_score_level_low_value,
            facet_score_level_high=facet_score_level_high_value,
        )

        return big5

    def score_level(
        self,
        score: float,
        facet_score_level_low: int = None,
        facet_score_level_high: int = None,
    ) -> str:
        facet_score_level_low_value = (
            facet_score_level_low
            if facet_score_level_low is not None
            else FacetLevel.LOW.value
        )
        facet_score_level_high_value = (
            facet_score_level_high
            if facet_score_level_high is not None
            else FacetLevel.HIGH.value
        )
        return (
            "low"
            if int(score) < facet_score_level_low_value
            else "average"
            if facet_score_level_low_value <= int(score) <= facet_score_level_high_value
            else "high"
        )
