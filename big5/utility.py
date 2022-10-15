
def check(answers: list) -> None | BaseException:
    match self._nquestion:
        case 300:
            assert len(answers) == 300, 'The number of questions should be 300!'
        case 120:
            assert len(answers) == 120, 'The number of questions should be 120!'
        case _:
            raise BaseException('Number of answers is invalid!')
