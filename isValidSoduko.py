from collections import  defaultdict
board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

""""
We need to check row
We need to check colum
We need to check cube
"""

"""
brute force it
"""
"""
def check_cube(nums, i, j):
 row = math.floor(j / 3)*3
 col = math.floor(i / 3)*3
 for m in range(3):
  for n in range(3):
   if m+col != i and n+row != j:
    if nums[m + col][n + row] == nums[i][j]:
     print(m+col, n + row, "vs", i, j)
     print(nums[m + col][n + row], "vs",nums[i][j])
     return False
 return True



for i in range(len(board)):
 for j in range(len(board)):
  if board[i][j] == ".":
   continue
  if not check_cube(board, i, j):
   print("check cube",i, j)
   break
  for k in range(len(board)):
   if i != k:
    if board[k][j] == board[i][j]:
     print(i, j, "vs", k, j)
     print(board[i][j], "compared to", board[k][j])
     print("Not Valid")
     break
    if j != k:
     if board[i][k] == board[i][j]:
      print(i, j, "vs", i, k)
      print(board[i][j], "compared with", board[i][k])
      print("Not Valid")
      break

"""

"""
I don't need to check each row for each value
I can go once over each row, and once over each column and create a set, if I try to add to this set a value tha
already existed then its not valid
"""
def isValid(board):
 cols = defaultdict(set)
 rows = defaultdict(set)
 squares = defaultdict(set)  # key = (r /3, c /3)

 for r in range(9):
  for c in range(9):
   if board[r][c] == ".":
    continue
   if (
           board[r][c] in rows[r]
           or board[r][c] in cols[c]
           or board[r][c] in squares[(r // 3, c // 3)]
   ):
    return False
   cols[c].add(board[r][c])
   rows[r].add(board[r][c])
   squares[(r // 3, c // 3)].add(board[r][c])

 return True



