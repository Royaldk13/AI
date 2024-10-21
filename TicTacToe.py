# Define the Tic-Tac-Toe board
board = [' ' for _ in range(9)]  # Initially, the board is empty

def print_board():
    print("\n")
    for i in range(3):
        print(board[3*i] + ' | ' + board[3*i + 1] + ' | ' + board[3*i + 2])
        if i < 2:
            print('--|---|--')
    print("\n")

# Check if the game has a winner
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Check if there are any moves left
def is_moves_left():
    return ' ' in board

# Evaluate the board for Minimax
def evaluate():
    if check_winner('X'):
        return 10
    elif check_winner('O'):
        return -10
    else:
        return 0

# Minimax function
def minimax(is_maximizing):
    score = evaluate()

    if score == 10:  # X wins
        return score
    if score == -10:  # O wins
        return score
    if not is_moves_left():  # Tie
        return 0

    if is_maximizing:  # Maximizing player (X)
        best = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(False))
                board[i] = ' '  # Undo move
        return best
    else:  # Minimizing player (O)
        best = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(True))
                board[i] = ' '  # Undo move
        return best

# Find the best move for the maximizing player
def find_best_move():
    best_value = -1000
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_value = minimax(False)
            board[i] = ' '  # Undo move

            if move_value > best_value:
                best_move = i
                best_value = move_value

    return best_move

# Driver code to play against AI
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    while True:
        print_board()

        # Player O (human) makes a move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

        # Check if O has won
        if check_winner('O'):
            print_board()
            print("You win!")
            break

        # Check for tie
        if not is_moves_left():
            print_board()
            print("It's a tie!")
            break

        # AI (X) makes a move
        print("AI is making its move...")
        best_move = find_best_move()
        board[best_move] = 'X'

        # Check if X has won
        if check_winner('X'):
            print_board()
            print("AI wins!")
            break

        # Check for tie
        if not is_moves_left():
            print_board()
            print("It's a tie!")
            break