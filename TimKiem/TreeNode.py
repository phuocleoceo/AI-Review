class Tree:

    def __init__(self, data, goal_cost=100000):

        self.data = data # label

        self.goal_cost = goal_cost # h(n)

        self.children = []

        self.parent = None

    def add_child(self, child):

        child.parent = self

        self.children.append(child)

    def get_data(self):

        return self.data

    def get_children(self):

        return self.children

    def get_parent(self):

        return self.parent

    def __lt__(self, other):

        return self.goal_cost < other.goal_cost