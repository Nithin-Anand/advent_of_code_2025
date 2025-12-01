import pytest
from one.password_cracker import crack_password, read_input

def password_crack_flow(input_path: str) -> int:
    test_case_input = read_input(input_path)
    return crack_password(test_case_input)


def test_simple_case():
    simple_test_input_path = "/Users/nithinanand/Documents/study/advent_of_code/tests/1/simple_test_input.txt"

    assert password_crack_flow(simple_test_input_path) == 1

def test_provided():
    provided = "/Users/nithinanand/Documents/study/advent_of_code/tests/1/test_case.txt"
    assert password_crack_flow(provided) == 3

def test_bigger_swing():
    swing = "/Users/nithinanand/Documents/study/advent_of_code/tests/1/bigger_swing_test.txt"
    assert password_crack_flow(swing) == 3

def test_ninety_nine():
    nn = '/Users/nithinanand/Documents/study/advent_of_code/tests/1/another_test.txt'
    assert password_crack_flow(nn) == 1