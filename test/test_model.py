"""Unit tests for Model."""

import unittest

from big5.model import QuestionNumber

class TestModel(unittest.TestCase):

    def test_question_number(self) -> None:
        model = QuestionNumber

        self.assertEqual(model.IPIP_120, 120)
        self.assertEqual(model.IPIP_120.value, 120)

        self.assertEqual(model.IPIP_300, 300)
        self.assertEqual(model.IPIP_300.value, 300)

        x1 = list(map(int, model))
        self.assertEqual(len(x1), 2)
