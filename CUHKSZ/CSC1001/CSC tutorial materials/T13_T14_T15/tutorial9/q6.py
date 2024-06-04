def eight_queens():
    """
    The classic Eight Queens puzzle is to place eight queens on a 
    chessboard such that no two queens can attack each other (i.e., no two queens are in the 
    same row, same column, or same diagonal). There are many possible solutions. Write a 
    program that displays one such solution.

    Note: you cannot just pre-define a solution and display it. 
    Please use algorithm to display a possible solution.
    """

    ############## Start your codes ##############
    #in this program, we define a list called queen=[] with a elements
    #the index of the elements are the No.line, the value of the elements are No.column
    #first define a function to print the graph of the queen=[]
    def print_queens(queen):
        for i in queen:
            print("| "*i,end="")
            if(i>=0):
                print("|Q",end="")
            print("| "*(len(queen) - i ))


    def isValid(rowNum, columnNum):
    # we check it row by row, with reverse order
        for (indexNum, value) in enumerate(queen[:rowNum][::-1]):
        # these three means same column, on the diagonal(right&left)
            if value in [columnNum, columnNum + indexNum + 1, columnNum - indexNum - 1]:
                return False
        #if the space is valid, we assign it with No.column
        queen[rowNum] = columnNum
        return True

    #before we judge, we assign the list with -1
    queen = [-1] * 8
    def find_queens(rowNum):
        length = len(queen)

    #first check the first line
        for i in range(length):
            if(isValid(rowNum,i)):
                if rowNum == length - 1:
                    print_queens(queen)
                    return True
                #if there is a valid answer the loop stops
                if find_queens(rowNum+1):
                    return True
            
    #we begin with row 0
    find_queens(0)
    ##############  End your codes  ##############

if __name__ == '__main__':
    eight_queens()

    # This function does not need a return value. 
    # You can just print your solution. For example:
    # |Q| | | | | | | |
    # | | | | |Q| | | |
    # | | | | | | | |Q|
    # | | | | | |Q| | |
    # | | |Q| | | | | |
    # | | | | | | |Q| |
    # | |Q| | | | | | |
    # | | | |Q| | | | |