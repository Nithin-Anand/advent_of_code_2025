from ..utils import read_list_input

def part1(puzzle_input: list[str], remove_rolls: bool = False):

    accessible_rolls = 0

    for row in range(0, len(puzzle_input)):

        for column in range(len(puzzle_input[row])):
            adjacent_rolls = 0

            if puzzle_input[row][column] == ".":
                continue
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    
                    if (i == 0 and j == 0):
                        continue
                    x = row + i
                    y = column + j
                    if check_for_roll(puzzle_input, x, y):
                        adjacent_rolls += 1
                    
            if adjacent_rolls < 4:
                accessible_rolls += 1
                if remove_rolls:
                    puzzle_input[row][column] = "x"

    return accessible_rolls, puzzle_input

def part2(puzzle_input: list[str]):

    for i in range(len(puzzle_input)):
        puzzle_input[i] = convert_string_to_char(puzzle_input[i])
        

    previous_accessible = -1

    while(True):
        accessible, puzzle_input = part1(puzzle_input, remove_rolls=True)
        if accessible == previous_accessible:
            return accessible
        else:
            previous_accessible = accessible

    

def convert_string_to_char(string):
    return list(string)

def check_for_roll(grid: list[str], x: int, y: int) -> bool:
    if x < 0 or y < 0:
        return False
    try:
        if grid[x][y] == "@":
            return True
        else:
            return False
    except IndexError:
        return False
    

if __name__ == "__main__":

    test_case_path = "/Users/nithinanand/Documents/study/advent_of_code/src/four/test.txt"

    test_input = read_list_input(test_case_path)

    real_case_path = "/Users/nithinanand/Documents/study/advent_of_code/src/four/input.txt"
    real_input = read_list_input(real_case_path)

    print(part1(test_input)[0])
    # print(part1(real_input))

    print(part2(test_input))

    print(part2(real_input))
