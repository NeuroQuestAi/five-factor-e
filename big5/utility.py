"""Add desc."""


def assert_ipip_neo_answers(answers: list, nquestion) -> None | AssertionError:
    assert (
        len(answers) == 300 if nquestion == 300 else 120 if nquestion == 120 else 0
    ), 'The number of questions should be 300 or 120!'
