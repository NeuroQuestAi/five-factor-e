"""ADD desc here..."""

from enum import IntEnum

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


class Facet:
    """Class with facet information."""

    def __init__(self, nquestion: IntEnum) -> None | BaseException:
        """
        Initialize the class.

        Args:
            - nquestion: Enum with question type.
        """
        self._scale = 0

        match nquestion:
            case 300:
                self._scale = FacetScale.IPIP_300.value
            case 120:
                self._scale = FacetScale.IPIP_120.value
            case _:
                raise BaseException(
                    f"The available questions are: {list(QuestionNumber)}"
                )

    def score(self, answers: list) -> list | BaseException:
        """
        Score facet scales are created.

        Args:
            - answers: The list with the answers.
        """
        ss = [0] * len(answers)

        try:
            for j in range(FacetScale.IPIP_MAX.value):
                for i in range(self._scale):
                    ss[1 + j] += answers[1 + i * FacetScale.IPIP_MAX.value + j]
        except IndexError as e:
            raise BaseException(f'The number of questions setting is wrong: {str(e)}')

        return ss


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

    def compute(self, answers: list):
        self.check(answers=answers)

        # Add zero in first position.
        answers.insert(0, 0)

        score = self.score(answers=answers)
        print(score)
