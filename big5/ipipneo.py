"""It does the calculations to generate the IPIP-NEO results based on the questions and answers."""

__author__ = "Ederson Corbari, Neural-7"
__email__ = "e@neural7.io"
__status__ = "planning"

import uuid

from big5.facet import Facet
from big5.model import QuestionNumber
from big5.norm import Norm
from big5.utility import data_input_is_valid


class IpipNeo(Facet):
    """Class that calculates IPIP-NEO answers."""

    def __init__(self, question: int) -> None | BaseException:
        """
        Initialize the class.

        Args:
            - nquestion: Question type.
        """
        if question == 120:
            nquestion = QuestionNumber.IPIP_120
        elif question == 120:
            nquestion = QuestionNumber.IPIP_300
        else:
            raise BaseException(f"Type question {question} is invalid!")

        super().__init__(nquestion=nquestion)
        self._nquestion = nquestion

    def compute(self, sex: str, age: int, answers: list) -> dict:
        """Desc."""
        if not data_input_is_valid(sex=sex, age=age, answers=answers):
            return {}

        score = self.score(answers=answers)
        print("1", score)

        b5 = self.b5create(score=score)
        print("2", b5)

        domain = self.domain(score=score)
        print("3", domain)

        norm = Norm(sex=sex, age=age)
        print("4", norm)

        normc = Norm.calc(domain=domain, norm=norm)
        print("5", normc)

        distrib = self.distrib(size=len(score), b5=b5, norm=norm)
        print("6", distrib)

        percent = Norm.percent(normc=normc)
        print("7", percent)

        normalize = Norm.normalize(normc=normc, percent=percent)
        print("8", normalize)

        N = self.personality(size=len(score), big5=normalize, traits=distrib, label="N")
        E = self.personality(size=len(score), big5=normalize, traits=distrib, label="E")
        O = self.personality(size=len(score), big5=normalize, traits=distrib, label="O")
        A = self.personality(size=len(score), big5=normalize, traits=distrib, label="A")
        C = self.personality(size=len(score), big5=normalize, traits=distrib, label="C")

        data = {
            "id": str(uuid.uuid4()),
            "theory": "Big 5 Personality Traits",
            "model": "IPIP-NEO",
            "question": 120,
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

        import json

        print(json.dumps(data, indent=4, sort_keys=False))

        return data or {}
