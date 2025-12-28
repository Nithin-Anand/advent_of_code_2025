from ..utils import read_list_input
from .problem import AdditionProblem, MultiplicationProblem, BaseProblem

def process_input(file_input: list[str]) -> list[BaseProblem]:

    problems = []
    number_of_problems = len(clean_array(file_input[0].split(" ")))
    
    list_of_numbers = [[] for _ in range(number_of_problems)]

    for i in range(len(file_input) - 1):

        numbers = file_input[i].split(" ")
        numbers = clean_array(numbers)

        for i in range(number_of_problems):
            list_of_numbers[i].append(int(numbers[i]))

    operators = clean_array(file_input[-1].split(" "))
    
    for i in range(number_of_problems):

        problem_operator = operators[i]

        if problem_operator == "*":
            problems.append(MultiplicationProblem(list_of_numbers[i]))
        elif problem_operator == "+":
            problems.append(AdditionProblem(list_of_numbers[i]))

    return problems

def clean_array(str_array):
    modified_array = str_array
    while '' in modified_array:
        modified_array.remove('')

    return modified_array

def sum_all_problems(problems: list[BaseProblem]) -> int:
    total = 0

    for problem in problems:
        total += problem.resolve_problem()

    return total

def part1(file_input: list[str]):
    print(sum_all_problems(process_input(file_input)))

if __name__ == "__main__":

    test_path = "/Users/nithinanand/Documents/study/advent_of_code/src/six/test.txt"

    test_input = read_list_input(test_path)

    part1(file_input=test_input)


    puzzle_path = '/Users/nithinanand/Documents/study/advent_of_code/src/six/input.txt'
    puzzle_input = read_list_input(puzzle_path)
    part1(file_input=puzzle_input)
