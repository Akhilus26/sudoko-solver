

def is_valid(grid, row, column, number):

    for i in range(9):
        if grid[row][i] == number:
            return False
        
    for i in range(9):
        if grid[i][column] == number:
            return False
    
    corner_row = row - row % 3
    corner_col = column - column % 3

    for i in range(3):
        for j in range(3):
            if grid[corner_row + i][corner_col + j] == number:
                return False
    
    return True

def solve(grid, row, column):

    if column == 9:
        if row == 8 and column == 9:
            return True
        row += 1
        column = 0 

    if grid[row][column] > 0:
        return solve(grid, row, column + 1)
    
    for number in range(1,10):

        if is_valid(grid, row, column, number):

            grid[row][column] = number

            if solve(grid, row, column + 1):

                return True
        grid[row][column] = 0

    return False

grid = [[0, 0, 7, 0, 0, 0, 0, 8, 4],
        [1, 0, 0, 6, 0, 4, 2, 0, 7],
        [9, 5, 4, 0, 0, 2, 0, 0, 0],
        [7, 0, 0, 4, 6, 0, 0, 3, 0],
        [0, 3, 0, 2, 0, 1, 0, 4, 5],
        [0, 2, 8, 0, 3, 0, 0, 9, 0],
        [5, 4, 1, 0, 2, 0, 0, 0, 0],
        [8, 0, 0, 3, 0, 0, 0, 6, 1],
        [3, 0, 0, 0, 5, 8, 0, 2, 9]]

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print("")


else:
    print("NO solution found ")