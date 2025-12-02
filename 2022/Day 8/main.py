from pprint import pp
import re


DataType = list[list[int]]

def is_edge(i, j, forest: DataType) -> bool:
    if (i == 0) or \
        (j == 0) or \
        (i == len(forest) - 1) or \
        (j == len(forest[0]) - 1):
        return True
        

def is_visible(i, j, forest: DataType) -> bool:
    value = forest[i][j]
    max_prev = max(forest[i][:j])
    if max_prev < value:
        return True

    max_next = max(forest[i][j + 1:])
    if max_next < value:
        return True

    return False

def T(forest: DataType) -> DataType:
    return [[forest[j][i] for j in range(len(forest))] for i in range(len(forest[0]))]

def solution_part1(forest: DataType) -> int:
    result = 0

    # массив индексов (i, j) которые не видны по горизонтали, 
    # необхожимо их проверить по вертикали что бы в этом удостовериться
    maybe_not_visible = []

    for i, row in enumerate(forest):
        for j, j_value in enumerate(row):
            if is_edge(i, j, forest):
                result += 1
                continue

            print(f"{i=}, {j=}, {j_value=}, {row=}, {is_visible(i, j, forest)}")
            if is_visible(i, j, forest):
                result += 1
            else:
                maybe_not_visible.append((i, j))
        print()

    # print(maybe_not_visible)
    forestT = T(forest)

    for j, i in maybe_not_visible:
        print(f"{i=}, {j=}, j_value={forestT[i][j]}, {forestT[i]}, {is_visible(i, j, forestT)}")
        if is_visible(i, j, forestT):
            result += 1

    return result

def get_scenic_score(i: int, j: int, forest: DataType) -> int:
    value = forest[i][j]

    prevs = []
    prevs_score = 0
    if j != 0:
        prevs = forest[i][:j][::-1]
        for prev_value in prevs:
            prevs_score += 1
            if value <= prev_value:
                break

    
    nexts = []
    nexts_score = 0
    if j != len(forest[i]) - 1:
        nexts = forest[i][j + 1:]
        for next_value in nexts:
            nexts_score += 1
            if value <= next_value:
                break
            

    forestT = T(forest)
    if value != forestT[j][i]:
        print("ЭЭ ты че-то не то делаешь")

    ups = []
    ups_score = 0
    if i != 0:
        ups = forestT[j][:i][::-1]
        for up_value in ups:
            ups_score += 1
            if value <= up_value: 
                break
                

    downs = []
    downs_score = 0
    if i != len(forestT[i]):
        downs = forestT[j][i + 1:]
        for downs_value in downs:
            downs_score += 1
            if value <= downs_value:
                break
                

    score = prevs_score * ups_score * downs_score * nexts_score
    # print()
    # print(f"[{i}][{j}]={value}, {prevs_score=}, {ups_score=}, {downs_score=}, {nexts_score=}, {score=}")
    # print(f"{prevs=}")
    # print(f"{ups=}")
    # print(f"{downs=}")
    # print(f"{nexts=}")
    return score


def solution_part2(forest: DataType) -> int:
    result = 0
    scenics = [[None for j in range(len(forest))] for i in range(len(forest))]

    for i, row in enumerate(forest):
        for j, j_value in enumerate(row):
            scenics[i][j] = get_scenic_score(i, j, forest)
        # print('-'*20)
        
    result = max(map(max, scenics))
    return result

def parce_input(file_name: str) -> DataType:
    data: DataType = []
    with open(file_name, "r") as f:
        rows = f.readlines()
        rows = map(lambda x: x.strip(), rows)
        for row in rows:
            data.append(list(map(int, row)))
    return data

if __name__ == '__main__':
    file_name = "input"
    forest = parce_input(file_name)
    # result = solution_part1(forest)
    # print(result)
    result = solution_part2(forest)
    print(result)