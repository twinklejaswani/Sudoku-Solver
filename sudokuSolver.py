#1. Pick empty square
#2. Try all numbers
#3. Pick one that works
#4. Repeat
#5. BackTracks

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]    



def print_board(bo):
    for i in range(len(bo)):
        if i % 3 ==0 and i!=0 :
             print('-------------------')
        for j in range(len(bo[0])):
            if j %3 == 0 and j!=0:
                print('|',end ="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+ " ", end ="")
    print("_______________________")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) # this denotes y,x instead of x,y (row,col)
    return None

def valid(bo, num, pos):
    #pos is a tuple with (row,column)

    #stap1 check row
    for i in range(len(bo[0])): #this will always be range(9) for sudoku
        if(bo[pos[0]][i]) == num and i!=pos[1]:  #checking the full row of that pos[row][column] if that number exists
            return False
    
    #Check column
    for i in range(len(bo)):
        if(bo[i][pos[1]]) == num and i!=pos[0]:
            return False
    
    #check little box
    box_x = pos[1]//3 #integer div
    box_y = pos[0]//3

    for i in range(box_y * 3, box_y*3+3):   #multiple by 3 to get the actual index in bo from 0,1,2 index
        for j in range(box_x*3,box_x*3+3):  #adding 3 because for loop doesnt go to the last element
            if bo[i][j] == num and pos!=(i,j):
                return False

    return True



def solve(bo):
    find = find_empty(bo)
    if not find:
        return True #recursion base case i.e. board is solved no more empty boxes
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0 #no solution found reset that box to 0 and try with next value

    return False

print_board(board)
solve(board)
print("SOLUTION:")
print("---------------------------")
print_board(board)