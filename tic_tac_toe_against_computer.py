#!/usr/bin/python3

### tic tac toe against computer

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

def computer_move(board):
    
    ## check for winning move ##
    for i in range(3):
        if number_in_row(board[i],2) == 2:
            for j in range(3):
                if board[i][j] != 2 and is_legal(i,j):
                    board[i][j] = 2
                    return
    for i in range(3):
        if number_in_col(board,i,2) == 2:
            for j in range(3):
                if board[j][i] != 2 and is_legal(j,i):
                    board[j][i] = 2
                    return
    if number_in_vertical(board,2) == 2:
        for i in range(3):
            if board[i][i] != 2 and is_legal(i,i):
                board[i][i] = 2
                return
    if number_in_other_vertical(board,2) == 2:
        for i in range(3):
            if board[i][2-i] != 2 and is_legal(i,2-i):
                board[i][2-i] = 2
                return
    
    ##check if other player has a winning move
    for i in range(3):
        if number_in_row(board[i],1) == 2:
            for j in range(3):
                if board[i][j] != 1 and is_legal(i,j):
                    board[i][j] = 2
                    return
        if number_in_col(board,i,1) == 2:
            for j in range(3):
                if board[j][i] != 1 and is_legal(j,i):
                    board[j][i] = 2
                    return
    if number_in_vertical(board,1) == 2:
        for i in range(3):
            if board[i][i] != 1 and is_legal(i,i):
                board[i][i] = 2
                return
    if number_in_other_vertical(board,1) == 2:
        for i in range(3):
            if board[i][2-i] != 1 and is_legal(i,2-i):
                board[i][2-i] = 2
                return
    
    ## ckeck to see if there is a row/col/ver that has one 'O' and 2 empty spaces ##
    for i in range(3):
        if number_in_row(board[i],2) == 1 and number_in_row(board[i],0) == 2:
            for j in range(3):
                if board[i][j] != 2:
                    board[i][j] = 2
                    return
        
        if number_in_col(board,i,2) == 1 and number_in_col(board,i,0) == 2:
            for j in range(3):
                if board[j][i] != 2:
                    board[j][i] = 2
                    return
    if number_in_vertical(board,2) == 1 and number_in_vertical(board,0) == 2:
        for i in range(3):
            if board[i][i] != 2:
                board[i][i] = 2
                return
    if number_in_other_vertical(board,2) == 1 and number_in_other_vertical(board,0) == 2:
        for i in range(3):
            if board[i][2-i] != 2:
                board[i][2-i] = 2
                return
    
    for i in range(3):
        for j in range(3):
            if is_legal(i,j):
                board[i][j] = 2
                return
        
    
def number_in_vertical(board,player):
    count = 0
    for i in range(3):
        if board[i][i] == player:
            count += 1
    return count

def number_in_other_vertical(board,player):
    count = 0
    for i in range(3):
        if board[i][2-i] == player:
            count += 1
    return count

def number_in_col(board,col,player):
    count = 0
    for row in range(3):
        if board[row][col] == player:
            count += 1
    return count

def number_in_row(row,player):
    count = 0
    for i in range(3):
        if row[i] == player:
            count += 1
    return count

def print_board(board):
    print ('\n   1   2   3\n')
    for i in range(3):
        print('%d  '%(i+1), end = '')
        for j in range(3):
            if board[i][j] == 1:
                print('X', end = '')
            elif board[i][j] == 2:
                print('O', end = '')
            else:
                print(' ', end = '')
            if j!=2:
                print(' | ',end = '')
        if i == 2:
            print()
        else:
            print('\n  ---+---+---')


def check_for_winners(board,player):
    for i in range(3):
        if number_in_row(board[i],player) == 3:
            return True
        if number_in_col(board,i,player) == 3:
            return True
        if number_in_vertical(board,player) == 3:
            return True
        if number_in_other_vertical(board,player) == 3:
            return True
    return False

def is_legal(row,col):
    if col<0 or col>2:
        return 0
    if row<0 or row>2:
        return 0
    if board[row][col] != 0:
        return 0
    return 1

def move(player):
    try:
        row = int(input('pick row: '))-1
        print_board(board)
        col = int(input('pick column: '))-1
    except Exception as e:
        print_board(board)
        print('Invalid input, try again:')
        move(player)
        return
    
    while not is_legal(row,col):
        print_board(board)
        print ('Invalid input, try again: ')
        try:
            row = int(input('pick row: '))-1
            print_board(board)
            col = int(input('pick column: '))-1
        except Exception as e:
            print_board(board)
            print('Invalid input, try again:')
            move(player)
            return
        
    board[row][col] = player

        
print_board(board)


for i in range(4):
    move(1)
    print_board(board)
    if (check_for_winners(board,1)):
        print('****** YOU WIN! ******')
        break
    computer_move(board)
    print_board(board)
    if (check_for_winners(board,2)):
        print('****** YOU LOSE ********')
        break
    
    if i == 3:
        print('****** IT IS A TIE ******')
    
