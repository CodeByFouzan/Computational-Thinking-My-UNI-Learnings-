# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       p        |            |
# +----------------+------------+
# |      2500      |    YES        |
# |      2800      |     NO       |
# |      2600      |     NO       |
# +----------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variable here.
p = int(input("Enter price per ticket: ")) #INTEGER
Budget =10000
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
Total = 4 * p
if (Total <= Budget):
    print("YES")
else:
    print("NO")
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.


