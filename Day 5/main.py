from pprint import pp

DataType = list[tuple[int, int, int]]
STACKS_OF_CRATES = [
    ['R', 'N', 'P', 'G'],
    ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'],
    ['T', 'D', 'B', 'M', 'N', 'L'],
    ['R', 'V', 'P', 'S', 'B'],
    ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'],
    ['W', 'Q', 'S', 'C', 'D', 'B', 'J'],
    ['F', 'Q', 'L'],
    ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
    ['L', 'P', 'B', 'V', 'M', 'J', 'F']
]

def solution_part1(data: DataType):
    for move, _from, _to in data:
        _from_index = _from - 1
        _to_index = _to - 1
        for _ in range(move):
            crate = STACKS_OF_CRATES[_from_index].pop()
            STACKS_OF_CRATES[_to_index].append(crate)

def solution_part2(data: DataType) -> int:
    for move, _from, _to in data:
        _from_index = _from - 1
        _to_index = _to - 1
        stack_len = len(STACKS_OF_CRATES[_from_index])
        crates = STACKS_OF_CRATES[_from_index][stack_len - move:]
        for _ in range(move):
            STACKS_OF_CRATES[_from_index].pop()
        STACKS_OF_CRATES[_to_index].extend(crates)

def parce_input(file_name: str) -> DataType:
    with open(file_name, "r") as f:
        return list(map(lambda row: tuple(map(int, row.strip().split(","))), f.readlines()))

if __name__ == '__main__':
    file_name = "input"
    data = parce_input(file_name)
    # pp(data)
    # solution_part1(data)
    # pp("".join(map(lambda x: x[-1], STACKS_OF_CRATES)))
    solution_part2(data)
    pp("".join(map(lambda x: x[-1], STACKS_OF_CRATES)))