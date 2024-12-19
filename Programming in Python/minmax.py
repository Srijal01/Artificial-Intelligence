##MIN MAX Algorithm
def minimax(depth, is_maximizing_player, board):
    if depth == 0:
        print(f"Leaf node reached with value: {board[0]}")
        return board[0]
    if is_maximizing_player:
        best = -float('inf')
        for i in range(len(board)):
            print(f"Maximizing: Checking node {i + 1} with value: {board[i]}")
            value = minimax(depth - 1, False, board)
            best = max(best, value)
        print(f"Maximizing player: Best value so far: {best}")
        return best
    else:
        best = float('inf')
        for i in range(len(board)):
            print(f"Minimizing: Checking node {i + 1} with value: {board[i]}")
            value = minimax(depth - 1, True, board)
            best = min(best, value)
        print(f"Minimizing player: Best value so far: {best}")
        return best
board = [3, 5, 2]
depth = 2
is_maximizing_player = True
print("Starting Minimax Algorithm...")
result = minimax(depth, is_maximizing_player, board)
print(f"Best value found: {result}")