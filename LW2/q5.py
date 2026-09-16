# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       g        |            |
# +----------------+------------+
# |       29       |    29       |
# |       78       |    80        |
# |       51       |    51        |
# +----------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variable here.
g = int(input("Please enter your score: "))

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
Diff = (5 - g%5)
if g < 38 :
    print(g)
elif ((g+Diff)-g < 3):
    print(g + Diff)
else:
    print(g)
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.