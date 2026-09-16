# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +-----------------------+------------+
# |         Input         |   Output   |
# |  w1    w2    w3    s  |            |
# +-----------------------+------------+
# |  2     1     3     6  |    1        |
# |  8     5     4    10  |    2        |
# |  6     5     6    10  |    3        |
# +-----------------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
w1 = int(input("Please enter  w1: "))
w2 = int(input("Please enter  w2: "))
w3 = int(input("Please enter  w3: "))
s = int(input("Please enter the total w you can take on one trip: "))
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
sum = w1 + w2 + w3
if (sum <= s):
    print(1)
else: 
    if (w1 + w2 <= s ) or (w2 + w3 <= s):
         print(2)
    else:
        print(3)
        



# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.