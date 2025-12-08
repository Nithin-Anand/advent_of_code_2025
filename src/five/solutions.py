from src.utils import read_list_input

def build_list_of_bounds(id_ranges: list[str]) -> list[tuple[int,int]]:

    valid_id_bounds = []

    id_lines = 0

    for ids in id_ranges:

        split_line = ids.split("-")
        lower_bound = int(split_line[0])
        upper_bound = int(split_line[1])

        valid_id_bounds.append((lower_bound, upper_bound))
        
    return valid_id_bounds

def split_puzzle_input(puzzle_input: list[str]):
    id_ranges = []
    ids_to_test = []

    reached_middle = False

    for line in puzzle_input:
        if not reached_middle:
            if line == '' or line is None:
                reached_middle = True
            else:
                id_ranges.append(line)
        else:
            ids_to_test.append(line)

    return id_ranges, ids_to_test

def check_total_fresh_ingredients(valid_ids: list[tuple[int,int]], test_ids: list[str]) -> int:
    total_fresh = 0

    for id in test_ids:
        for id_bounds in valid_ids:
            if int(id) >= id_bounds[0] and int(id) <= id_bounds[1]:
                total_fresh += 1
                break

    return total_fresh

def check_total_of_valid_fresh_ingredients(valid_ids: list[tuple[int,int]]):
    total_fresh = 0

    

def part1(puzzle_input: list[str]):

    id_ranges, ids_to_test = split_puzzle_input(puzzle_input)

    id_set = build_list_of_bounds(id_ranges)
    print(check_total_fresh_ingredients(id_set, ids_to_test))


if __name__ == "__main__":

    test_path = '/Users/nithinanand/Documents/study/advent_of_code/src/five/test_input.txt'
    input_path = '/Users/nithinanand/Documents/study/advent_of_code/src/five/input.txt'


    test_data = read_list_input(test_path)
    real_data = read_list_input(input_path)

    part1(test_data)
    part1(real_data)

