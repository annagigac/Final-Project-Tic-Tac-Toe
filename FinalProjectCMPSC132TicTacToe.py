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

def main():
    board = create_board()
    current_player = "X"
    game_over = False
    while not game_over:
        print_board(board)
        get_valid_move(board, current_player)
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            if current_player == "X":  #alternate turns
                current_player = "O"
            else:
                current_player = "X"
main()