##Breadth First Search Algorithm
from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def bfs(self, root):
        visited = set()
        q = deque()
        pointer = root
        visited.add(root)
        print(root, end=" ")
        q.append(root)
        while q:
            pointer = q[0]
            all_adjacent_visited = True
            for neighbor in self.adj_list.get(pointer, []):
                if neighbor not in visited:
                    all_adjacent_visited = False
                    q.append(neighbor)
                    visited.add(neighbor)
                    print(neighbor, end=" ")
            q.popleft()
            if all_adjacent_visited and len(q) > 0:
                pointer = q[0]
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
print("BFS traversal starting from node 1:")
g.bfs(1)