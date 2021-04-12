# 2 x 12 = 24 
# 3 x 8 = 24
# so this is possible

def createShape(columns, rows):
    board = []
    # so lets first create printed arrays for comparison
    for i in range(columns):
        board.append([])
        for j in range(rows):
            board[i].append(j+1)
    return board

hole = createShape(2, 12)
print("___Hole___")
print(hole)
cutting_board = createShape(3, 8)
print("___uncut Board___")
print(cutting_board)

"""after creating our shapes we need to learn how to split it
 we can do this by trying to split the board at an angle
 which will be represented by x and 0 and put together later"""

# first we will take the length of the board and cut it in half for our two piece
for i in range(len(cutting_board[0])):
    cutting_board[0][i] = 0
    cutting_board[2][len(cutting_board)-i],  = 'X'
    # this places the piece into the hole
    hole[0][i] = 0
    hole[1][len(hole[0])-1-i] = 'X'

# then we can take the remaining array and split it in half
mid_split = int(len(cutting_board[0])/2)
end_split = (mid_split*2)-1
for i in range(mid_split):
    cutting_board[1][i] = 0
    cutting_board[1][end_split - i] = 'X'
    # this places the piece into the hole
    hole[1][i] = 0
    hole[0][len(hole[0])-1-i] = 'X'

print("___Cut Board___")
print(cutting_board)

# Now we can set our cutting board into the exact shape as the hole in two pieces
print("___In Hole___")
print(hole)