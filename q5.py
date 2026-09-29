# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def decode_clue(clue_number):
    Dig_1 = clue_number//10000
    temp1 = clue_number%10000
    Dig_2 = temp1//1000
    temp2 = clue_number%1000
    Dig_3 = temp2//100
    temp3 = clue_number%100
    Dig_4 = temp3//10
    temp4 = clue_number%10
    Dig_5 = temp4
    Verification_score = (Dig_1*1) + (Dig_2*2) +(Dig_3*3) + (Dig_4*4) + (Dig_5*5)
    return Verification_score
# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
clue_number = int(input("Please enter your clue number: "))


# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.
Ret_val = decode_clue(clue_number)
print(Ret_val)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-------------+--------+
# | clue_number | Output |
# +-------------+--------+
# | 58324       | 58     |
# | 91736       | 74     |
# | 42618       | 70     |
# | 73105       | 41     |
# | 99999       | 135    |
# +-------------+--------+