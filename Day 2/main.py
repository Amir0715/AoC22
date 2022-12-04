DataType = list[tuple[str, str]]

# Комбинации исхода
# ROCK - A, X
# PAPER - B, Y
# SCISSORS - C, Z
rules_part_1 = {
    "A": {
        "Y": 6,
        "Z": 0,
        "X": 3,
    },
    "B": {
        "Y": 3,
        "Z": 6,
        "X": 0,
    },
    "C": {
        "Y": 0,
        "Z": 3,
        "X": 6,
    }
}

score_by_hand_part_1 = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3 
}

# X - lose
# Y - draw
# Z - win
rules_part_2 = {
    "A": {
        "Y": "ROCK",
        "Z": "PAPER",
        "X": "SCISSORS",
    },
    "B": {
        "Y": "PAPER",
        "Z": "SCISSORS",
        "X": "ROCK",
    },
    "C": {
        "Y": "SCISSORS",
        "Z": "ROCK",
        "X": "PAPER",
    }
}

rules_ends_part_2 = {
    "Y": 3,
    "X": 0,
    "Z": 6,
}

score_by_hand_part_2 = {
    "ROCK" : 1,
    "PAPER" : 2,
    "SCISSORS" : 3 
}

def solution_part1(data: DataType) -> int:
    return sum(map(lambda x: rules_part_1[x[0]][x[1]] + score_by_hand_part_1[x[1]], data))

def solution_part2(data: DataType) -> int:
    return sum(map(lambda x: score_by_hand_part_2[rules_part_2[x[0]][x[1]]] + rules_ends_part_2[x[1]], data))

def parce_input(file_name: str) -> DataType:
    data = []
    with open(file_name, "r") as f:
        data = list(map(lambda x: tuple(x.strip().split(" ")), f.readlines()))
    return data

if __name__ == '__main__':
    file_name = "input"
    data = parce_input(file_name)
    # print(data)
    result = solution_part1(data)
    print(result)
    result = solution_part2(data)
    print(result)