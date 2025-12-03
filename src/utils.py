def read_list_input(input_path: str, clean_input: bool = True) -> list[str]:
    with open(input_path, "r") as f:
        list_input = f.readlines()

    if clean_input:
        return [line.strip() for line in list_input]