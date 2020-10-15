from git import Repo
from exercises import *

repo = Repo(".")
commits = list(repo.iter_commits("master"))
messages = map(lambda commit: commit.message(), commits)


def commit_exists(message):

    for commit in commits:
        if message.lower() in commit.message.lower():
            return True

    return False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(7) == 5040
    assert factorial(8) == 40320
    assert factorial(9) == 362880
    assert factorial(10) == 3628800


def test_factorial_commit():
    assert commit_exists("implementing factorial function")


def test_multiples():
    assert multiples([1, 2, 3, 4], 2) == [2, 4]
    assert multiples([1, 2, 3, 4], 1) == [1, 2, 3, 4]
    assert multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3) == [
        3, 6, 9, 12]


def test_multiples_commit():
    assert commit_exists("implementing multiples function")
