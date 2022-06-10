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
    nodeS = Node('S')
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')
    nodeF = Node('F')
    nodeG = Node('G')
    nodeH = Node('H')
    nodeS.add_children([nodeA, nodeB, nodeC])
    nodeA.add_children([nodeD])
    nodeB.add_children([nodeD, nodeE, nodeG])
    nodeC.add_children([nodeE])
    nodeD.add_children([nodeF])
    nodeE.add_children([nodeH, nodeF])
    nodeF.add_children([nodeG])
    nodeH.add_children([nodeG])

    Solve("BFS", nodeS, "G")
    print("------------------------------------------------")
    Solve("DFS", nodeS, "G")
