"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lubomír Vaňura
email: Lubomir.2@seznam.cz
"""

splitter = "=" * 40
splitter2 = "-" *40

mesh = ("+---+---+---+")

def print_board(board):
    print("\n+---+---+---+")
    for i in range(3):
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
        print(mesh)

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    else: False

def check_full(board):
    return all(spot != ' ' for spot in board)

def get_move(player, board):
    while True:
        move_str = input(f"Player {player} | Please enter your move number: ")
        if move_str.isdigit():
            move = int(move_str)
            if move < 1 or move > 9:
                print("Invalid number! Please choose a number between 1 and 9.")
            elif board[move - 1] != ' ':
                print("This position is already occupied! Please choose another.")
            else:
                return move - 1
        else:
            print("Invalid input! Please enter a number between 1 and 9.")

def main():
    print("Welcome to Tic Tac Toe")
    print(splitter)
    print("GAME RULES:")
    print("Each player can place one mark (or stone) per turn on the 3x3 grid.")
    print("The WINNER is who succeeds in placing three of their marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print(splitter)
    print("Let's start the game")
    print(splitter2)
    
    board = [' '] * 9
    
    # definování 2 hráčů, kde je pouze 0 a X
    players = ['O', 'X']
    turn = 0  

    # herní smyčka
    while True:
        print_board(board)
        current_player = players[turn % 2]
        move = get_move(current_player, board)
        board[move] = current_player
        
        # Kontrola jednoho z výherců
        if check_winner(board, current_player):
            print_board(board)
            print(splitter)
            print(f"Congratulations, the player {current_player} WON!")
            break
        
        # Kontrola remízy
        if check_full(board):
            print_board(board)
            print(splitter)
            print("It's a DRAW!")
            break
        
        # Přepnutí hráče
        turn += 1

if __name__ == "__main__":
    main()