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
    "https://raw.githubusercontent.com/neural7/five-factor-e/main/data/IPIP-NEO"
)


def load_ipip_questions(lang: int, question: int) -> dict:
    """
    Load the IPIP-NEO questions.

    Args:
        - lang: The language ID.
        - question: Inventory model 120 or 300.
    """
    target = URL_IPIP_QUESTIONS + "/" + str(question)
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


def get_questions(lang: int, question: int) -> list:
    """
    Filter only the question list.

    Args:
        - lang: The language ID.
        - question: Inventory model 120 or 300.
    """
    return [
        x
        for x in load_ipip_questions(lang=lang, question=question).get("questions", [])
    ]


def get_select(lang: int, question: int) -> list:
    """
    Filter only the select list.

    Args:
        - lang: The language ID.
        - question: Inventory model 120 or 300.
    """
    return [
        str(x.get("id", 0)) + ". " + str(x.get("text", None))
        for x in load_ipip_questions(lang=lang, question=question).get("select", [])
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
    questions, answers = (get_questions(lang=lang, question=inventory), [])
    print("\n *** Big Five IPIP-NEO Personality Test ***\n")

    if shuffle == "Y":
        random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nQ.{i} {q.get('text')}\n")
        print(*get_select(lang=lang, question=inventory), sep="\n")

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
        sex=sex, age=age, answers={"answers": answers}, compare=True
    )

    object = json.dumps(result, indent=4)
    fname = f"result-{str(inventory)}-{result.get('id', 'id')}.json"

    with open(fname, "w") as f:
        f.write(object)

    display_result(result=result)

    print(f"The result was saved in the file: {fname}")


def display_result(result: dict) -> None:
    """Print the screen result."""
    print("\n====================================================================\n")
    big5 = result.get("person").get("result").get("personalities")

    print(f"EXTRAVERSION....................{big5[2].get('Extraversion').get('E')}")
    print(
        f"1.Friendliness..................{big5[2].get('Extraversion').get('traits')[0].get('Friendliness')}"
    )
    print(
        f"2.Gregariousness................{big5[2].get('Extraversion').get('traits')[1].get('Gregariousness')}"
    )
    print(
        f"3.Assertiveness.................{big5[2].get('Extraversion').get('traits')[2].get('Assertiveness')}"
    )
    print(
        f"4.Activity Level................{big5[2].get('Extraversion').get('traits')[3].get('Activity-Level')}"
    )
    print(
        f"5.Excitement-Seeking............{big5[2].get('Extraversion').get('traits')[4].get('Excitement-Seeking')}"
    )
    print(
        f"6.Cheerfulness..................{big5[2].get('Extraversion').get('traits')[5].get('Cheerfulness')}\n"
    )

    print(f"AGREEABLENESS...................{big5[3].get('Agreeableness').get('A')}")
    print(
        f"1.Trust.........................{big5[3].get('Agreeableness').get('traits')[0].get('Trust')}"
    )
    print(
        f"2.Morality......................{big5[3].get('Agreeableness').get('traits')[1].get('Morality')}"
    )
    print(
        f"3.Altruism......................{big5[3].get('Agreeableness').get('traits')[2].get('Altruism')}"
    )
    print(
        f"4.Cooperation...................{big5[3].get('Agreeableness').get('traits')[3].get('Cooperation')}"
    )
    print(
        f"5.Modesty.......................{big5[3].get('Agreeableness').get('traits')[4].get('Modesty')}"
    )
    print(
        f"6.Sympathy......................{big5[3].get('Agreeableness').get('traits')[5].get('Sympathy')}\n"
    )

    print(
        f"CONSCIENTIOUSNESS...............{big5[1].get('Conscientiousness').get('C')}"
    )
    print(
        f"1.Self-Efficacy.................{big5[1].get('Conscientiousness').get('traits')[0].get('Self-Efficacy')}"
    )
    print(
        f"2.Orderliness...................{big5[1].get('Conscientiousness').get('traits')[1].get('Orderliness')}"
    )
    print(
        f"3.Dutifulness...................{big5[1].get('Conscientiousness').get('traits')[2].get('Dutifulness')}"
    )
    print(
        f"4.Achievement-Striving..........{big5[1].get('Conscientiousness').get('traits')[3].get('Achievement-Striving')}"
    )
    print(
        f"5.Self-Discipline...............{big5[1].get('Conscientiousness').get('traits')[4].get('Self-Discipline')}"
    )
    print(
        f"6.Cautiousness..................{big5[1].get('Conscientiousness').get('traits')[5].get('Cautiousness')}\n"
    )

    print(f"NEUROTICISM.....................{big5[4].get('Neuroticism').get('N')}")
    print(
        f"1.Anxiety.......................{big5[4].get('Neuroticism').get('traits')[0].get('Anxiety')}"
    )
    print(
        f"2.Anger.........................{big5[4].get('Neuroticism').get('traits')[1].get('Anger')}"
    )
    print(
        f"3.Depression....................{big5[4].get('Neuroticism').get('traits')[2].get('Depression')}"
    )
    print(
        f"4.Self-Consciousness............{big5[4].get('Neuroticism').get('traits')[3].get('Self-Consciousness')}"
    )
    print(
        f"5.Immoderation..................{big5[4].get('Neuroticism').get('traits')[4].get('Immoderation')}"
    )
    print(
        f"6.Vulnerability.................{big5[4].get('Neuroticism').get('traits')[5].get('Vulnerability')}\n"
    )

    print(f"OPENNESS TO EXPERIENCE..........{big5[0].get('Openness').get('O')}")
    print(
        f"1.Imagination...................{big5[0].get('Openness').get('traits')[0].get('Imagination')}"
    )
    print(
        f"2.Artistic Interests............{big5[0].get('Openness').get('traits')[1].get('Artistic-Interests')}"
    )
    print(
        f"3.Emotionality..................{big5[0].get('Openness').get('traits')[2].get('Emotionality')}"
    )
    print(
        f"4.Adventurousness...............{big5[0].get('Openness').get('traits')[3].get('Adventurousness')}"
    )
    print(
        f"5.Intellect.....................{big5[0].get('Openness').get('traits')[4].get('Intellect')}"
    )
    print(
        f"6.Liberalism....................{big5[0].get('Openness').get('traits')[5].get('Liberalism')}"
    )
    print("\n====================================================================\n")


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
