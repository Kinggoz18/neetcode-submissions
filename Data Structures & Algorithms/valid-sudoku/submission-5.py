class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subs = defaultdict(set)  # 3 row 3 matrix represented as an array

        # Check rows and cols
        for row in range(9):
            for col in range(9):
                subRow = row // 3
                subCol = col // 3

                # Check if (row,col) does not exist in row
                if board[row][col] == "." or board[row][col] not in rows[row]:
                    rows[row].add(board[row][col])
                else:
                    print(str(board[row][col]) + " is in " + str(rows[row]))
                    return False

                # Check if (row,col) does not exist in col
                if board[row][col] == "." or board[row][col] not in cols[col]:
                    cols[col].add(board[row][col])
                else:
                    print(str(board[row][col]) + " is in " + str(cols[row]))
                    return False

                # Check sub-cols
                if board[row][col] == "." or board[row][col] not in subs[subRow, subCol]:
                    subs[subRow, subCol].add(board[row][col])
                else:
                    print(str(board[row][col]) + " is in " + str(subs[subRow, subCol]))
                    return False

        return True
