"""Auxiliary constants that are used in the library."""

__author__ = "Ederson Corbari"
__email__ = "e@NeuroQuest.ai"
__copyright__ = "Copyright NeuroQuest 2022-2024, Big 5 Personality Traits"
__credits__ = ["John A. Johnson", "Dhiru Kholia"]
__license__ = "MIT"
__version__ = "1.12.0"
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

    TRAIT1 = "anxiety"
    TRAIT2 = "anger"
    TRAIT3 = "depression"
    TRAIT4 = "self_consciousness"
    TRAIT5 = "immoderation"
    TRAIT6 = "vulnerability"


class Big5Extraversion(str, Enum):
    """Composition of the big5 facets: Extraversion."""

    TRAIT1 = "friendliness"
    TRAIT2 = "gregariousness"
    TRAIT3 = "assertiveness"
    TRAIT4 = "activity_level"
    TRAIT5 = "excitement_seeking"
    TRAIT6 = "cheerfulness"


class Big5Openness(str, Enum):
    """Composition of the big5 facets: Openness."""

    TRAIT1 = "imagination"
    TRAIT2 = "artistic_interests"
    TRAIT3 = "emotionality"
    TRAIT4 = "adventurousness"
    TRAIT5 = "intellect"
    TRAIT6 = "liberalism"


class Big5Agreeableness(str, Enum):
    """Composition of the big5 facets: Agreeableness."""

    TRAIT1 = "trust"
    TRAIT2 = "morality"
    TRAIT3 = "altruism"
    TRAIT4 = "cooperation"
    TRAIT5 = "modesty"
    TRAIT6 = "sympathy"


class Big5Conscientiousness(str, Enum):
    """Composition of the big5 facets: Conscientiousness."""

    TRAIT1 = "self_efficacy"
    TRAIT2 = "orderliness"
    TRAIT3 = "dutifulness"
    TRAIT4 = "achievement_striving"
    TRAIT5 = "self_discipline"
    TRAIT6 = "cautiousness"
