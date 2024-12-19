##Depth First Search Algorithm
from collections import defaultdict
class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def dfs(self, root):
        visited = set()
        stack = []
        stack.append(root)
        visited.add(root)
        print(root, end=" ")
        while stack:
            top = stack[-1]
            all_adjacent_visited = True
            for neighbor in self.adj_list.get(top, []):
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    print(neighbor, end=" ")
                    all_adjacent_visited = False
                    break
            if all_adjacent_visited:
                stack.pop()
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
print("DFS traversal starting from node 1:")
g.dfs(1)