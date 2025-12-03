from src.utils import read_list_input

def part1(puzzle_input: list[str]) -> int:

    total_joltage = 0

    for bank in puzzle_input:
        digit_array = [int(digit) for digit in bank]

        max_value = 0
        max_value_index = None

        second_largest_value = 0

        for i in range(len(digit_array) - 1):
            if digit_array[i] > max_value:
                max_value = digit_array[i]
                max_value_index = i

        for j in range(max_value_index + 1, len(digit_array)):
            if digit_array[j] > second_largest_value:
                second_largest_value = digit_array[j]

        total_joltage += (max_value * 10) + second_largest_value

    return total_joltage

def part2(puzzle_input: list[str], batteries: int = 12) -> int:
    total_joltage = 0

    for bank in puzzle_input:
        digit_array = [int(digit) for digit in bank]
        ptr1 = 0
        ptr2 = len(digit_array) - (batteries - 1)
        digits = []

        while(len(digits)) < batteries:
            current_max = 0
            current_max_idx = None

            for i in range(ptr1, ptr2):
                if digit_array[i] > current_max:
                    current_max = digit_array[i]
                    current_max_idx = i

            digits.append(current_max)
            ptr1 = current_max_idx + 1
            ptr2 += 1

        str_digits = [str(digit) for digit in digits]
        total_joltage += int(''.join(str_digits))

    
    return total_joltage

if __name__ == "__main__":

    input_path = "/Users/nithinanand/Documents/study/advent_of_code/src/three/input.txt"
    # input_path = "/Users/nithinanand/Documents/study/advent_of_code/src/three/test_case.txt"


    puzzle = read_list_input(input_path=input_path)
    print(part1(puzzle_input=puzzle))
    print(part2(puzzle_input=puzzle, batteries=12))