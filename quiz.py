"""We use this for testing."""

__author__ = "Ederson Corbari"
__email__ = "e@neural7.io"
__copyright__ = "Copyright Neural7 2022, Big 5 Personality Traits"
__credits__ = ["John A. Johnson", "Dhiru Kholia"]
__license__ = "MIT"
__version__ = "1.2.0"
__status__ = "production"

import json
import random
import sys
import urllib.request

try:
    from ipipneo import IpipNeo
except ModuleNotFoundError:
    from ipipneo.ipipneo import IpipNeo

URL_IPIP_QUESTIONS = (
    "https://raw.githubusercontent.com/neural7/five-factor-e/main/data/IPIP-NEO/120"
)


def load_ipip_questions(lang: int) -> dict:
    """Load the IPIP-NEO questions."""
    target = URL_IPIP_QUESTIONS
    if lang == 0:
        target = target + "/questions.json"
    if lang == 1:
        target = target + "/translation/questions-en-us.json"
    if lang == 2:
        target = target + "/translation/questions-pt-br.json"
    if lang == 3:
        target = target + "/translation/questions-es-es.json"
    try:
        return json.loads(urllib.request.urlopen(target).read())
    except BaseException:
        print(f"\nQuestion package not found in repository: {target}")
        sys.exit(0)


def get_questions(lang: int) -> list:
    """Filter only the question list."""
    return [x for x in load_ipip_questions(lang=lang).get("questions", [])]


def get_select(lang: int) -> list:
    """Filter only the select list."""
    return [
        str(x.get("id", 0)) + ". " + str(x.get("text", None))
        for x in load_ipip_questions(lang=lang).get("select", [])
    ]


def question_translate() -> list:
    """Return the available question translations."""
    return ["0. IPIP-NEO Original", "1. EN-US", "2. PT-BR", "3. ES-ES"]


def quiz(inventory: int, sex: str, age: int, shuffle: str, lang: int) -> None:
    """
    Inventory of questions.

    Args:
        - inventory: Inventory model 120 or 300.
        - sex: The sex of the person.
        - age: The age of the person.
        - shuffle: Shuffle the questions.
        - lang: Then number of language.
    """
    answers = questions = []
    if inventory == 120:
        questions = get_questions(lang=lang)
    elif inventory == 300:
        pass
    else:
        raise BaseException(f"Invalid inventory model: {inventory}")

    print("\n *** Big Five IPIP-NEO Personality Test ***\n")

    if shuffle == "Y":
        random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nQ.{i} {q.get('text')}\n")
        print(*get_select(lang=lang), sep="\n")

        try:
            option = int(input("\nOption: "))
        except BaseException as e:
            print(f"\n!!! Invalid option {e}. The quiz has been aborted !!!\n")
            sys.exit(0)

        if option < 1 or option > 5:
            print(f"\n!!! Invalid answer {option}. Only options between 1 to 5 !!!")
            option = int(input("\nOption: "))
            if option < 1 or option > 5:
                print(f"\n!!! Invalid answer {option}. The quiz has been aborted !!!\n")
                sys.exit(0)

        answers.append({"id_question": q.get("id"), "id_select": option})

    result = IpipNeo(question=inventory).compute(
        sex=sex, age=age, answers={"answers": answers}
    )

    print(json.dumps(result, indent=4))


def main() -> None:
    """Initialize the test."""
    print("\n *** Welcome to Big Five IPIP-NEO Personality Test ***")

    go = str(input("\nDo you wish to continue? Yes / No: "))
    if go.upper() == "NO" or go.upper() == "N":
        sys.exit(0)

    inventory = int(input("\nWhat inventory model will you make? 120 / 300: "))
    assert isinstance(inventory, int), "The (inventory) field must be an integer!"
    if inventory != 120 and inventory != 300:
        print(f"Invalid inventory model: {inventory}!")
        sys.exit(0)

    print("\n====================================================================")
    if inventory == 120:
        print(
            "The following test contains 120 questions which is estimated to take you about 15 minutes to complete!"
        )
    elif inventory == 300:
        print(
            "The following test contains 300 questions which is estimated to take you about 35 minutes to complete!"
        )

    sex = str(input("\nWhat is your sex Male or Female? M / F: "))
    assert (
        sex.upper() == "M" or sex.upper() == "F"
    ), "The (sex) field must contain (M or F)!"

    age = int(input("\nWhat is your age? "))
    assert isinstance(age, int), "The (age) field must be an integer!"
    if not (18 <= age <= 100):
        print(f"The age ({age}) must be between 18 and 100!")
        sys.exit(0)

    shuffle = str(input("\nDo you want to shuffle the questions? Yes / No: "))
    if shuffle.upper() == "NO" or shuffle.upper() == "N":
        shuffle = "N"
    else:
        shuffle = "Y"

    print("\n====================================================================")
    print(*question_translate(), sep="\n")
    lang = int(
        input("\nChoose the language of the questions above, (enter the number)? ")
    )
    assert isinstance(age, int), "The (lang) field must be an integer!"

    quiz(
        inventory=int(inventory),
        sex=sex.upper(),
        age=int(age),
        shuffle=shuffle,
        lang=int(lang),
    )


if __name__ == "__main__":
    main()
