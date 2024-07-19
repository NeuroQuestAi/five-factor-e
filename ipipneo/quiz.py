"""We use this for testing."""

__author__ = "Ederson Corbari"
__email__ = "e@NeuroQuest.ai"
__copyright__ = "Copyright NeuroQuest 2022-2024, Big 5 Personality Traits"
__credits__ = ["John A. Johnson", "Dhiru Kholia"]
__license__ = "MIT"
__version__ = "1.12.0"
__status__ = "production"

import json
import random
import sys
import urllib.request
from itertools import chain, repeat

try:
    from ipipneo import IpipNeo
except ModuleNotFoundError:
    sys.path.insert(0, "../")
    from ipipneo.ipipneo import IpipNeo

URL_IPIP_QUESTIONS = (
    "https://raw.githubusercontent.com/NeuroQuestAi/five-factor-e/main/data/IPIP-NEO"
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

    Returns:
        The filtered list of questions.
    """
    questions = load_ipip_questions(lang=lang, question=question).get("questions", [])

    return list(filter(lambda x: x is not None, questions))


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


def question_translate_120() -> list:
    """Return the available question translations (120)."""
    return ["0. IPIP-NEO Original", "1. EN-US", "2. PT-BR", "3. ES-ES"]


def question_translate_300() -> list:
    """Return the available question translations (300)."""
    return ["0. IPIP-NEO Original"]


def quiz(inventory: int, sex: str, age: int, shuffle: str, lang: int) -> None:
    """
    Inventory / quiz of questions.

    Args:
        - inventory: Inventory model 120 or 300.
        - sex: The sex of the person.
        - age: The age of the person.
        - shuffle: Shuffle the questions.
        - lang: Then number of language.
    """
    questions, answers = (get_questions(lang=lang, question=inventory), [])
    print("\n *** Big Five IPIP-NEO Personality Test ***\n")

    if str(shuffle[0]).upper() == "Y":
        random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nQ.{i} {q.get('text')}\n")
        print(*get_select(lang=lang, question=inventory), sep="\n")

        replies = map(
            input,
            chain(
                ["\nOption: "],
                repeat("Only numbers from 1 to 5 are accepted! Try again: "),
            ),
        )
        option = int(next(filter({"1", "2", "3", "4", "5"}.__contains__, replies)))
        answers.append({"id_question": q.get("id"), "id_select": option})

    result = IpipNeo(question=inventory).compute(
        sex=sex, age=age, answers={"answers": answers}, compare=True
    )

    object = json.dumps(result, indent=4)
    fname = f"result-{str(inventory)}-{result.get('id', 'id')}.json"

    with open(fname, "w") as f:
        f.write(object)

    plot_results(result=result)

    print(f"\nThe result was saved in the file: {fname}")


def plot_results(result: dict) -> None:
    """
    Show the Big-Five result plots.

    Args:
        - result: Result of the person's big-five.
    """
    try:
        import plotext as plt

        big5 = result.get("person").get("result").get("personalities")

        print(
            "\nInventory:",
            str(result.get("model"))
            + "-"
            + str(result.get("question"))
            + " v"
            + str(result.get("version")),
        )
        print("Case:", result.get("id"))
        print("Gender:", result.get("person").get("sex"))
        print("Age:", result.get("person").get("age"), "\n")

        E = [
            "EXTRAVERSION",
            "Friendliness",
            "Gregariousness",
            "Assertiveness",
            "Activity Level",
            "Excitement-Seeking",
            "Cheerfulness",
        ]

        plt.simple_bar(
            E,
            [
                int(big5[2].get("extraversion").get("E")),
                int(big5[2].get("extraversion").get("traits")[0].get("friendliness")),
                int(big5[2].get("extraversion").get("traits")[1].get("gregariousness")),
                int(big5[2].get("extraversion").get("traits")[2].get("assertiveness")),
                int(big5[2].get("extraversion").get("traits")[3].get("activity_level")),
                int(
                    big5[2]
                    .get("extraversion")
                    .get("traits")[4]
                    .get("excitement_seeking")
                ),
                int(big5[2].get("extraversion").get("traits")[5].get("cheerfulness")),
            ],
            width=100,
            title="Big-Five | Extraversion",
            color="orange",
        )
        plt.show()

        print("\n")

        A = [
            "AGREEABLENESS",
            "Trust",
            "Morality",
            "Altruism",
            "Cooperation",
            "Modesty",
            "Sympathy",
        ]

        plt.simple_bar(
            A,
            [
                int(big5[3].get("agreeableness").get("A")),
                int(big5[3].get("agreeableness").get("traits")[0].get("trust")),
                int(big5[3].get("agreeableness").get("traits")[1].get("morality")),
                int(big5[3].get("agreeableness").get("traits")[2].get("altruism")),
                int(big5[3].get("agreeableness").get("traits")[3].get("cooperation")),
                int(big5[3].get("agreeableness").get("traits")[4].get("modesty")),
                int(big5[3].get("agreeableness").get("traits")[5].get("sympathy")),
            ],
            width=100,
            title="Big-Five | Agreeableness",
            color="green",
        )
        plt.show()

        print("\n")

        C = [
            "CONSCIENTIOUSNESS",
            "Self-Efficacy",
            "Orderliness",
            "Dutifulness",
            "Achievement-Striving",
            "Self-Discipline",
            "Cautiousness",
        ]

        plt.simple_bar(
            C,
            [
                int(big5[1].get("conscientiousness").get("C")),
                int(
                    big5[1]
                    .get("conscientiousness")
                    .get("traits")[0]
                    .get("self_efficacy")
                ),
                int(
                    big5[1].get("conscientiousness").get("traits")[1].get("orderliness")
                ),
                int(
                    big5[1].get("conscientiousness").get("traits")[2].get("dutifulness")
                ),
                int(
                    big5[1]
                    .get("conscientiousness")
                    .get("traits")[3]
                    .get("achievement_striving")
                ),
                int(
                    big5[1]
                    .get("conscientiousness")
                    .get("traits")[4]
                    .get("self_discipline")
                ),
                int(
                    big5[1]
                    .get("conscientiousness")
                    .get("traits")[5]
                    .get("cautiousness")
                ),
            ],
            width=100,
            title="Big-Five | Consciousness",
            color="magenta",
        )
        plt.show()

        print("\n")

        N = [
            "NEUROTICISM",
            "Anxiety",
            "Anger",
            "Depression",
            "Self-Consciousness",
            "Immoderation",
            "Vulnerability",
        ]

        plt.simple_bar(
            N,
            [
                int(big5[4].get("neuroticism").get("N")),
                int(big5[4].get("neuroticism").get("traits")[0].get("anxiety")),
                int(big5[4].get("neuroticism").get("traits")[1].get("anger")),
                int(big5[4].get("neuroticism").get("traits")[2].get("depression")),
                int(
                    big5[4]
                    .get("neuroticism")
                    .get("traits")[3]
                    .get("self_consciousness")
                ),
                int(big5[4].get("neuroticism").get("traits")[4].get("immoderation")),
                int(big5[4].get("neuroticism").get("traits")[5].get("vulnerability")),
            ],
            width=100,
            title="Big-Five | Neuroticism",
            color="red",
        )
        plt.show()

        print("\n")

        O = [
            "OPENNESS",
            "Imagination",
            "Artistic Interests",
            "Emotionality",
            "Adventurousness",
            "Intellect",
            "Liberalism",
        ]

        plt.simple_bar(
            O,
            [
                int(big5[0].get("openness").get("O")),
                int(big5[0].get("openness").get("traits")[0].get("imagination")),
                int(big5[0].get("openness").get("traits")[1].get("artistic_interests")),
                int(big5[0].get("openness").get("traits")[2].get("emotionality")),
                int(big5[0].get("openness").get("traits")[3].get("adventurousness")),
                int(big5[0].get("openness").get("traits")[4].get("intellect")),
                int(big5[0].get("openness").get("traits")[5].get("liberalism")),
            ],
            width=100,
            title="Big-Five | Openness",
            color="blue",
        )
        plt.show()

    except ModuleNotFoundError:
        print("\n*** Unable to plot graphs! Install the package (plotext). ***\n")


def main() -> None:
    """Initialize the test."""
    print("\n *** Welcome to Big Five IPIP-NEO Personality Test ***")

    yes_or_no = {"Y", "y", "yes", "Yes", "YES", "N", "n", "no", "No", "NO"}

    replies = map(
        input,
        chain(
            ["\n> Do you wish to continue? Yes / No: "],
            repeat("Please, only Yes or No are valid! Try again: "),
        ),
    )
    go = str(next(filter(yes_or_no.__contains__, replies)))

    if go.upper() == "NO" or go.upper() == "N":
        print("Bye!")
        sys.exit(0)

    replies = map(
        input,
        chain(
            ["\n> What inventory model will you make? 120 / 300: "],
            repeat("Please, only 120 or 300 are valid! Try again: "),
        ),
    )
    inventory = int(next(filter({"120", "300"}.__contains__, replies)))

    print("\n====================================================================")
    if inventory == 120:
        print(
            "The following test contains 120 questions which is estimated to take you about 15 minutes to complete!"
        )
    elif inventory == 300:
        print(
            "The following test contains 300 questions which is estimated to take you about 35 minutes to complete!"
        )

    replies = map(
        input,
        chain(
            ["\n> What is your sex Male or Female? M / F: "],
            repeat("Please, only M or F are valid! Try again: "),
        ),
    )
    sex = str(next(filter({"F", "f", "M", "m"}.__contains__, replies)))

    replies = map(
        input,
        chain(
            ["\n> What is your age? "],
            repeat("Please, only numbers between 10 and 110 are valid! Try again: "),
        ),
    )
    age = int(next(filter(set(map(str, range(10, 110))).__contains__, replies)))

    replies = map(
        input,
        chain(
            ["\n> Do you want to shuffle the questions? Yes / No: "],
            repeat("Please, only Yes or No are valid! Try again: "),
        ),
    )
    shuffle = str(next(filter(yes_or_no.__contains__, replies)))

    print("\n====================================================================")
    if inventory == 120:
        print(*question_translate_120(), sep="\n")
    elif inventory == 300:
        print(*question_translate_300(), sep="\n")

    replies = map(
        input,
        chain(
            ["\n> Choose the language of the questions above: "],
            repeat(
                "Please, only the numbers that are on the list are valid! Try again: "
            ),
        ),
    )
    lang = int(next(filter(set(map(str, range(0, 3))).__contains__, replies)))

    quiz(
        inventory=int(inventory),
        sex=str(sex).upper(),
        age=int(age),
        shuffle=str(shuffle).upper(),
        lang=int(lang),
    )


if __name__ == "__main__":
    main()
