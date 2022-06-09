from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_children(self, listChildren: List):
        self.children += listChildren


def BFS(initState: Node, goal: str):
    frontier = [initState]
    explored = []
    while frontier:
        state = frontier.pop(0)
        explored.append(state)
        if state.name == goal:
            return explored
        for child in state.children:
            if child not in (explored and frontier):
                frontier.append(child)
    return False


def DFS(initState: Node, goal: str):
    frontier = [initState]
    explored = []
    while frontier:
        state = frontier.pop(-1)
        explored.append(state)
        if state.name == goal:
            return explored
        for child in state.children:
            if child not in (explored and frontier):
                frontier.append(child)
    return False


def Solve(option: str, initState: Node, goal: str):
    result = BFS(initState, goal) if option == "BFS" else DFS(initState, goal)
    print(f">> Result of {option} : ")
    if result:
        s = 'Explored : '
        for i in result:
            s += i.name + " "
            print(s)
    else:
        print('404 Not Found !')


if __name__ == "__main__":
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')
    nodeF = Node('F')
    nodeG = Node('G')
    nodeH = Node('H')
    nodeI = Node('I')
    nodeJ = Node('J')
    nodeK = Node('K')
    nodeL = Node('L')
    nodeM = Node('M')
    nodeN = Node('N')
    nodeO = Node('O')
    nodeA.add_children([nodeB, nodeC])
    nodeB.add_children([nodeD, nodeE])
    nodeC.add_children([nodeF, nodeG])
    nodeD.add_children([nodeH, nodeI])
    nodeE.add_children([nodeJ, nodeK])
    nodeF.add_children([nodeL, nodeM])
    nodeG.add_children([nodeN, nodeO])

    Solve("BFS", nodeA, "H")
    print("------------------------------------------------")
    Solve("DFS", nodeA, "H")
