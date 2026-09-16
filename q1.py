# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    N     K     |            |
# +----------------+------------+
# |   50     0     |      50    |
# |  100    50     |      50    |
# |   25    12     |      13    |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
N = 5 #Number of questions (INTEGER)
K = 2 #Total marks for Ayaan (INTEGER)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
N = int(input("Enter total questions in the quiz: ")) #INPUT
K = int(input("Enter the score for Ayaan: ")) #INPUT
Bilal_Marks = N - K #Calculating the score for Bilal
print("Bilal Score is:", Bilal_Marks)  #OUTPUT

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.