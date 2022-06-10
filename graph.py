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

graph = {}
for node in V:
    temp = []
    for edge in E:
        if edge[0] == node[0]:
            temp.append((edge[1], edge[2]))
    graph[node] = temp
print(graph)