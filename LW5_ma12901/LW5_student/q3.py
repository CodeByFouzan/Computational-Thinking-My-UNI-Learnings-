# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def power_pyramid(row_count):
    # WRITE YOUR CODE HERE
    # for x in range(row_count,0,-1):
    #     for x in range(row_count)
    #     for y in range(row_count,x-1,-1):
    #         print()
   
    for x in range(row_count):
        for z in range(0,x+1):
            print(2**z , end=" ")
        for y in range(x-1,-1,-1):
            print(2**y, end=" ")
        print()


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    power_pyramid(3)
    ''' Should print:
    1
    1 2 1
    1 2 4 2 1
    '''

    power_pyramid(1)
    ''' Should print:
    1
    '''

    power_pyramid(2)
    ''' Should print:
    1
    1 2 1
    '''

    power_pyramid(6)
    ''' Should print:
    1
    1 2 1
    1 2 4 2 1
    1 2 4 8 4 2 1
    1 2 4 8 16 8 4 2 1
    1 2 4 8 16 32 16 8 4 2 1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py