"""It does the calculations to generate the IPIP-NEO results based on the questions and answers."""

__author__ = "Ederson Corbari"
__email__ = "e@NeuroQuest.ai"
__copyright__ = "Copyright NeuroQuest 2022-2024, Big 5 Personality Traits"
__credits__ = ["John A. Johnson", "Dhiru Kholia"]
__license__ = "MIT"
__version__ = "1.12.0"
__status__ = "production"

import copy
import uuid

from ipipneo.facet import Facet
from ipipneo.model import FacetLevel, NormScale, QuestionNumber
from ipipneo.norm import Norm
from ipipneo.reverse import (ReverseScored120, ReverseScored300,
                             ReverseScoredCustom)
from ipipneo.utility import (add_dict_footer, organize_list_json,
                             raise_if_age_is_invalid, raise_if_sex_is_invalid)


class IpipNeo(Facet):
    """Class that calculates IPIP-NEO answers."""

    def __init__(self, question: int, test: bool = False) -> None:
        """
        Initialize the class.

        Args:
            - question: Question type, 120 or 300.
            - test: Used to test your proposed questions with reverse.
        """
        assert isinstance(question, int), "The (question) field must be an int!"
        assert isinstance(test, bool), "The (test) field must be a bool!"

        question_mapping = {
            120: QuestionNumber.IPIP_120,
            300: QuestionNumber.IPIP_300,
        }

        nquestion = question_mapping.get(question)

        if nquestion is None:
            raise ValueError(f"Type question {question} is invalid!")

        super().__init__(nquestion)
        self._nquestion: int = question
        self._test: bool = test
        self._norm_scale_min: int = None
        self._norm_scale_max: int = None
        self._score_level_low: int = None
        self._score_level_high: int = None

    def set_new_norm_scale(self, scale_min: int, scale_max: int) -> None:
        """
        Used to set a new norm scale. Used for testing only.

        The default is min=32 and max=73.

        Args:
            - scale_min: The minimum value of the norm scale.
            - scale_max: The maximum value of the norm scale.
        """
        assert isinstance(scale_min, int), "The (scale_min) field must be an int!"
        assert isinstance(scale_max, int), "The (scale_max) field must be an int!"

        self._norm_scale_min = int(scale_min)
        self._norm_scale_max = int(scale_max)

    def get_current_norm(self) -> tuple:
        """Shows the values ​​of the current level scale used."""
        if self._norm_scale_min is not None and self._norm_scale_max is not None:
            return self._norm_scale_min, self._norm_scale_max
        return NormScale.CONST_MIN.value, NormScale.CONST_MAX.value

    def set_new_facet_level(self, low_min: int, high_max: int) -> None:
        """
        Used to set a new facet level. Used for testing only.

        The default is low=45 and high=55.

        Args:
            - low_min: Value considered low.
            - high_max: Value considered high.
        """
        assert isinstance(low_min, int), "The (low_min) field must be an int!"
        assert isinstance(high_max, int), "The (high_max) field must be an int!"

        self._score_level_low = int(low_min)
        self._score_level_high = int(high_max)

    def get_current_scale_level(self) -> tuple:
        """Shows the values ​​of the current level scale used."""
        if self._score_level_low is not None and self._score_level_high is not None:
            return self._score_level_low, self._score_level_high
        return FacetLevel.LOW.value, FacetLevel.HIGH.value

    def evaluator(self, sex: str, age: int, score: list) -> dict:
        """
        Apply the calculation of the Big-Five and its personalities based on the answers.

        Args:
            - sex: Gender of the individual (M or F).
            - age: The age of the individual.
            - score: The normalized score.
        """
        norm = Norm(sex=sex, age=age, nquestion=self._nquestion)
        assert isinstance(norm, dict), "norm must be a dict"

        normc = Norm.calc(domain=self.domain(score=score), norm=norm)
        assert isinstance(normc, dict), "normc must be a dict"

        distrib = self.distrib(
            size=len(score), b5=self.b5create(score=score), norm=norm
        )
        assert isinstance(distrib, dict), "distrib must be a dict"

        normalize = Norm.normalize(
            normc=normc,
            percent=Norm.percent(normc=normc),
            norm_scale_min=self._norm_scale_min if self._norm_scale_min else None,
            norm_scale_max=self._norm_scale_max if self._norm_scale_max else None,
        )
        assert isinstance(normalize, dict), "normalize must be a dict"

        N = self.personality(
            size=len(score),
            big5=normalize,
            traits=distrib,
            label="N",
            norm_scale_min=self._norm_scale_min if self._norm_scale_min else None,
            norm_scale_max=self._norm_scale_max if self._norm_scale_max else None,
            facet_score_level_low=self._score_level_low
            if self._score_level_low
            else None,
            facet_score_level_high=self._score_level_high
            if self._score_level_high
            else None,
        )
        E = self.personality(
            size=len(score),
            big5=normalize,
            traits=distrib,
            label="E",
            norm_scale_min=self._norm_scale_min if self._norm_scale_min else None,
            norm_scale_max=self._norm_scale_max if self._norm_scale_max else None,
            facet_score_level_low=self._score_level_low
            if self._score_level_low
            else None,
            facet_score_level_high=self._score_level_high
            if self._score_level_high
            else None,
        )
        O = self.personality(
            size=len(score),
            big5=normalize,
            traits=distrib,
            label="O",
            norm_scale_min=self._norm_scale_min if self._norm_scale_min else None,
            norm_scale_max=self._norm_scale_max if self._norm_scale_max else None,
            facet_score_level_low=self._score_level_low
            if self._score_level_low
            else None,
            facet_score_level_high=self._score_level_high
            if self._score_level_high
            else None,
        )
        A = self.personality(
            size=len(score),
            big5=normalize,
            traits=distrib,
            label="A",
            norm_scale_min=self._norm_scale_min if self._norm_scale_min else None,
            norm_scale_max=self._norm_scale_max if self._norm_scale_max else None,
            facet_score_level_low=self._score_level_low
            if self._score_level_low
            else None,
            facet_score_level_high=self._score_level_high
            if self._score_level_high
            else None,
        )
        C = self.personality(
            size=len(score),
            big5=normalize,
            traits=distrib,
            label="C",
            norm_scale_min=self._norm_scale_min if self._norm_scale_min else None,
            norm_scale_max=self._norm_scale_max if self._norm_scale_max else None,
            facet_score_level_low=self._score_level_low
            if self._score_level_low
            else None,
            facet_score_level_high=self._score_level_high
            if self._score_level_high
            else None,
        )
        assert isinstance(O, dict), "O must be a dict"
        assert isinstance(C, dict), "C must be a dict"
        assert isinstance(E, dict), "E must be a dict"
        assert isinstance(A, dict), "A must be a dict"
        assert isinstance(N, dict), "N must be a dict"

        return {
            "id": str(uuid.uuid4()),
            "theory": "Big 5 Personality Traits",
            "model": "IPIP-NEO" if self._nquestion == 120 else "IPIP",
            "question": self._nquestion,
            "test": self._test,
            "person": {
                "sex": sex,
                "age": age,
                "result": {
                    "personalities": [
                        {
                            "openness": self.big_five_level(
                                big5=O,
                                label="O",
                                facet_score_level_low=self._score_level_low
                                if self._score_level_low
                                else None,
                                facet_score_level_high=self._score_level_high
                                if self._score_level_high
                                else None,
                            )
                        },
                        {
                            "conscientiousness": self.big_five_level(
                                big5=C,
                                label="C",
                                facet_score_level_low=self._score_level_low
                                if self._score_level_low
                                else None,
                                facet_score_level_high=self._score_level_high
                                if self._score_level_high
                                else None,
                            )
                        },
                        {
                            "extraversion": self.big_five_level(
                                big5=E,
                                label="E",
                                facet_score_level_low=self._score_level_low
                                if self._score_level_low
                                else None,
                                facet_score_level_high=self._score_level_high
                                if self._score_level_high
                                else None,
                            )
                        },
                        {
                            "agreeableness": self.big_five_level(
                                big5=A,
                                label="A",
                                facet_score_level_low=self._score_level_low
                                if self._score_level_low
                                else None,
                                facet_score_level_high=self._score_level_high
                                if self._score_level_high
                                else None,
                            )
                        },
                        {
                            "neuroticism": self.big_five_level(
                                big5=N,
                                label="N",
                                facet_score_level_low=self._score_level_low
                                if self._score_level_low
                                else None,
                                facet_score_level_high=self._score_level_high
                                if self._score_level_high
                                else None,
                            )
                        },
                    ]
                },
            },
            **add_dict_footer(),
        }

    def compute(self, sex: str, age: int, answers: dict, compare: bool = False) -> dict:
        """
        Compute the answers and generate the data with the results.

        Args:
            - sex: Gender of the individual (M or F).
            - age: The age of the individual.
            - answers: Standardized dictionary with answers.
            - compare: If true, it shows the user's answers and reverse score.
        """
        raise_if_sex_is_invalid(sex=sex)
        raise_if_age_is_invalid(age=age)
        assert isinstance(answers, dict), "answers must be a dict"

        original = copy.deepcopy(answers)
        assert isinstance(original, dict), "original must be a dict"

        reversed = (
            ReverseScoredCustom(answers=answers)
            if self._test
            else (
                ReverseScored120(answers=answers)
                if self._nquestion == 120
                else ReverseScored300(answers=answers)
            )
        )
        assert isinstance(reversed, dict), "reversed must be a dict"

        score = self.score(answers=organize_list_json(answers=reversed))
        assert isinstance(score, list), "score must be a list"

        result = self.evaluator(sex=sex, age=age, score=score)
        assert isinstance(result, dict), "result 1 must be a dict"

        if compare:
            result["person"]["result"]["compare"] = {
                "user_answers_original": original.get("answers", []),
                "user_answers_reversed": reversed.get("answers", []),
            }
        assert isinstance(result, dict), "result 2 must be a dict"

        return result or {}
