from pprint import pp
import re


class NodeType:
    DIR = "DIR"
    FILE = "FILE"

class Node:
    def __init__(self, name: str, type: str, parrent: "Node" = None, size: int = None):
        self.parent: "Node" = parrent
        self.name: str = name
        self.size: int = size
        self.childrens: list["Node"] = []
        self.type: str = type

    def add_dir(self, name: str):
        self.childrens.append(Node(name, NodeType.DIR, self))

    def add_file(self, name: str, size: int):
        self.childrens.append(Node(name, NodeType.FILE, self, size))

    def get_dir(self, name: str) -> "Node":
        for node in self.childrens:
            if node.name == name:
                return node
        raise Exception("Dir not found in")

    def tree_print(self, tab_count: int = 0, last: bool = False):
        if tab_count != 0:
            print("│  " * (tab_count), sep="", end="")
            if last:
                print("└──", sep="", end="")
            else:
                print("├──", sep="", end="")
        print(f"{self.type} {self.name} {self.get_size()}")

        for i, child in enumerate(self.childrens):
            is_last = len(self.childrens) - 1 == i
            child.tree_print(tab_count + 1, is_last)

    def is_dir(self) -> bool:
        return self.type == NodeType.DIR

    def is_file(self) -> bool:
        return self.type == NodeType.FILE

    def get_size(self) -> int:
        if self.is_file():
            return self.size

        result_size = 0
        for child in self.childrens:
            result_size += child.get_size()

        return result_size

DataType = Node

def solution_part1(tree: DataType) -> int:
    result = 0
    
    if tree.get_size() <= 100000:
        result = tree.get_size()

    for child in tree.childrens:
        if child.is_file():
            continue
        
        result += solution_part1(child)
    return result

def solution_part2(tree: DataType) -> int:
    result = []
    
    if tree.get_size() >= 8381165:
        result.append(tree.get_size())

    for child in tree.childrens:
        if child.is_file():
            continue

        child_sizes = solution_part2(child)
        result.extend(child_sizes)

    return result

def parce_input(file_name: str) -> DataType:
    with open(file_name, "r") as f:
        rows = f.readlines()

        root = Node("/", NodeType.DIR)
        current_ptr = None

        for row in rows:
            words = row.strip().split()

            match words:
                case ["$", "cd", "/"]:
                    current_ptr = root
                case ["$", "cd", ".."]:
                    current_ptr = current_ptr.parent
                case ["$", "cd", name]:
                    current_ptr = current_ptr.get_dir(name)
                case ["$", "ls"]:
                    pass
                case ["dir", name]:
                    current_ptr.add_dir(name)
                case [size, name]:
                    current_ptr.add_file(name, int(size))

        return root

if __name__ == '__main__':
    file_name = "input"
    tree = parce_input(file_name)
    tree.tree_print()
    result = solution_part1(tree)
    print(result)
    results = solution_part2(tree)
    print(min(results))