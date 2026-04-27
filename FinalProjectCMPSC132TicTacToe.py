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