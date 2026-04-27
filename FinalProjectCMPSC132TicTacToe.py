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