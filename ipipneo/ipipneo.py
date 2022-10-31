"""It does the calculations to generate the IPIP-NEO results based on the questions and answers."""

__author__ = "Ederson Corbari"
__email__ = "e@neural7.io"
__copyright__ = "Copyright Neural7 2022, Big 5 Personality Traits"
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "production"

import uuid

from ipipneo.facet import Facet
from ipipneo.model import QuestionNumber
from ipipneo.norm import Norm
from ipipneo.utility import (organize_list_json, raise_if_age_is_invalid,
                             raise_if_sex_is_invalid)


class IpipNeo(Facet):
    """Class that calculates IPIP-NEO answers."""

    def __init__(self, question: int) -> None or BaseException:
        """
        Initialize the class.

        Args:
            - nquestion: Question type.
        """
        if question == 120:
            nquestion = QuestionNumber.IPIP_120
        elif question == 300:
            nquestion = QuestionNumber.IPIP_300
        else:
            raise BaseException(f"Type question {question} is invalid!")

        super().__init__(nquestion=nquestion)
        self._nquestion = question

    def compute(self, sex: str, age: int, answers: dict) -> dict:
        """
        Compute the answers and generate the dictionary with the results.

        Args:
            - sex: Gender of the individual (M or F).
            - age: The age of the individual.
            - answers: Standardized dictionary with answers.
        """
        raise_if_sex_is_invalid(sex=sex)
        raise_if_age_is_invalid(age=age)

        score = self.score(answers=organize_list_json(answers=answers))
        assert isinstance(score, list), "score must be a list"

        norm = Norm(sex=sex, age=age)
        assert isinstance(norm, dict), "norm must be a dict"

        normc = Norm.calc(domain=self.domain(score=score), norm=norm)
        assert isinstance(normc, dict), "normc must be a dict"

        distrib = self.distrib(
            size=len(score), b5=self.b5create(score=score), norm=norm
        )
        assert isinstance(distrib, dict), "distrib must be a dict"

        normalize = Norm.normalize(normc=normc, percent=Norm.percent(normc=normc))
        assert isinstance(normalize, dict), "normalize must be a dict"

        N = self.personality(size=len(score), big5=normalize, traits=distrib, label="N")
        E = self.personality(size=len(score), big5=normalize, traits=distrib, label="E")
        O = self.personality(size=len(score), big5=normalize, traits=distrib, label="O")
        A = self.personality(size=len(score), big5=normalize, traits=distrib, label="A")
        C = self.personality(size=len(score), big5=normalize, traits=distrib, label="C")

        assert isinstance(O, dict), "O must be a dict"
        assert isinstance(C, dict), "C must be a dict"
        assert isinstance(E, dict), "E must be a dict"
        assert isinstance(A, dict), "A must be a dict"
        assert isinstance(N, dict), "N must be a dict"

        return {
            "id": str(uuid.uuid4()),
            "theory": "Big 5 Personality Traits",
            "model": "IPIP-NEO",
            "question": self._nquestion,
            "person": {
                "sex": sex,
                "age": age,
                "result": {
                    "personalities": [
                        {"Openness": O},
                        {"Conscientiousness": C},
                        {"Extraversion": E},
                        {"Agreeableness": A},
                        {"Neuroticism": N},
                    ]
                },
            },
        }
