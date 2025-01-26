"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lubomír Vaňura
email: Lubomir.2@seznam.cz
"""

splitter = "=" * 40
splitter2 = "-" *40

def main():
    print("Welcome to Tic Tac Toe ")
    print(splitter)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)") 
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print(splitter)
    print("Let's start the game")
    print(splitter2)

mesh = ("+---+---+---+")

def play_area(board):
    print(mesh)
    for step in range(3):
        print(f"| {board[step*3]} | {board[step*3+1]} | {board[step*3+2]} |")  
        print(mesh)  

if __name__ == "__main__":
    main()

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    play_area(board) 

print(splitter)


def player_zone(board, player):
    win_combination: {
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]  
    }

    for combination in win_combination:
        while True:
            if all(board[z] == player for z in combination):
                return True
            else: False


      