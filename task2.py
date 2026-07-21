import random

board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

while True:
    show()
    p = int(input("Enter position (1-9): ")) - 1

    if board[p] != " ":
        print("Position already filled!")
        continue

    board[p] = "X"

    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]

    if any(board[a] == board[b] == board[c] == "X" for a,b,c in wins):
        show()
        print("You Win!")
        break

    if " " not in board:
        show()
        print("Draw!")
        break

    ai = random.choice([i for i in range(9) if board[i] == " "])
    board[ai] = "O"

    if any(board[a] == board[b] == board[c] == "O" for a,b,c in wins):
        show()
        print("AI Wins!")
        break