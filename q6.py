# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------+------------+
# |        Input         |   Output   |
# |    F      T      C   |            |
# +----------------------+------------+
# |    4      4   1000   |    0        |
# |   10      5      1   |    100        |
# |   13     31     35   |     10       |
# +----------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
F = 13
T = 31
C = 35
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
Total_Money = (F*5 + T*10)
Tokens_Bought = (Total_Money//C)
print("Total Tokens That Can Be Bought Are:", Tokens_Bought)
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.