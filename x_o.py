board = list(range(1, 10))
win_cords = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6 ,9)]
def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')

draw_board()

def take_input(player_token):
    while True:
        value = input('Куда поставить' + player_token)
        if not (value in '123456789'):
            print('Error')
            continue
        value = int(value)
        if str(board[value - 1] in ['XO']):
            print('Это клетка уже занят')
            continue
        board[value - 1] = player_token
        break
take_input('X')

def my_function():
    print('hello world!')

def check_win():
    for each in win_cords:
        if (board[each[0]] - 1 == board[each[1]] - 1 == board[each[2]] - 1):
            print('you win')
        else:
            continue