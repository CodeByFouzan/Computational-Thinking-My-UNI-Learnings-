# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def phone_rating(speed_score, lag_time ,battery_mah):
    C1 = speed_score > 50
    C2 = lag_time < 0.7
    C3 = battery_mah > 4500
    if C1 and C2 and C3:
        return 10
    elif C1 and C2:
        return 9
    elif C2 and C3:
        return 8
    elif C1 and C3:
        return 7
    elif C1 or C2 or C3:
        return 6
    else:
        return 5

    
# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
speed_score = int(input("Enter speed_score: "))
lag_time = float(input("Enter lag time: "))
battery_mah =int(input("ENter battery mah in mAh: " ))

# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

Rating = phone_rating(speed_score, lag_time, battery_mah)
print(Rating)
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# The first two testcases are from the Sample section.
#
# +-------------+----------+-------------+--------+
# | speed_score | lag_time | battery_mah | Output |
# +-------------+----------+-------------+--------+
# | 60          | 0.5      | 5000        | 10     |
# | 50          | 0.7      | 4500        | 5      |
# | 60          | 0.5      | 4000        | 9      |
# | 45          | 0.5      | 5000        | 8      |
# | 60          | 0.9      | 5000        | 7      |
# | 60          | 0.9      | 4000        | 6      |
# | 45          | 0.5      | 4000        | 6      |
# | 45          | 0.9      | 5000        | 6      |
# +-------------+----------+-------------+--------+