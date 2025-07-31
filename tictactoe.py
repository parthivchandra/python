board = [ ' 'for _ in range(9) ]
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
def check_winner(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
def play_game():
    current_player = 'X'
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = current_player
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")
    print_board()
    print("It's a tie!")

    play_game()

