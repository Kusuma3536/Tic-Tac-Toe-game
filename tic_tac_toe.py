def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if "-" in row:
            return False
    return True

def play_game():
    # Initialize the board
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        # Print the board
        print_board(board)
        
        # Get the current player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the move is valid
        if board[row][col] == "-":
            # Make the move
            board[row][col] = current_player
            
            # Check if the current player wins
            winner = check_winner(board)
            if winner:
                print("Player", winner, "wins!")
                game_over = True
            elif is_board_full(board):
                print("It's a tie!")
                game_over = True
            else:
                # Switch to the other player
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")

# Start the game
play_game()
