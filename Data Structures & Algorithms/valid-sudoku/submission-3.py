class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #each row only contains a given number once
        #each col and each box also follows 
        #check each cell, if "." then continue, else add the number to its row, col and box that it belongs
        #once it's not valid, return False
        #when all cells checked return True

        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                box=(row//3)*3+(col//3)
                number=board[row][col]
                if number==".":
                    continue
                if(
                    number in rows[row] or
                    number in cols[col] or
                    number in boxes[box] 
                ):
                    return False
                
                rows[row].add(number)
                cols[col].add(number)
                boxes[box].add(number)
        return True