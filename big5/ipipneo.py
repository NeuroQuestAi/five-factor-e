"""It does the calculations to generate the IPIP-NEO results based on the questions and answers."""

__author__ = 'Ederson Corbari, Neural-7'
__email__ = 'e@neural7.io'
__status__ = 'planning'

from enum import IntEnum

from big5.facet import Facet
from big5.norm import Norm
from big5.utility import data_input_is_valid


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

    def compute(self, sex: str, age: int, answers: list) -> dict:
        """Desc."""
        if not data_input_is_valid(sex=sex, age=age, answers=answers):
            return {}

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

        N = self.personality(size=len(score), big5=normalize, traits=distrib, label='N')
        E = self.personality(size=len(score), big5=normalize, traits=distrib, label='E')
        O = self.personality(size=len(score), big5=normalize, traits=distrib, label='O')
        A = self.personality(size=len(score), big5=normalize, traits=distrib, label='A')
        C = self.personality(size=len(score), big5=normalize, traits=distrib, label='C')

        # print('\n')
        # print('9-1', N)
        # print('9-2', E)
        # print('9-3', O)
        # print('9-4', A)
        # print('9-5', C)

        data = {
            'theory': 'Big 5 Personality Traits',
            'model': 'IPIP-NEO',
            'question': 120,
            'person': {
                'sex': sex,
                'age': age,
                'result': {
                    'personalities': [
                        {'Openness': O},
                        {'Conscientiousness': C},
                        {'Extraversion': E},
                        {'Agreeableness': A},
                        {'Neuroticism': N},
                    ]
                },
            },
        }

        import json

        print(json.dumps(data, indent=4, sort_keys=False))

        return data or {}
