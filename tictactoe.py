import random

PLACEMENTS = {
    "1,1": 23,
    "1,2": 29,
    "1,3": 35,
    "2,1": 102,
    "2,2": 108,
    "2,3": 114,
    "3,1": 181,
    "3,2": 187,
    "3,3": 193,
}


def create_board() -> str:
    a = " _____" * 3
    b = "     ".join(" || ")
    board = "\n".join(
        (
            b,
            b,
            b,
            a,
            b,
            b,
            b,
            a,
            b,
            b,
            b,
        )
    )
    print(board)
    return board


def make_move(board):
    choice = ""
    temp = 0
    boardlist = list(board)
    while True:
        row = input("\nPick a row:\t")
        column = input("Pick a column:\t")
        if row and column:
            if row not in "123" or column not in "123":
                print("Please enter valid numbers between 1-3 for row and column.")
                continue
            else:
                break
        choice = ",".join((row, column))
        temp = PLACEMENTS.get(choice)
        if boardlist[temp] != " ":
            print("Place already occupied, please pick again")
        else:
            break
    boardlist[temp] = "X"
    board = "".join(boardlist)
    print(board)


def full_board(boardlist) -> bool:
    return all(boardlist[place] != " " for place in PLACEMENTS.values())


def is_winner(board) -> bool:
    sequences = [
        [23, 29, 35],
        [102, 108, 114],
        [181, 187, 193],
        [23, 102, 181],
        [29, 108, 187],
        [35, 114, 193],
        [23, 108, 193],
        [35, 108, 181],
    ]
    for seq in sequences:
        if board[seq[0]] == board[seq[1]] == board[seq[2]] != " ":
            return True
    return False


def start_game():
    board = create_board()
    for i in range(10):
        board = make_move(board)
        # print(is_winner(board))


start_game()
