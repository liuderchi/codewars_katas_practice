'''
Write a function done_or_not passing a board (list[list_lines]) as parameter.
If the board is valid return 'Finished!', otherwise return 'Try again!'
'''
def done_or_not(board): #board[i][j]

    for m in range(9):
        col = [board[i][m] for i in range(9)]
        row = board[m]
        if len(set(col)) != 9 or len(set(row)) != 9:
            return 'Try again!'

    for oi in range(0, 9, 3):
        for oj in range(0, 9, 3):
            block = []
            for i in range(3):
                block += board[oi + i][oj:oj + 3]
            if len(set(block)) != 9:
                return 'Try again!'

    return 'Finished!'


assert done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                   ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                   ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                   ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                   ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                   ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                   ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                   ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                   ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]) == 'Finished!'

assert done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                   ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                   ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                   ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                   ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                   ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                   ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                   ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                   ,[8, 7, 9, 6, 4, 2, 1, 3, 9]]) == 'Try again!'
