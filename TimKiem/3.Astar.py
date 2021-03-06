from typing_extensions import Self
from typing import List, Tuple
import heapq


class Node:
    def __init__(self, label: str, goal_cost: int) -> None:
        self.label = label
        self.cost = 10000
        self.goal_cost = goal_cost
        self.parent = []
        self.child = []

    # Equal dùng cho heapq
    def __eq__(self, other: Self) -> bool:
        return self.label == other.label

    # Less than dùng cho heapq
    def __lt__(self, other: Self) -> bool:
        return self.cost < other.cost

    def get_neighbors(self) -> List[Self]:
        return self.child+self.parent


class Edge:
    def __init__(self, start_node: Node, end_node: Node, cost: int) -> None:
        self.start_node = start_node
        self.end_node = end_node
        self.cost = cost


class Tree:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []

    def add_node(self, data: Node) -> None:
        self.nodes.append(data)

    def add_nodes(self, data: List[Node]) -> None:
        self.nodes += data

    def index_of(self, n: str) -> int:
        # Tìm index của 1 node(label) ở trong mảng nodes
        for i in range(len(self.nodes)):
            if self.nodes[i].label == n:
                return i
        return -1

    def add_edge(self, data: Tuple[str, str, int]) -> None:
        # Tuple nhận vào chứa nhãn của start_node và end_node
        # Dựa vào nhãn tìm được Node trong cây
        start_lbl, end_lbl, cost = data
        start_node = self.nodes[self.index_of(start_lbl)]
        end_node = self.nodes[self.index_of(end_lbl)]
        # Tạo quan hệ cho start_node và end_node
        start_node.child.append(end_node)
        end_node.parent.append(start_node)
        # Thêm cạnh
        self.edges.append(Edge(start_node, end_node, cost))

    def add_edges(self, list_edges: List[Tuple[str, str, int]]) -> None:
        for e in list_edges:
            self.add_edge(e)

    def get_edge(self, start_node: Node, end_node: Node):
        # self.edges là mảng các tuple dạng (Node,Node,int)
        # Ta lấy cạnh đầu tiên tìm được
        for e in self.edges:
            if e.start_node == start_node and e.end_node == end_node:
                return e
        return None


def update_cost(tree: Tree, current_node: Node, prev_node: Node) -> None:
    # Cạnh nối 2 node current (neighbors) và prev (state đang xét)
    prev_to_current_edge: Edge = tree.get_edge(prev_node, current_node)
    if prev_to_current_edge is not None:
        # Cost từ prev đến current bằng Ước lượng đến đích của prev(state)
        # cộng với cost của cạnh prev_to_current
        prev_to_current_cost = prev_node.cost+prev_to_current_edge.cost
        # Nếu cost ước lượng đích của current dài hơn prev_current cost thì gán lại
        if current_node.cost > prev_to_current_cost:
            current_node.cost = prev_to_current_cost


def A_Star(tree: Tree, inititalState: Node, goal: Node) -> List[Node]:
    frontier = [inititalState]
    # Biến list thành heap
    heapq.heapify(frontier)
    explored = []
    while len(frontier) > 0:
        # Lấy ra item nhỏ nhất trong heap
        state: Node = heapq.heappop(frontier)
        explored.append(state)
        if goal == state:
            return explored
        for child in state.get_neighbors():
            update_cost(tree, child, state)
            # Dựa vào label, nếu child chưa xét thì ta thêm nó vào frontier
            if child.label not in set(node.label for node in frontier+explored):
                heapq.heappush(frontier, child)
    return False


if __name__ == "__main__":
    V = [("S", 12), ("A", 7), ("B", 8), ("C", 9), ("D", 6), ("E", 5),
         ("F", 4), ("G", 10), ("H", 10), ("K", 3), ("M", 9), ("N", 10), ("I", 6),
         ("J", 0), ("L", 0), ("Z", 8)]
    E = [("S", "A", 5), ("S", "B", 6), ("S", "C", 5),
         ("A", "D", 6), ("A", "E", 7),
         ("B", "F", 3), ("B", "G", 4),
         ("C", "H", 6), ("C", "K", 4),
         ("D", "M", 5), ("D", "N", 8),
         ("E", "I", 8),
         ("F", "J", 4), ("F", "L", 4),
         ("K", "Z", 2)]

    tree = Tree()
    for v in V:
        tree.add_node(Node(v[0], v[1]))
    for e in E:
        tree.add_edge((e[0], e[1], e[2]))

    # Gốc -> chính nó thì có cost bằng 0
    tree.nodes[0].cost = 0

    # Index cac dinh co trong so bang 0
    V_0 = []
    for i in range(len(V)):
        if V[i][1] == 0:
            V_0.append(i)
    print(">> Các đỉnh có trọng sốt trên đỉnh bằng 0 là : ", end="")
    for v0 in V_0:
        print(V[v0][0], end=", ")

    print("")
    print(">> Giải thuật A* : ")

    for v0 in V_0:
        print(f"- Thứ tự khám phá từ S đến {V[v0][0]} : ")
        result = A_Star(tree, tree.nodes[0], tree.nodes[v0])
        if result:
            s = "Explored : "
            for i in result:
                s += i.label + " "
                print(s)
        else:
            print("404 Not Found")
