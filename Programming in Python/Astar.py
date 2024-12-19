##A* Search Algorithm
import heapq
class Node:
    def __init__(self, name, cost, heuristic):
        self.name = name
        self.cost = cost
        self.heuristic = heuristic
        self.f = cost + heuristic
    def __lt__(self, other):
        return self.f < other.f
def a_star(graph, heuristics, start, goal):
    open_set = [Node(start, 0, heuristics[start])]
    heapq.heapify(open_set)
    came_from = {}
    g_score = {start: 0}
    print(f"Start searching from {start} to {goal}...\n")
    while open_set:
        current = heapq.heappop(open_set)
        print(f"Visiting {current.name} (f = {current.f}, g = {current.cost}, h = {current.heuristic})")
        if current.name == goal:
            print(f"Goal {goal} reached!\n")
            return reconstruct_path(came_from, goal)
        for neighbor, cost in graph[current.name].items():
            tentative_g_score = g_score[current.name] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(open_set, Node(neighbor, tentative_g_score, heuristics[neighbor]))
                came_from[neighbor] = current.name
                print(f"  -> Adding {neighbor} (f = {f_score}, g = {tentative_g_score}, h = {heuristics[neighbor]})")
    return None
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 2, 'C': 1}
}
heuristics = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 0
}
path = a_star(graph, heuristics, 'A', 'D')
print("Path found:", path)