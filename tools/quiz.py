"""A aa."""

import json
import sys
import urllib.request

URL = "https://raw.githubusercontent.com/neural7/five-factor-e/main/data/IPIP-NEO/120/questions.json"
def load_ipip_120_questions() -> dict:
    return json.loads(urllib.request.urlopen(URL).read())


questions = load_ipip_120_questions()
questions = [x for x in questions.get("questions")]
# print(questions)

answers = []

while True:

    for i, q in enumerate(questions, start=1):
        print(f"Q.{i} {q.get('text')}\n")

        print("1. Very Inaccurate")
        print("2. Moderately Inaccurate")
        print("3. Neither Accurate Nor Inaccurate")
        print("4. Moderately Accurate")
        print("5. Very Accurate")

        option = int(input("\nOption: "))

        if option > 5:
            print(f"\n!!! Invalid answer {option}. Only options between 1 to 5 !!!")
            option = int(input("\nOption: "))
            if option > 5:
                print(f"\n!!! Invalid answer {option}. The quiz has been aborted !!!\n")
                sys.exit(0)

    # answers.append(resp)
    # print(resp)


"""
print("Calculator")
# number1 = int(input("Give the first number:"))
# number2 = int(input("Give the second number:"))

while True:
    password = input('Enter your password: ')

    if len(password) < 5:
        print('Password too short')
        continue
    else:
        print(f'You entered {password}')
        break
"""
