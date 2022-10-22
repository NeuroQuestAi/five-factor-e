"""Add desc."""

from enum import Enum


class Big5Neuroticism(str, Enum):
    """Composition of the big5 facets: Neuroticism."""

    TRAIT1 = 'Anxiety'
    TRAIT2 = 'Anger'
    TRAIT3 = 'Depression'
    TRAIT4 = 'Self-Consciousness'
    TRAIT5 = 'Immoderation'
    TRAIT6 = 'Vulnerability'


class Big5Extraversion(str, Enum):
    """Composition of the big5 facets: Extraversion."""

    TRAIT1 = 'Friendliness'
    TRAIT2 = 'Gregariousness'
    TRAIT3 = 'Assertiveness'
    TRAIT4 = 'Activity-Level'
    TRAIT5 = 'Excitement-Seeking'
    TRAIT6 = 'Cheerfulness'


class Big5Openness(str, Enum):
    """Composition of the big5 facets: Openness."""

    TRAIT1 = 'Imagination'
    TRAIT2 = 'Artistic-Interests'
    TRAIT3 = 'Emotionality'
    TRAIT4 = 'Adventurousness'
    TRAIT5 = 'Intellect'
    TRAIT6 = 'Liberalism'


class Big5Agreeableness(str, Enum):
    """Composition of the big5 facets: Agreeableness."""

    TRAIT1 = 'Trust'
    TRAIT2 = 'Morality'
    TRAIT3 = 'Altruism'
    TRAIT4 = 'Cooperation'
    TRAIT5 = 'Modesty'
    TRAIT6 = 'Sympathy'


class Big5Conscientiousness(str, Enum):
    """Composition of the big5 facets: Conscientiousness."""

    TRAIT1 = 'Self-Efficacy'
    TRAIT2 = 'Orderliness'
    TRAIT3 = 'Dutifulness'
    TRAIT4 = 'Achievement-Striving'
    TRAIT5 = 'Self-Discipline'
    TRAIT6 = 'Cautiousness'


def assert_ipip_neo_answers(answers: list, nquestion) -> None | AssertionError:
    assert (
        len(answers) == 300 if nquestion == 300 else 120 if nquestion == 120 else 0
    ), 'The number of questions should be 300 or 120!'


def create_big5_dict(label: str, big5: int, x: list, y: list) -> dict:

    if label == 'N':
        model = Big5Neuroticism
    elif label == 'E':
        model = Big5Extraversion
    elif label == 'O':
        model = Big5Openness
    elif label == 'A':
        model = Big5Agreeableness
    elif label == 'C':
        model = Big5Conscientiousness
    else:
        raise 'Big five is invalid'

    return {
        label: big5,
        'traits': [
            {'trait': 1, model.TRAIT1.value: x[1], 'score': y[1]},
            {'trait': 2, model.TRAIT2.value: x[2], 'score': y[2]},
            {'trait': 3, model.TRAIT3.value: x[3], 'score': y[3]},
            {'trait': 4, model.TRAIT4.value: x[4], 'score': y[4]},
            {'trait': 5, model.TRAIT5.value: x[5], 'score': y[5]},
            {'trait': 6, model.TRAIT6.value: x[6], 'score': y[6]},
        ],
    }
