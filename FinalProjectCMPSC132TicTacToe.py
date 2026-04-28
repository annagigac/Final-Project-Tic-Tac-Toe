def create_board():  #create 3x3 board -- list of lists
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return board

def print_board(board): #display board -- print_board(board)
    print()
    print("  0   1   2")
    for i in range(3):
        print(i, board[i][0], "|", board[i][1], "|", board[i][2])
        if i < 2:
            print(" ---+---+---")
    print()

def get_valid_move(board, player): #row and col player input w/ invalid moves ex. 0-2
    valid = False
    while not valid:
        try:
            row = int(input(f"Player {player}, enter row 0-2: "))
            col = int(input(f"Player {player}, enter column 0-2: "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("That spot is outside the board. Try again.")
            elif board[row][col] != " ":
                print("That spot is already taken. Try again.")
            else:
                board[row][col] = player
                valid = True   
        except ValueError:
            print("Please enter numbers only.")

def check_winner(board, player): #detect winner -- check_winner(board, player)
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_draw(board): #detect draw -- is_draw(board)
    for row in board:
        for spot in row:
            if spot == " ":
                return False
    return True

def play_again():
    while True:
        answer = input("Would you like to play again? (yes/no): ").lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please type 'yes' or 'no'.")


def print_score(x_score, o_score, draws):
    print("\nScoreboard")
    print(f"Player X wins: {x_score}")
    print(f"Player O wins: {o_score}")
    print(f"Draws: {draws}\n")

def main():
    x_score = 0
    o_score = 0
    draws = 0
    playing = True
    while playing:
        board = create_board()
        current_player = "X"
        game_over = False
        while not game_over:
            print_board(board)
            get_valid_move(board, current_player)
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                if current_player == "X":
                    x_score += 1
                else:
                    o_score += 1
                game_over = True
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                draws += 1
                game_over = True
            else:
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
        print_score(x_score, o_score, draws)
        playing = play_again()
    print("Thanks for playing!")
main ()