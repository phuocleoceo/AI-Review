import heapq

class node:
    def __init__(self, label, finalCost):
        self.label = label
        self.cost = 10000
        self.finalCost = finalCost
        self.saveCost = None
        self.parent = []
        self.child = []
    
    def getLabel(self):
        return self.label

    def neighbors(self):
        return self.child + self.parent

    def __lt__(self, other):
        if self.saveCost == 10000:
            return self.finalCost + self.cost < other.finalCost + other.cost
        else:
            return self.cost < other.cost
    

class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNodes(self, data):
        for node in data:
            self.nodes.append(node)

    def getLocation(self, node):
        for index, n in enumerate(self.nodes):
            if n.getLabel() == node.getLabel():
                return index
        return -1

    def addEdges(self, listEdges):
        for index in listEdges:
            locationStart = self.getLocation(node(index[0], None))
            locationEnd = self.getLocation(node(index[1], None))
            self.nodes[locationStart].child.append(self.nodes[locationEnd])
            self.nodes[locationEnd].parent.append(self.nodes[locationStart])
            self.edges.append((self.nodes[locationStart], self.nodes[locationEnd],index[2]))

    def getEgde(self, nodeStart, nodeEnd):
        try:
            return [edges for edges in self.edges if edges[0] == nodeStart and edges[1] == nodeEnd][0]
        except:
            return None


def updateCost(tree, nodeCurrent, nodePrevious):
    if tree.getEgde(nodePrevious, nodeCurrent) is not None:
        if nodeCurrent.cost > nodePrevious.cost + tree.getEgde(nodePrevious, nodeCurrent)[2]:
            nodeCurrent.cost = nodePrevious.cost + tree.getEgde(nodePrevious, nodeCurrent)[2]

def AStarSearch(tree, start, end):
    frontier = [start]
    heapq.heapify(frontier)
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        if state == end:
            return explored
        for child in state.neighbors():
            updateCost(tree, child, state)
            if child.getLabel() not in list(set(node.getLabel() for node in frontier + explored)):
                heapq.heappush(frontier, child)
    return False

if __name__ == "__main__":
    tree = Tree()
    tree.addNodes([
        node("A", 9),
        node("B", 4),
        node("C", 3),
        node("D", 7),
        node("E", 2),
        node("F", 6),
        node("G", 8),
        node("H", 9),
        node("I", 2),
        node("J", 1),
        node("K", 5),
        node("L", 3),
        node("M", 7),
        node("N", 1),
        node("O", 2)
    ])

    tree.addEdges([
        ("A", "B", 4),
        ("A", "C", 9),
        ("A", "D", 4),
        ("B", "E", 3),
        ("B", "F", 7),
        ("C", "G", 6),
        ("C", "H", 7),
        ("D", "I", 2),
        ("D", "J", 8),
        ("F", "K", 5),
        ("F", "L", 3),
        ("F", "M", 1),
        ("H", "N", 4),
        ("H", "O", 5),
    ])
    tree.nodes[0].cost = 0
    rs = AStarSearch(tree, tree.nodes[0], tree.nodes[10])
    if rs:
        s = "Explored: "
        for i in rs:
            s += i.label + " "
            print(s);
    else:
        print("Not Found")