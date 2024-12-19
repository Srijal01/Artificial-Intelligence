//Program to implement Min Max Algorithm.
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int minimax(int depth, bool isMaximizingPlayer, vector<int>& board) 
{
    if (depth == 0) 
    {
        cout << "Leaf node reached with value: " << board[0] << endl;
        return board[0];
    }
    if (isMaximizingPlayer) 
    {
        int best = -1000;
        for (int i = 0; i < board.size(); i++) 
        {
            cout << "Maximizing: Checking node " << i + 1 << " with value: " << board[i] << endl;
            int value = minimax(depth - 1, false, board);
            best = max(best, value);
        }
        cout << "Maximizing player: Best value so far: " << best << endl;
        return best;
    } 
    else 
    {
        int best = 1000;
        for (int i = 0; i < board.size(); i++) 
        {
            cout << "Minimizing: Checking node " << i + 1 << " with value: " << board[i] << endl;
            int value = minimax(depth - 1, true, board);
            best = min(best, value);
        }
        cout << "Minimizing player: Best value so far: " << best << endl;
        return best;
    }
}
int main() 
{
    vector<int> board = {3, 5, 2};
    int depth = 2;
    bool isMaximizingPlayer = true;
    cout << "Starting Minimax Algorithm..." << endl;
    int result = minimax(depth, isMaximizingPlayer, board);
    cout << "Best value found: " << result << endl;
    return 0;
}