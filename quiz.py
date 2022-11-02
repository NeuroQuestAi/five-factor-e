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

URL_PROD = "https://raw.githubusercontent.com/neural7/five-factor-e/main/data/IPIP-NEO/120/questions.json"
URL_DEV = "https://raw.githubusercontent.com/neural7/five-factor-e/feature/v1.2.0/data/IPIP-NEO/120/questions.json"


def load_original_questions_ipip() -> dict:
    """Load the original questions into the project repo."""
    return json.loads(urllib.request.urlopen(URL_PROD).read())


def quiz(sex: str, age: int, shuffle: str) -> None:
    """
    Inventory of questions.

    Args:
        - sex: The sex of the person.
        - age: The age of the person.
        - shuffle: Shuffle the questions.
    """
    questions, answers = (
        [x for x in load_original_questions_ipip().get("questions", [])],
        [],
    )

    print("\n *** Big Five IPIP-NEO Personality Test ***\n")

    if shuffle == "Y":
        random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"Q.{i} {q.get('text')}\n")

        print("1. Very Inaccurate")
        print("2. Moderately Inaccurate")
        print("3. Neither Accurate Nor Inaccurate")
        print("4. Moderately Accurate")
        print("5. Very Accurate")

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

    result = IpipNeo(question=120).compute(
        sex="M", age=40, answers={"answers": answers}
    )

    print(json.dumps(result, indent=4))


def main() -> None:
    """Initialize the test."""
    print("\n *** Welcome to Big Five IPIP-NEO Personality Test ***\n")
    print(
        "The following test contains 120 questions which is estimated to take you about 10 minutes to complete!"
    )

    go = str(input("\nDo you wish to continue? Yes / No: "))
    if go.upper() == "NO" or go.upper() == "N":
        sys.exit(0)

    sex = str(input("\nWhat is your sex Male or Female? M / F: "))
    assert (
        sex.upper() == "M" or sex.upper() == "F"
    ), "The (sex) field must contain (M or F)!"

    age = int(input("\nWhat is your age? "))
    assert isinstance(age, int), "The (age) field must be an integer!"
    if not (10 <= age <= 120):
        print(f"The age ({age}) must be between 10 and 120!")
        sys.exit(0)

    shuffle = str(input("\nDo you want to shuffle the questions? Yes / No: "))
    if shuffle.upper() == "NO" or shuffle.upper() == "N":
        shuffle = "N"
    else:
        shuffle = "Y"

    quiz(sex=sex, age=age, shuffle=shuffle)


if __name__ == "__main__":
    main()
