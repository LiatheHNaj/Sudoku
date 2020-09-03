## Liathe-Najdawi
##Sudoku Solver using Backtracking Algorithm

import sys

def read_file(textfile):
    f = open(textfile, 'r')
    next(f)
    i = 0
    j = 0
    matrix = [[0 for x in range (9)] for y in range(9)]

    while True:
        j = 0 
        char = f.readline()
        for c in char:
            matrix[i][j] = int(c)
            j = j+1
            if j == 0:
                i = i+1
                break
        if i == 9:
            break
    return matrix 

def analyze_puzzle(row, column, number, matrix_board):
    check = 0
    for i in range(0,9):
        if matrix_board[row][i] == number:
            check = 1
    for i in range(0,9):
        if matrix_board[i][column] == number:
            check = 1
    row = row-row%3
    column = column-column%3

    for i in range(0,3):
        for j in range(0,3):
            if matrix_board[row+i][column+j] == number:
                check = 1
    if check == 1:
        return False
    else:
        return True

class calls:
    numbers_of_calls = 0
c = calls()
def solve_sudoku(matrix):
    c.number_of_calls = c.numbers_of_calls+1
    break_condition = 0
    for i in range(0,9):
        for j in range(0,9):
            if matrix[i][j]==0:
                break_condition = 1
                row = 1
                column = j
                break
    if break_condition == 0:
        print('Backtracking Algorithm Solution')
        for i in matrix:
            print(i)
            print('Amount of Recursions')
            print(c.numbers_of_calls)
            exit(0)
    for i in range(0,10):
        if analyze_puzzle(row, column, i, matrix):
            matrix[row][column] = i
            if solve_sudoku(matrix):
                return True
            matrix[row][column] = 0
    return False

matrix = read_file(sys.argv[1])
solve_sudoku(matrix)

