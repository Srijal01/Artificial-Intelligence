//Program to implement Breadth First Search Algorithm.
#include <iostream>
#include <queue>
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
    void bfs(int root)
    {
        unordered_set<int> visited;
        queue<int> q;
        int pointer = root;
        visited.insert(root);
        cout << root << " ";
        q.push(root);
        while (!q.empty()) 
        {
            pointer = q.front();
            q.pop();
            bool allAdjacentVisited = true;
            for (int neighbor : adjList[pointer]) 
            {
                if (visited.find(neighbor) == visited.end()) 
                {
                    allAdjacentVisited = false;
                    if (visited.find(neighbor) == visited.end()) 
                    {
                        q.push(neighbor);
                        visited.insert(neighbor);
                        cout << neighbor << " ";
                    }
                }
            }
            if (allAdjacentVisited && !q.empty())
            {
                pointer = q.front();
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
    cout << "BFS traversal starting from node 1:" << endl;
    g.bfs(1);
    return 0;
}