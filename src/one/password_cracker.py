

def crack_password(puzzle_input: list[str]) -> 0:
    current_position = 50
    num_zero = 0

    for line in puzzle_input:
        magnitude = int(line[1:])
        if line.startswith('L'):
            current_position -= magnitude
            current_position = manage_underflow(current_position)
        else:
            current_position += magnitude
            current_position = manage_overflow(current_position)
        
        if current_position == 0:
            num_zero += 1


    return num_zero


def read_input(input_path: str) -> list[str]:
    with open(input_path, "r") as f:
        return f.readlines()
    
def manage_overflow(position: int) -> int:
    return position % 100

def manage_underflow(position: int) -> int:
    if position < 0:
        return (100 - abs(position)) % 100
    else:
        return position
    
if __name__ == "__main__":
    input_path = "/Users/nithinanand/Documents/study/advent_of_code/src/one/input.txt"
    
    input_code = read_input(input_path)

    print(crack_password(input_code))