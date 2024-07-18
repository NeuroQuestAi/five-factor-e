"""Contains utility functions used in the library."""

__author__ = "Ederson Corbari"
__email__ = "e@NeuroQuest.ai"
__copyright__ = "Copyright NeuroQuest 2022-2024, Big 5 Personality Traits"
__credits__ = ["John A. Johnson", "Dhiru Kholia"]
__license__ = "MIT"
__version__ = "1.12.0"
__status__ = "production"

from datetime import datetime
from enum import Enum

from ipipneo.model import (Big5Agreeableness, Big5Conscientiousness,
                           Big5Extraversion, Big5Neuroticism, Big5Openness)


def raise_if_sex_is_invalid(sex: str) -> bool | AssertionError | BaseException:
    """
    Validate the sex field.

    Args:
        - sex: Male is M or Female is F.
    """
    if not sex:
        raise BaseException("The (sex) field is required!")

    assert isinstance(sex, str), "The (sex) field must be a string!"
    assert sex == "M" or sex == "F", "The (sex) field must contain (M or F)!"
    return True


def raise_if_age_is_invalid(age: int) -> bool | AssertionError | BaseException:
    """
    Validate the age field.

    Args:
        - age: Person's age.
    """
    if not age:
        raise BaseException("The (age) field is required!")

    assert isinstance(age, int), "The (age) field must be an integer!"

    min, max = (10, 110)
    if not (min <= age <= max):
        raise AssertionError(
            "The age (%r) must be between %r and %r!" % (age, min, max)
        )

    return True


def answers_is_valid(answers: list) -> bool | AssertionError | BaseException:
    """
    Validate the answers field.

    Args:
        - answers: List with the answers.
    """
    if not answers:
        raise BaseException("The (answers) field is required!")

    assert isinstance(answers, list), "The (answers) field must be a list!"

    if 0 in answers:
        raise BaseException("It cannot contain zeros in the answer list!")

    if 1 in [1 if x > 5 else 0 for x in answers]:
        raise BaseException("You cannot have answers with a number greater than 5!")

    assert (
        len(answers) == 120 or len(answers) == 300
    ), "The (answers) field should be of size 120 or 300!"

    return True


def organize_list_json(answers: dict) -> list | AssertionError | BaseException:
    """
    Organize input list in json format.

    Args:
        - answers: Dictionary with the list of answers.
    """
    assert isinstance(answers, dict), "The (answers) field must be a dict!"

    if "answers" not in answers:
        raise BaseException("The key named (answers) was not found!")

    if not any("id_question" in x for x in answers.get("answers", [])):
        raise BaseException("The key named (id_question) was not found!")

    if not any("id_select" in x for x in answers.get("answers", [])):
        raise BaseException("The key named (id_select) was not found!")

    return [
        x["id_select"]
        for x in sorted(
            [x for x in answers.get("answers", [])], key=lambda x: x["id_question"]
        )
        if x["id_select"] >= 1
    ]


def reverse_scored(select: int) -> int | BaseException:
    """
    Apply reverse scoring (1=5, 2=4, 4=2, 5=1).

    Args:
        - answers: Selected item.
    """
    if select == 1:
        return 5
    elif select == 2:
        return 4
    elif select == 3:
        return 3
    elif select == 4:
        return 2
    elif select == 5:
        return 1
    raise BaseException(f"Something wrong in the selection option: {select}")


def big5_ocean_is_valid(label: str) -> bool | BaseException:
    """
    Validate if the Big-Five acronym is correct.

    Args:
        - label: The acronym for the Big-Five standard O.C.E.A.N.
    """
    if label == "O":
        return True
    if label == "C":
        return True
    if label == "E":
        return True
    if label == "A":
        return True
    if label == "N":
        return True
    raise BaseException("The Big-Five label is invalid!")


def big5_target(label: str) -> Enum | BaseException:
    """
    Return the facets of a Big-Five.

    Args:
        - label: The acronym for the Big-Five standard O.C.E.A.N.
    """
    big5_ocean_is_valid(label=label)

    try:
        if label == "O":
            return Big5Openness
        if label == "C":
            return Big5Conscientiousness
        if label == "E":
            return Big5Extraversion
        if label == "A":
            return Big5Agreeableness
        if label == "N":
            return Big5Neuroticism
    except BaseException:
        raise BaseException("The Big-Five label is invalid!")


def create_big5_dict(label: str, big5: float, x: list, y: list) -> dict:
    """
    Create a dictionary for Big-Five final result.

    Args:
        - label: The acronym for the Big-Five standard O.C.E.A.N.
        - big5: The list with the personalities / facets.
        - x: The list with the facets.
        - y: The list of scores.
    """
    return {
        label: big5,
        "traits": [
            {
                "trait": 1,
                big5_target(label=label).TRAIT1.value: x[1],
                "score": y[1],
            },
            {
                "trait": 2,
                big5_target(label=label).TRAIT2.value: x[2],
                "score": y[2],
            },
            {
                "trait": 3,
                big5_target(label=label).TRAIT3.value: x[3],
                "score": y[3],
            },
            {
                "trait": 4,
                big5_target(label=label).TRAIT4.value: x[4],
                "score": y[4],
            },
            {
                "trait": 5,
                big5_target(label=label).TRAIT5.value: x[5],
                "score": y[5],
            },
            {
                "trait": 6,
                big5_target(label=label).TRAIT6.value: x[6],
                "score": y[6],
            },
        ],
    }


def add_dict_footer() -> dict:
    return {
        "library": "five-factor-e",
        "version": __version__,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
