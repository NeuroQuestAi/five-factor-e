"""Unit tests for IpipNeo 300."""

import json
import unittest

from ipipneo.ipipneo import IpipNeo


def load_mock_answers_300() -> dict:
    with open("test/mock/answers-test-300-case-1.json") as f:
        data = json.load(f)
    return data


class TestX01300(unittest.TestCase):
    def test_compute_300_compare(self) -> None:
        #############################################
        # 1. Test with 40 year old man.
        #############################################

        result = IpipNeo(question=300).compute(
            sex="M", age=40, answers=load_mock_answers_300(), compare=True
        )

        compare_original = result["person"]["result"]["compare"][
            "user_answers_original"
        ]
        compare_reverse = result["person"]["result"]["compare"]["user_answers_reversed"]

        differences = []
        for original, reversed in zip(compare_original, compare_reverse):
            if original["id_select"] != reversed["id_select"]:
                differences.append(
                    {
                        "id_question": original["id_question"],
                        "id_select_original": original["id_select"],
                        "id_select_reversed": reversed["id_select"],
                    }
                )

        self.assertEqual(len(differences), 144)

        print("\n")
        print("O", result["person"]["result"]["personalities"][0]["openness"]["O"])
        print("C", result["person"]["result"]["personalities"][1]["conscientiousness"]["C"])
        print("E", result["person"]["result"]["personalities"][2]["extraversion"]["E"])
        print("A", result["person"]["result"]["personalities"][3]["agreeableness"]["A"])
        print("N", result["person"]["result"]["personalities"][4]["neuroticism"]["N"])

        # Test unisex norm
        from ipipneo.norm import Norm

        domain = {
            "N": result["person"]["result"]["personalities"][4]["neuroticism"]["N"],
            "E": result["person"]["result"]["personalities"][2]["extraversion"]["E"],
            "O": result["person"]["result"]["personalities"][0]["openness"]["O"],
            "A": result["person"]["result"]["personalities"][3]["agreeableness"]["A"],
            "C": result["person"]["result"]["personalities"][1]["conscientiousness"]["C"],
        }
        unisex_norm = {
            "ns": [0, 55.5, 42.9, 40, 5.7, 1.5, 5, 5, 5, 5, 5]
        }

        # T = 10 * (X - M) / SD + 50
        norm = Norm.calc(domain=domain, norm=unisex_norm)
        print(norm)
