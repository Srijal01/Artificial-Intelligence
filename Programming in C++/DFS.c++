//Program to implement Depth First Search Algorithm.
#include <iostream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
class Graph 
{
public:
    unordered_map<int, vector<int>> adjList;
    void addEdge(int u, int v) 
    {
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }
    void dfs(int root) 
    {
        unordered_set<int> visited;
        stack<int> s;
        s.push(root);
        visited.insert(root);
        cout << root << " ";
        while (!s.empty()) 
        {
            int top = s.top();
            bool allAdjacentVisited = true;
            for (int neighbor : adjList[top]) 
            {
                if (visited.find(neighbor) == visited.end()) 
                { 
                    s.push(neighbor);
                    visited.insert(neighbor);
                    cout << neighbor << " ";
                    allAdjacentVisited = false;
                    break;
                }
            }
            if (allAdjacentVisited)
            {
                s.pop();
            }
        }
    }
};
int main() 
{
    Graph g;
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(3, 5);
    cout << "DFS traversal starting from node 1:" << endl;
    g.dfs(1);
    return 0;
}