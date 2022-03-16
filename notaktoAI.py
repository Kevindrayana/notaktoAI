# line function to print a line
def line(iterable, board_list, board_num):
    for num in board_num:
        if num == '':
            continue
            
        for i in iterable:
            
            for j in range(2,-1,-1):
                if str(board_num[j]).isdecimal():
                    x = j
                    break
            
            if (num == x) and (i == 2 or i == 5 or i == 8):
                print(board_list[num][i], end = '\n')
            elif i == 2 or i == 5 or i == 8:
                print(board_list[num][i], end = '  ')
            else:
                print(board_list[num][i], end = ' ')
            
            
# board function to print the board
def board(board_list, board_marker):
## printing the board marker
    for i in range(len(board_marker)):
        
        for j in range(2,-1,-1):
                if str(board_num[j]).isdecimal():
                    x = j
                    break
                    
        if i != x and board_marker[i] != '':
            print(f'{board_marker[i]:<7}', end = '')
        else:
            print(board_marker[i],end = '')
    print()
    line((0,1,2), board_list, board_num)
    line((3,4,5), board_list, board_num)
    line((6,7,8), board_list, board_num)

    
# change board list function to mutate the board_list in a given index to X    
def change_board_list(move, board_list):
    if move[0] == 'A':
        board_list[0][int(move[1])] = 'X'
    elif move[0] == 'B':
        board_list[1][int(move[1])] = 'X'
    elif move[0] == 'C':
        board_list[2][int(move[1])] = 'X'
        

# delete board_function to delete part of a board which is dead
def delete_board(index):
    board_list[index] = ['', '', '', '', '', '', '', '', '']
    board_marker[index] = ''
    board_num[index] = ''
    
    
# check win function to specify winning conditions
def check_win(board_list, board_num):
    for i in board_num:
        if i != '':
            if (board_list[i][0] == board_list[i][1] == board_list[i][2] == 'X'  or board_list[i][3] == board_list[i][4] == board_list[i][5] == 'X' or board_list[i][6] == board_list[i][7] == board_list[i][8] == 'X' or board_list[i][0] == board_list[i][3] == board_list[i][6] == 'X' or board_list[i][1] == board_list[i][4] == board_list[i][7] == 'X' or board_list[i][2] == board_list[i][5] == board_list[i][8] == 'X' or board_list[i][0] == board_list[i][4] == board_list[i][8] == 'X' or board_list[i][6] == board_list[i][4] == board_list[i][2] == 'X'):
                delete_board(i)
                return True
        

# check input invalidity 
def input_check(move,used_move,board_marker):
    if move not in ('A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'):
        return True
    if move in used_move:
        return True
    if move[0] not in board_marker:
        return True
    

def scissors_move(board_list):
    for i in range(3):
        if board_list[i][4] != 'X' and board_list[i] != ['', '', '', '', '', '', '', '', '']:
            if board_list[i][1] == 'X' and board_list[i][3] == 'X' and board_list[i][8] != 'X': 
                if i == 0:
                    return 'A8'
                elif i == 1:
                    return 'B8'
                elif i == 2:
                    return 'C8'
            elif board_list[i][1] == 'X' and board_list[i][3] != 'X' and board_list[i][8] == 'X':
                if i == 0:
                    return 'A3'
                elif i == 1:
                    return 'B3'
                elif i == 2:
                    return 'C3'
            elif board_list[i][1] != 'X' and board_list[i][3] == 'X' and board_list[i][8] == 'X': 
                if i == 0:
                    return 'A1'
                elif i == 1:
                    return 'B1'
                elif i == 2:
                    return 'C1'
            elif board_list[i][1] == 'X' and board_list[i][5] == 'X' and board_list[i][6] != 'X': 
                if i == 0:
                    return 'A6'
                elif i == 1:
                    return 'B6'
                elif i == 2:
                    return 'C6'
            elif board_list[i][1] == 'X' and board_list[i][5] != 'X' and board_list[i][6] == 'X':
                if i == 0:
                    return 'A5'
                elif i == 1:
                    return 'B5'
                elif i == 2:
                    return 'C5'
            elif board_list[i][1] != 'X' and board_list[i][5] == 'X' and board_list[i][6] == 'X':
                if i == 0:
                    return 'A1'
                elif i == 1:
                    return 'B1'
                elif i == 2:
                    return 'C1'
            elif board_list[i][3] == 'X' and board_list[i][7] == 'X' and board_list[i][2] != 'X':
                if i == 0:
                    return 'A2'
                elif i == 1:
                    return 'B2'
                elif i == 2:
                    return 'C2'
            elif board_list[i][3] == 'X' and board_list[i][7] != 'X' and board_list[i][2] == 'X':
                if i == 0:
                    return 'A7'
                elif i == 1:
                    return 'B7'
                elif i == 2:
                    return 'C7'
            elif board_list[i][3] != 'X' and board_list[i][7] == 'X' and board_list[i][2] == 'X':
                if i == 0:
                    return 'A3'
                elif i == 1:
                    return 'B3'
                elif i == 2:
                    return 'C3'
            elif board_list[i][0] == 'X' and board_list[i][5] == 'X' and board_list[i][7] != 'X': 
                if i == 0:
                    return 'A7'
                elif i == 1:
                    return 'B7'
                elif i == 2:
                    return 'C7'
            elif board_list[i][0] == 'X' and board_list[i][5] != 'X' and board_list[i][7] == 'X': 
                if i == 0:
                    return 'A5'
                elif i == 1:
                    return 'B5'
                elif i == 2:
                    return 'C5'
            elif board_list[i][0] != 'X' and board_list[i][5] == 'X' and board_list[i][7] == 'X': 
                if i == 0:
                    return 'A0'
                elif i == 1:
                    return 'B0'
                elif i == 2:
                    return 'C0'


def sacrifice_if_there_is_x_in_centre(board_list):
    for i in range(3):
        if board_list[i][0] == 'X' and board_list[i][4] == 'X':
            if i == 0:
                return 'A8'
            elif i == 1:
                return 'B8'
            elif i == 2:
                return 'C8'
            
        elif board_list[i][1] == 'X' and board_list[i][4] == 'X':
            if i == 0: 
                return 'A7'
            elif i == 1:
                return 'B7'
            elif i == 2:
                return 'C7'
            
        elif board_list[i][2] == 'X' and board_list[i][4] == 'X':
            if i == 0:
                return 'A6'
            elif i == 1:
                return 'B6'
            elif i == 2:
                return 'C6'
            
        elif board_list[i][3] == 'X' and board_list[i][4] == 'X':
            if i == 0:
                return 'A5'
            elif i == 1:
                return 'B5'
            elif i == 2:
                return 'C5'
            
        elif board_list[i][5] == 'X' and board_list[i][4] == 'X':
            if i == 0:
                return 'A3'
            elif i == 1:
                return 'B3'
            elif i == 2:
                return 'C3'
        
        elif board_list[i][6] == 'X' and board_list[i][4] == 'X':
            if i == 0:
                return 'A2'
            elif i == 1:
                return 'B2'
            elif i == 2:
                return 'C2'
        
        elif board_list[i][7] == 'X' and board_list[i][4] == 'X':
            if i == 0:
                return 'A1'
            elif i == 1:
                return 'B1'
            elif i == 2:
                return 'C1'
        
        elif board_list[i][8] == 'X' and board_list[i][4] == 'X':
            if i == 0:
                return 'A0'
            elif i == 1:
                return 'B0'
            elif i == 2:
                return 'C0'
    
    
def sacrifice_if_no_x_in_centre(board_list):
    for i in range(3):
        if board_list[i][0] == 'X' and board_list[i][1] == 'X' and board_list[i][2] != 'X':
            if i == 0:
                return 'A2'
            elif i == 1:
                return 'B2'
            elif i == 2:
                return 'C2'
        elif board_list[i][0] == 'X' and board_list[i][1] != 'X' and board_list[i][2] == 'X':
            if i == 0:
                return 'A1'
            elif i == 1:
                return 'B1'
            elif i == 2:
                return 'C1'
        elif board_list[i][0] != 'X' and board_list[i][1] == 'X' and board_list[i][2] == 'X':
            if i == 0:
                return 'A0'
            elif i == 1:
                return 'B0'
            elif i == 2:
                return 'C0'
            
        elif board_list[i][0] == 'X' and board_list[i][3] == 'X' and board_list[i][6] != 'X':
            if i == 0:
                return 'A6'
            elif i == 1:
                return 'B6'
            elif i == 2:
                return 'C6'
        elif board_list[i][0] == 'X' and board_list[i][3] != 'X' and board_list[i][6] == 'X':
            if i == 0:
                return 'A3'
            elif i == 1:
                return 'B3'
            elif i == 2:
                return 'C3'
        elif board_list[i][0] != 'X' and board_list[i][3] == 'X' and board_list[i][6] == 'X':
            if i == 0:
                return 'A0'
            elif i == 1:
                return 'B0'
            elif i == 2:
                return 'C0'
            
        elif board_list[i][2] == 'X' and board_list[i][5] == 'X' and board_list[i][8] != 'X':
            if i == 0:
                return 'A8'
            elif i == 1:
                return 'B8'
            elif i == 2:
                return 'C8'
        elif board_list[i][2] == 'X' and board_list[i][5] != 'X' and board_list[i][8] == 'X':
            if i == 0:
                return 'A5'
            elif i == 1:
                return 'B5'
            elif i == 2:
                return 'C5'
        elif board_list[i][2] != 'X' and board_list[i][5] == 'X' and board_list[i][8] == 'X':
            if i == 0:
                return 'A2'
            elif i == 1:
                return 'B2'
            elif i == 2:
                return 'C2'
            
        elif board_list[i][6] == 'X' and board_list[i][7] == 'X' and board_list[i][8] != 'X':
            if i == 0:
                return 'A8'
            elif i == 1:
                return 'B8'
            elif i == 2:
                return 'C8'
        elif board_list[i][6] == 'X' and board_list[i][7] != 'X' and board_list[i][8] == 'X':
            if i == 0:
                return 'A7'
            elif i == 1:
                return 'B7'
            elif i == 2:
                return 'C7'
        elif board_list[i][6] != 'X' and board_list[i][7] == 'X' and board_list[i][8] == 'X':
            if i == 0:
                return 'A6'
            elif i == 1:
                return 'B6'
            elif i == 2:
                return 'C6'
    
        elif board_list[i][1] == 'X' and board_list[i][4] != 'X' and board_list[i][7] == 'X':
            if i == 0:
                return 'A4'
            elif i == 1:
                return 'B4'
            elif i == 2:
                return 'C4'
        
        elif board_list[i][3] == 'X' and board_list[i][4] != 'X' and board_list[i][5] == 'X':
            if i == 0:
                return 'A4'
            elif i == 1:
                return 'B4'
            elif i == 2:
                return 'C4'
        
        elif board_list[i][0] == 'X' and board_list[i][4] != 'X' and board_list[i][8] == 'X':
            if i == 0:
                return 'A4'
            elif i == 1:
                return 'B4'
            elif i == 2:
                return 'C4'   
        
        elif board_list[i][2] == 'X' and board_list[i][4] != 'X' and board_list[i][6] == 'X':
            if i == 0:
                return 'A4'
            elif i == 1:
                return 'B4'
            elif i == 2:
                return 'C4'
        

def board_count(board_num):
    counter = 0
    for i in board_num:
        if i == '':
            continue
        else:
            counter += 1
    return counter

def count_x_in_centre(board_list):
    counter = []
    for i in board_list:
        if i == ['', '', '', '', '', '', '', '', '']:
            pass
        elif i[4] != 'X':
            counter.append(False)
        elif i[4] == 'X':
            counter.append(True)
    return counter


def make_board_for_sacrifice(move, board_list):
    lst = []
    i = move[0]
    if i == 'A':
        x = 0
    elif i =='B':
        x = 1
    elif i == 'C':
        x = 2
    print(x)
    for j in range(len(board_list)):
        if j == x:
            lst.append(board_list[j])
        else:
            lst.append(['', '', '', '', '', '', '', '', ''])
    return lst

def count_x_in_a_board(board_list):
    counter = 0
    for board in board_list:
        for i in board:
            if i == 'X':
                counter += 1
                
    return counter

def scissors_in_board(board_list):
    for i in range(3):
        if board_list[i] == [0, 'X', 2, 'X', 4, 5, 6, 7, 'X'] or board_list[i] == [0, 'X', 2, 3, 4, 'X', 'X', 7, 8] or board_list[i] == [0, 1, 'X', 'X', 4, 5, 6, 'X', 8] or board_list[i] == ['X', 1, 2, 3, 4, 'X', 6, 'X', 8]:
            return True
        
def oneboard(board_list, used_move):
    
    board_alphabet = move[0]
    if board_alphabet == 'A':
        i = 0
    elif board_alphabet == 'B':
        i = 1
    elif board_alphabet == 'C':
        i = 2

    my_dict = {0: 'A', 1: 'B', 2: 'C'}

    if board_list[i][4] == 'X':

        if (board_list[i][0] == 'X') and (board_list[i][1] != 'X') and ((my_dict[i]+'7') not in used_move):
            return my_dict[i] + '7'
        elif board_list[i][0] == 'X' and board_list[i][3] != 'X' and ((my_dict[i]+'5') not in used_move):
            return my_dict[i] + '5'

        if board_list[i][1] == 'X' and board_list[i][2] != 'X' and ((my_dict[i]+'6') not in used_move):
            return my_dict[i] + '6'
        elif board_list[i][1] == 'X' and board_list[i][0] != 'X' and ((my_dict[i]+'8') not in used_move):
            return my_dict[i] + '8'

        if board_list[i][2] == 'X' and board_list[i][1] != 'X' and ((my_dict[i]+'7') not in used_move):
            return my_dict[i] + '7'
        elif board_list[i][2] == 'X' and board_list[i][5] != 'X'and ((my_dict[i]+'3') not in used_move):
            return my_dict[i] + '3'

        if board_list[i][3] == 'X' and board_list[i][6] != 'X' and ((my_dict[i]+'2') not in used_move):
            return my_dict[i] + '2'
        elif board_list[i][3] == 'X' and board_list[i][0] != 'X' and ((my_dict[i]+'8') not in used_move):
            return my_dict[i] + '8'

        if board_list[i][5] == 'X' and board_list[i][2] != 'X' and ((my_dict[i]+'6') not in used_move):
            return my_dict[i] + '6'
        elif board_list[i][5] == 'X' and board_list[i][8] != 'X' and ((my_dict[i]+'0') not in used_move):
            return my_dict[i] + '0'

        if board_list[i][6] == 'X' and board_list[i][7] != 'X' and ((my_dict[i]+'1') not in used_move):
            return my_dict[i] + '1'
        elif board_list[i][6] == 'X' and board_list[i][3] != 'X' and ((my_dict[i]+'5') not in used_move):
            return my_dict[i] + '5'

        if board_list[i][7] == 'X' and board_list[i][8] != 'X' and ((my_dict[i]+'0') not in used_move):
            return my_dict[i] + '0'
        elif board_list[i][7] == 'X' and board_list[i][6] != 'X' and ((my_dict[i]+'2') not in used_move):
            return my_dict[i] + '2'

        if board_list[i][8] == 'X' and board_list[i][7] != 'X' and ((my_dict[i]+'1') not in used_move):
            return my_dict[i] + '1'
        elif board_list[i][8] == 'X' and board_list[i][5] != 'X' and ((my_dict[i]+'3') not in used_move):
            return my_dict[i] + '3'
    for i in range(3):
        if board_list[i][4] != 'X' and board_list[i] != ['', '', '', '', '', '', '', '', ''] and not scissors_in_board(board_list):
            if board_list[i][0] == 'X' and board_list[i][8] != 'X':
                return my_dict[i] + '8'
            elif board_list[i][1] == 'X' and board_list[i][7] != 'X':
                return my_dict[i] + '7'
            elif board_list[i][2] == 'X'and board_list[i][6] != 'X':
                return my_dict[i] + '6'
            elif board_list[i][3] == 'X'and board_list[i][5] != 'X':
                return my_dict[i] + '5'
            elif board_list[i][5] == 'X'and board_list[i][3] != 'X':
                return my_dict[i] + '3'
            elif board_list[i][6] == 'X'and board_list[i][2] != 'X':
                return my_dict[i] + '2'
            elif board_list[i][7] == 'X'and board_list[i][1] != 'X':
                return my_dict[i] + '1'
            elif board_list[i][8] == 'X'and board_list[i][0] != 'X':
                return my_dict[i] + '0'
        
        elif board_list[i] == [0, 'X', 2, 'X', 4, 5, 6, 7, 'X']:
            return my_dict[i] + '0'
        elif board_list[i] == [0, 'X', 2, 3, 4, 'X', 'X', 7, 8]:
            return my_dict[i] + '2'
        elif board_list[i] == [0, 1, 'X', 'X', 4, 5, 6, 'X', 8]:
            return my_dict[i] + '6'
        elif board_list[i] == ['X', 1, 2, 3, 4, 'X', 6, 'X', 8]:
            return my_dict[i] + '8'
        elif board_list[i] == [0, 'X', 2, 3, 4, 'X', 'X', 7, 8]:
            return my_dict[i] + '2'
        
        elif board_list[i] == ['X', 'X', 2, 'X', 4, 'X', 6, 7, 'X']:
            return my_dict[i] + '7'
        elif board_list[i] == ['X', 'X', 2, 'X', 4, 5, 6, 'X', 'X']:
            return my_dict[i] + '5'
        
        elif board_list[i] == [0, 'X', 'X', 'X', 4, 'X', 'X', 7, 8]:
            return my_dict[i] + '7'
        elif board_list[i] == [0, 'X', 'X', 3, 4, 'X', 'X', 'X', 8]:
            return my_dict[i] + '3'
        
        elif board_list[i] == [0, 'X', 'X', 'X', 4, 5, 'X', 'X', 8]:
            return my_dict[i] + '5'
        elif board_list[i] == [0, 1, 'X', 'X', 4, 'X', 'X', 'X', 8]:
            return my_dict[i] + '1'
        
        elif board_list[i] == ['X', 1, 2, 'X', 4, 'X', 6, 'X', 'X']:
            return my_dict[i] + '1'
        elif board_list[i] == ['X', 'X', 2, 3, 4, 'X', 6, 'X', 'X']:
            return my_dict[i] + '3'
        
        
        
def twoboard(used_move):

    for i in range(len(board_list)):
        if board_list[i] == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if i == 0:
                return 'A4'
            elif i == 1:
                return 'B4'
            else:
                return 'C4'
    
    if count_x_in_centre(board_list) == [True, True]:
        mylist = make_board_for_sacrifice(move, board_list)
        if sacrifice_if_there_is_x_in_centre (mylist)!= None:
            return sacrifice_if_there_is_x_in_centre(mylist)
        
    elif count_x_in_centre(board_list) == [True, False] or count_x_in_centre(board_list) == [False, True]:
        # play in the one with center x
        if move[0] + '4' in used_move:
            return oneboard(board_list, used_move)
        # play in the one with no center x
        else:
            new_board = []
            for i in board_list:
                if i[4] != 'X':
                    new_board.append(i)
                elif i[4] == 'X':
                    new_board.append(['', '', '', '', '', '', '', '', ''])
                    
            if sacrifice_if_no_x_in_centre(new_board) != None:
                return sacrifice_if_no_x_in_centre(new_board)
            else:
                return scissors_move(board_list)    
            

def threeboard():
    
    if move_count == 0:
        return 'A4'

    if move_count == 1 and move[0] == 'A':
        return sacrifice_if_there_is_x_in_centre(board_list) 
    if move_count == 1 and used_move[-1][0] == 'B':
        return 'C4'
    if move_count == 1 and used_move[-1][0] == 'C':
        return 'B4'
    
    if move_count >1 and sacrifice_if_there_is_x_in_centre(board_list) != None:
        return sacrifice_if_there_is_x_in_centre(board_list)
    elif move_count >1 and sacrifice_if_no_x_in_centre(board_list) != None:
        return sacrifice_if_no_x_in_centre(board_list)
    
    
    if move[0] == 'A':
        mymove = 0
    elif move[0] == 'B':
        mymove = 1
    else:
        mymove = 2
    
    centre = count_x_in_centre(board_list)
    if move_count == 2 and centre == [True, True, True]:
        return sacrifice_if_there_is_x_in_centre(board_list)
    elif move_count >= 2 and (centre == [True, False, True] or centre == [True, True, False]):
        
        if centre[mymove] == True:
            return sacrifice_if_there_is_x_in_centre(board_list)
        else:
            if sacrifice_if_no_x_in_centre(board_list) != None:
                return sacrifice_if_no_x_in_centre(board_list)
            else:
                return scissors_move(board_list)
    
import random
board_list = []
for _ in range(3):
    board_list.append([num for num in range(9)])

board_marker = ['A', 'B', 'C']

board_num = [0,1,2]

used_move = []

move_count = 0


while True: 
    # AI MOVE
    if board_count(board_num) == 3:
        move = threeboard()
    elif board_count(board_num) == 2:
        move = twoboard(used_move)
    elif board_count(board_num) == 1:
        move = oneboard(board_list,used_move)

    if move == None:
        while True:
            move = random.choice(('A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'))

            if input_check(move,used_move,board_marker):
                pass
            else:
                break

    board(board_list, board_marker)

    print('Player 1:', move)

    change_board_list(move, board_list)

    check_win(board_list, board_num)

    used_move.append(move)
    
    move_count += 1

    if board_count(board_num) == 0:
        print('Player 2 wins game')
        break
        
    # player 2 move
    board(board_list, board_marker)

    while True:
        move = input("Player 2: ")
        
        if input_check(move,used_move,board_marker):
            print('Invalid move, please input again')
            pass
        else:
            used_move.append(move)
            break
    
    change_board_list(move, board_list)

    check_win(board_list, board_num)

    if board_count(board_num) == 0:
        print('Player 1 wins game')
        break
