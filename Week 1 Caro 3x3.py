# Nguyễn Như Quỳnh - 11194482

import numpy as np

#Khởi tạo bàn cờ trống 3x3
empty = '__'
board = np.full((3, 3), empty)

still_going = True
winner = None
current_player = None

# Hàm in ra bàn cờ
def display():
    print(board[0, 0] + " | " + board[0, 1] + " | " + board[0, 2])
    print(board[1, 0] + " | " + board[1, 1] + " | " + board[1, 2])
    print(board[2, 0] + " | " + board[2, 1] + " | " + board[2, 2])

# Xác định người chơi X hoặc O chơi trước
def who_first():
    global current_player
    current_player = input("X or O ? ")

# Nhập vị trí muốn đi
def input_pos():
    position = list(input("\033[94mInput your choice: ").split(','))
    position = [int(item) for item in position]
    return position

# Kiểm tra vị trí có hợp lệ hay không
def check_turn(player):
    print(player + "'s turn\n")
    position = input_pos()

    checking = False
    while checking == False:
        while (position[0] > 2) or (position[1] > 2):
            print("Wrong input. Go again.\n")
            position = input_pos()

        if board[position[0], position[1]] == empty:
            checking = True
        else:
            print("You can't choose this. Go again.\n")
            position = input_pos()

    board[position[0], position[1]] = player
    display()

# Check dòng xem có winner không
def check_row():
    global still_going

    row_1 = board[0, 0] == board[0, 1] == board[0, 2] != empty
    row_2 = board[1, 0] == board[1, 1] == board[1, 2] != empty
    row_3 = board[2, 0] == board[2, 1] == board[2, 2] != empty

    if row_1 or row_2 or row_3:
        still_going = False
    if row_1:
        return board[0, 0]
    if row_2:
        return board[1, 0]
    if row_3:
        return board[2, 0]
    return

# Check cột xem có winner không
def check_col():
    global still_going

    col_1 = board[0, 0] == board[1, 0] == board[2, 0] != empty
    col_2 = board[0, 1] == board[1, 1] == board[2, 1] != empty
    col_3 = board[0, 2] == board[1, 2] == board[2, 2] != empty

    if col_1 or col_2 or col_3:
        still_going = False
    if col_1:
        return board[0, 0]
    if col_2:
        return board[0, 1]
    if col_3:
        return board[0, 2]
    return

# Check đường chéo xem có winner không
def check_diag():
    global still_going

    diag_1 = board[0, 0] == board[1, 1] == board[2, 2] != empty
    diag_2 = board[0, 2] == board[1, 1] == board[2, 0] != empty

    if diag_1 or diag_2:
        still_going = False
    if diag_1:
        return board[0, 0]
    if diag_2:
        return board[0, 2]
    return

# Check xem có hòa không
def check_tie():
    global still_going

    if empty not in board:
        still_going = False
    return still_going

# Luân phiên thay đổi người chơi
def change():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return current_player

# Check xem ai thắng
def check_winner():
    global winner

    row_win = check_row()
    col_win = check_col()
    diag_win = check_diag()

    if row_win:
        winner = row_win
    elif col_win:
        winner = col_win
    elif diag_win:
        winner = diag_win
    else:
        winner = None
    return

# Bắt đầu chơi
def start():
    display()
    who_first()

    while still_going:
        check_turn(current_player)
        check_winner()
        check_tie()
        change()

    if winner:
        print('\n')
        print(winner + '\033[91m won !!!')
    else:
        print('\033[91mThe match is tied.')

start()