"""Tests..."""

from big5.ipipneo import IpipNeo


import json

answers = {}

with open('data/IPIP-NEO/120/answers.json') as f:
    answers = json.load(f)

answers = [x for x in answers.get('answers')]
# print(answers)

answers = sorted(answers, key=lambda x: x['id_question'])
print(answers)

answers = [x['id_select'] for x in answers if x['id_select'] >= 1]
print(len(answers))

ipip = IpipNeo(question=120)

ipip.compute(sex='F', age=27, answers=answers)
