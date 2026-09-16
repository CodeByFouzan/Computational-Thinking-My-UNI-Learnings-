# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    T     C     |            |
# +----------------+------------+
# |   10     3     |    3.0        |
# |  100    10     |    100.0       |
# |  130     4     |    52.0        |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
T = 20  #Total Quiz Points INTEGER
C = 3 #Total Correct Answers INTEGER
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
T = int(input("Enter total quiz points: ")) #INPUT
C = int(input("Enter the total correct questions: ")) #INPUT
Each_Question_Marks = T/10   #Calculating each question mark
Score_Earned = (Each_Question_Marks * C) #Calculating the score earned
print("Your Score is:", Score_Earned) #OUTPUT

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.