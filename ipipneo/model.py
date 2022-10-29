"""Auxiliary constants that are used in the library."""

__author__ = "Ederson Corbari"
__email__ = "e@neural7.io"
__copyright__ = "Copyright Neural7 2022, Big 5 Personality Traits"
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "production"

from enum import Enum, IntEnum


class QuestionNumber(IntEnum):
    """Questionnaire types."""

    IPIP_300 = 300
    IPIP_120 = 120


class FacetScale(IntEnum):
    """Facet scale."""

    IPIP_MAX = 30
    IPIP_300 = 10
    IPIP_120 = 4


class FacetLevel(IntEnum):
    """Score level of a facet."""

    HIGH = 55
    LOW = 45


class NormScale(IntEnum):
    """Norms of the maximum and minimum facet."""

    CONST_MAX = 73
    CONST_MIN = 32


class NormCubic(float, Enum):
    """Perceptile cubic approximation of facets."""

    CONST1 = 210.335958661391
    CONST2 = 16.7379362643389
    CONST3 = 0.405936512733332
    CONST4 = 0.00270624341822222


class Big5Neuroticism(str, Enum):
    """Composition of the big5 facets: Neuroticism."""

    TRAIT1 = "Anxiety"
    TRAIT2 = "Anger"
    TRAIT3 = "Depression"
    TRAIT4 = "Self-Consciousness"
    TRAIT5 = "Immoderation"
    TRAIT6 = "Vulnerability"


class Big5Extraversion(str, Enum):
    """Composition of the big5 facets: Extraversion."""

    TRAIT1 = "Friendliness"
    TRAIT2 = "Gregariousness"
    TRAIT3 = "Assertiveness"
    TRAIT4 = "Activity-Level"
    TRAIT5 = "Excitement-Seeking"
    TRAIT6 = "Cheerfulness"


class Big5Openness(str, Enum):
    """Composition of the big5 facets: Openness."""

    TRAIT1 = "Imagination"
    TRAIT2 = "Artistic-Interests"
    TRAIT3 = "Emotionality"
    TRAIT4 = "Adventurousness"
    TRAIT5 = "Intellect"
    TRAIT6 = "Liberalism"


class Big5Agreeableness(str, Enum):
    """Composition of the big5 facets: Agreeableness."""

    TRAIT1 = "Trust"
    TRAIT2 = "Morality"
    TRAIT3 = "Altruism"
    TRAIT4 = "Cooperation"
    TRAIT5 = "Modesty"
    TRAIT6 = "Sympathy"


class Big5Conscientiousness(str, Enum):
    """Composition of the big5 facets: Conscientiousness."""

    TRAIT1 = "Self-Efficacy"
    TRAIT2 = "Orderliness"
    TRAIT3 = "Dutifulness"
    TRAIT4 = "Achievement-Striving"
    TRAIT5 = "Self-Discipline"
    TRAIT6 = "Cautiousness"
