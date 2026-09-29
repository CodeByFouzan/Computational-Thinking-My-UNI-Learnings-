# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def format_name(name,order_hour):
    if (order_hour <= 19):
        print(name.lower())
    else:
        print(name.upper())


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
name = input("Please enter your name: ")
order_hour = int(input("Please enter the order hour: "))

# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.

format_name(name,order_hour)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +--------+------------+--------+
# | name   | order_hour | Output |
# +--------+------------+--------+
# | waQar  | 20         | WAQAR  |
# | FatIMA | 19         | fatima |
# | AHMED  | 22         | AHMED  |
# | kaRIm  | 5          | karim  |
# | uShNa  | 10         | ushna  |
# +--------+------------+--------+