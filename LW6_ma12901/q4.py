# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def clean_walkway(walkway):
    # WRITE YOUR CODE HERE
    pass
    for x in range(len(walkway)):
        if walkway[x] == "V":
            if x < len(walkway)-1:
                if walkway[x+1] == "L":
                    index = x + 1
                    walkway = walkway[:index] + "E" + walkway[index+1:]
                elif x > 0:
                    if walkway[x-1] == "L":
                        index = x - 1
                        walkway = walkway[:index] + "E" + walkway[index+1:]
            elif x == len(walkway)-1:
                if walkway[x-1] == "L":
                        index = x - 1
                        walkway = walkway[:index] + "E" + walkway[index+1:]
    return walkway
                

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

    print(clean_walkway('LVLEL'))
    # Should print: LVEEL
     
    print(clean_walkway('VLLVE'))
    # Should print: VEEVE

    print(clean_walkway("LLLLL"))
    # Should print: LLLLL

    print(clean_walkway("VVVV"))
    # Should print: VVVV

    print(clean_walkway("LVLVLV"))
    # Should print: LVEVEV

    print(clean_walkway("LLLV"))
    # Should print: LLEV

    print(clean_walkway("VLLL"))
    # Should print: VELL

    print(clean_walkway("LVLELVLEVL"))
    # Should print: LVEELVEEVE

    print(clean_walkway("LLLLLVVVVV"))
    # Should print: LLLLEVVVVV

    print(clean_walkway("EVVEVLELV"))
    # Should print: EVVEVEEEV

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py