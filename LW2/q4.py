# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +------------------+------------+
# |      Input       |   Output   |
# |  A     B     C   |            |
# +------------------+------------+
# |  18   271   31   |    302        |
# |  127  2933  182  |    3115        |
# |  21    2    18   |    39        |
# +------------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
A = int(input("Please enter A fun score: "))
B = int(input("Please enter B fun score: "))
C = int(input("Please enter C fun score: "))

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
if (A == B and A == C):
    print(A + B)
elif (A > B) and (A > C):
    if (B > C):
        print(A + B)
    else:
        print(A + C)
elif (B > A) and (B > C):
    if (A < C):
        print(B + C)
elif (C > A) and (C > B):
    if (A > B):
        print(A+C)
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
