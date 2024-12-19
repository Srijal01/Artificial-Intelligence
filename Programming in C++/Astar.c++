//Program to implement A* Search Algorithm.
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <functional>
#include <algorithm> 
using namespace std;
struct Node 
{
    string name;
    int cost;
    int heuristic;
    int f;
    Node(string n, int c, int h) : name(n), cost(c), heuristic(h), f(c + h) {}
    bool operator<(const Node& other) const 
    {
        return f > other.f;
    }
};
vector<string> reconstruct_path(unordered_map<string, string>& came_from, string current) 
{
    vector<string> path;
    while (came_from.find(current) != came_from.end()) 
    {
        path.push_back(current);
        current = came_from[current];
    }
    path.push_back(current);
    reverse(path.begin(), path.end());
    return path;
}
vector<string> a_star(unordered_map<string, unordered_map<string, int>>& graph, 
                       unordered_map<string, int>& heuristics, string start, string goal) 
                       {
    priority_queue<Node> open_set;
    unordered_map<string, string> came_from;
    unordered_map<string, int> g_score;
    g_score[start] = 0;
    open_set.push(Node(start, 0, heuristics[start]));
    cout << "Start searching from " << start << " to " << goal << "...\n\n";
    while (!open_set.empty()) 
    {
        Node current = open_set.top();
        open_set.pop();
        cout << "Visiting " << current.name << " (f = " << current.f 
             << ", g = " << current.cost << ", h = " << current.heuristic << ")\n";
        if (current.name == goal) 
        {
            cout << "Goal " << goal << " reached!\n\n";
            return reconstruct_path(came_from, goal);
        }
        for (const auto& neighbor : graph[current.name]) 
        {
            string next_node = neighbor.first;
            int cost = neighbor.second;
            int tentative_g_score = g_score[current.name] + cost;
            if (g_score.find(next_node) == g_score.end() || tentative_g_score < g_score[next_node]) 
            {
                g_score[next_node] = tentative_g_score;
                int f_score = tentative_g_score + heuristics[next_node];
                open_set.push(Node(next_node, tentative_g_score, heuristics[next_node]));
                came_from[next_node] = current.name;
                cout << "  -> Adding " << next_node << " (f = " << f_score 
                     << ", g = " << tentative_g_score << ", h = " << heuristics[next_node] << ")\n";
            }
        }
    }
    return {};
}
int main() 
{
    unordered_map<string, unordered_map<string, int>> graph = {
        {"A", {{"B", 1}, {"C", 4}}},
        {"B", {{"A", 1}, {"D", 2}}},
        {"C", {{"A", 4}, {"D", 1}}},
        {"D", {{"B", 2}, {"C", 1}}}
    };
    unordered_map<string, int> heuristics = {
        {"A", 5},
        {"B", 3},
        {"C", 2},
        {"D", 0}
    };
    vector<string> path = a_star(graph, heuristics, "A", "D");
    if (!path.empty()) 
    {
        cout << "Path found: ";
        for (const string& node : path) 
        {
            cout << node << " ";
        }
        cout << endl;
    } 
    else 
    {
        cout << "No path found from A to D.\n";
    }
    return 0;
}