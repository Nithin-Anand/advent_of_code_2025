
def split_ranges(puzzle_input: str) -> list[str]:
    return puzzle_input.split(",")

def check_both_halves_are_identical(n: int) -> bool:
    string_rep = str(n)
    if len(string_rep) % 2 == 1:
        return False
    else:
        midpoint = len(string_rep) // 2
        first_half = string_rep[:midpoint]
        second_half = string_rep[midpoint:]
        if first_half == second_half:
            return True
        else:
            return False

def check_repeating_solution(string_n: str, segments) -> bool:
    if len(string_n) % segments != 0:
        return False
    else:
        segment_size = len(string_n) // segments
        slices = range(0, len(string_n) + 1, segment_size)

        for i in range(1, segments):
            first_slice = string_n[slices[i-1]:slices[i]]
            second_slice = string_n[slices[i]:slices[i+1]]

            if first_slice == second_slice:
                continue
            else:
                return False
    return True




        
            
    return True

def get_numbers_in_range(range_str: str) -> list[int]:
    nums = range_str.split("-")
    i = int(nums[0])
    j = int(nums[1])

    return range(i, j+1)

def part1(ranges):
    total = 0

    for range in ranges:
        ids = get_numbers_in_range(range)
        for id in ids:
            if check_both_halves_are_identical(id):
                total += id

    print(total)

def part2(ranges):
    total = 0

    for vals in ranges:
        ids = get_numbers_in_range(vals)
        ids = [str(id) for id in ids]
        for id in ids:
            for segment in range(2, len(id) + 1):
                if check_repeating_solution(id, segments=segment):
                    total += int(id)
                    break
                    

    print(total)



def main(input: str):
    ranges = split_ranges(input)

    part1(ranges=ranges)
    part2(ranges=ranges)

    
if __name__ == "__main__":

    # test = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

    input = "19391-47353,9354357-9434558,4646427538-4646497433,273-830,612658-674925,6639011-6699773,4426384-4463095,527495356-527575097,22323258-22422396,412175-431622,492524-611114,77-122,992964846-993029776,165081-338962,925961-994113,7967153617-7967231799,71518058-71542434,64164836-64292066,4495586-4655083,2-17,432139-454960,4645-14066,6073872-6232058,9999984021-10000017929,704216-909374,48425929-48543963,52767-94156,26-76,1252-3919,123-228"
    main(input)

