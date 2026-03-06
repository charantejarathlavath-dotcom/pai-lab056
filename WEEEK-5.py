import math

board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == player:
            return True
    return False

def board_full():
    return ' ' not in board

def minimax(is_max):
    
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if board_full():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


# AI starts first
print("AI starts the game")

while True:

    # AI Move
    move = ai_move()
    board[move] = 'O'
    print("AI chooses position:", move + 1)
    print_board()

    if check_winner('O'):
        print("AI Wins!")
        break
    if board_full():
        print("Draw!")
        break

    # Human Move
    human = int(input("Enter your position (1-9): ")) - 1

    if board[human] != ' ':
        print("Invalid move. Try again.")
        continue

    board[human] = 'X'
    print_board()

    if check_winner('X'):
        print("Human Wins!")
        break
    if board_full():
        print("Draw!")
        break5
        5