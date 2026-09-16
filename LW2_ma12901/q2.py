# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       m        |            |
# +----------------+------------+
# |       8        |   North         |
# |       15       |   West         |
# |      253       |   East         |
# +----------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variable here.
m = int(input("Please enter the total minutes the game was played: ")) #INTEGER (Number of Minutes)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
if (m%4 == 1):
    print("East")
elif (m%4 == 2):
    print("South")
elif (m%4 == 3):
    print("West")
else:
    print("North")
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.