from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def hasDuplicate(arr):
            seen = set()

            for value in arr:
                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

            return True

        # Check rows
        for row in board:
            if not hasDuplicate(row):
                return False

        # Check columns
        for col in range(9):
            column = []

            for row in range(9):
                column.append(board[row][col])

            if not hasDuplicate(column):
                return False

        # Check 3 x 3 sub-boxes
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                sub_box = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        sub_box.append(board[row][col])

                if not hasDuplicate(sub_box):
                    return False

        return True