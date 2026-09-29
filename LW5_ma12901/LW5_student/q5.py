# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def stage_light_display(size):
    # WRITE YOUR CODE HERE
    for x in range(size-1,-1,-1):
        for z in range(x):
            print(" ", end = "")

        for y in range(2*(size-x)-1):
            print("*", end = "")
            
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

    stage_light_display(5)
    ''' Should print:
        *
       ***
      *****
     *******
    *********
    '''

    stage_light_display(4)
    ''' Should print:
       *
      ***
     *****
    *******
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py