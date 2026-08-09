from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a=set()
        b=set()
        c=defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] in a:
                    return False
                elif board[i][j]!=".":
                    a.add(board[i][j])
                if board[j][i] in b:
                    return False
                elif board[j][i]!=".":
                    b.add(board[j][i])
                
                if i//3==0:
                    k=(i//3)+(j//3)
                else:
                    k=((i//3)*3)+((j//3))
                if board[i][j] in c[k]:
                    return False
                elif board[i][j]!=".":
                    c[k].append(board[i][j])

            a=set()
            b=set()

        return True
