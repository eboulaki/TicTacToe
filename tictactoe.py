import random

PLACEMENTS = {
    "1,1": 23,
    "1,2": 29,
    "1,3": 35,
    "2,1": 102,
    "2,2": 108,
    "2,3": 114,
    "3,1": 181,
    "3,1": 187,
    "3,3": 193,
}


class Tic_Tac_toe:
    def __init__(self) -> None:
        print("Start Game!\n")
        self.board = self.create_board()
        self.player1, self.player2 = self.create_player()
        print(self.player1, self.player2)

    def create_board(self) -> str:
        a = " ___" * 3
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

    def create_player(self):
        player_num = [1, 2]
        irlPlayer = random.choice(player_num)
        player_num.remove(irlPlayer)
        computer = player_num[0]
        print(f"You are player No {irlPlayer}. And computer is player No {computer}")
        while True:
            playerMark = input("Choose your marker (O, X): ").upper()
            if playerMark in "XO":
                if playerMark == "X":
                    computerMark = "O"
                else:
                    computerMark = "X"
                break
            else:
                print("Please enter a valid marker.")
        print("Computer plays as: ", computerMark)
        players = [
            {"playerName": irlPlayer, "mark": playerMark},
            {"playerName": computer, "mark": computerMark},
        ]
        return players[0], players[1]

    def make_move(self):
        self.board
        choice = ""
        boardlist = list(board)
        row = input("\nPick a row:\t")
        column = input("Pick a column:\t")
        choice = ",".join((row, column))
        temp = PLACEMENTS.get(choice)
        boardlist[temp] = "X"
        board = "".join(boardlist)
        print(board)


def is_winner(self) -> bool:
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


game = Tic_Tac_toe()
