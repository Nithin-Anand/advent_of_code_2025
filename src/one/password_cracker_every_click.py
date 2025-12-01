class PasswordCracker:

    def __init__(self):
        self.current_zeros = 0

    def crack_password_every_click(self, puzzle_input: list[str]) -> 0:
        current_position = 50
        self.current_zeros = 0

        for line in puzzle_input:
            magnitude = int(line[1:])
            next_position = current_position
            if line.startswith('L'):
                next_position -= magnitude
                if current_position > 0 and next_position < 0:
                    self.current_zeros += 1
                current_position = self.manage_underflow(next_position)
            else:
                next_position += magnitude
                if current_position < 0 and next_position > 0:
                    self.current_zeros += 1
                current_position = self.manage_overflow(next_position)
            
            if abs(next_position) > 99:
                self.current_zeros += (abs(next_position) // 100)
            elif current_position == 0:
                self.current_zeros += 1




        
    def manage_overflow(self, position: int) -> int:
       return position % 100

    def manage_underflow(self, position: int) -> int:
        if position < 0:
            # self.current_zeros += (abs(position) // 100)
            return (100 - abs(position)) % 100
        else:
            return position
    
def read_input(input_path: str) -> list[str]:
    with open(input_path, "r") as f:
        return f.readlines()
    
if __name__ == "__main__":
    input_path = "/Users/nithinanand/Documents/study/advent_of_code/src/one/input.txt"
    # input_path = "/Users/nithinanand/Documents/study/advent_of_code/tests/1/bigger_swing_test.txt"

    
    cracker = PasswordCracker()

    (cracker.crack_password_every_click(read_input(input_path)))
    print(cracker.current_zeros)