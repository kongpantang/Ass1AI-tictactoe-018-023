import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([s == player for s in row]):
            return True
    for col in range(3):
        if all([row[col] == player for row in board]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if not get_empty_cells(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for cell in get_empty_cells(board):
            board[cell[0]][cell[1]] = "O"
            eval = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in get_empty_cells(board):
            board[cell[0]][cell[1]] = "X"
            eval = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    move = None
    for cell in get_empty_cells(board):
        board[cell[0]][cell[1]] = "O"
        move_val = minimax(board, 0, False)
        board[cell[0]][cell[1]] = " "
        if move_val > best_val:
            best_val = move_val
            move = cell
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        if check_winner(board, "X"):
            print("You win!")
            break
        elif check_winner(board, "O"):
            print("AI wins!")
            break
        elif not get_empty_cells(board):
            print("It's a tie!")
            break
        
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != " ":
            print("Cell already occupied! Try again.")
            continue
        board[row][col] = "X"
        
        if get_empty_cells(board):
            ai_move = best_move(board)
            board[ai_move[0]][ai_move[1]] = "O"

if __name__ == "__main__":
    play_game()
