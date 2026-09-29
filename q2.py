# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def fan_speed(current_setting, buttton_presses):
    final_setting = (buttton_presses+current_setting)%4
    if final_setting == 0:
        return "OFF"
    elif final_setting == 1:
        return "LOW"
    elif final_setting == 2:
        return "MEDIUM"
    else:
        return "HIGH"


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

current_setting = int(input("Please enter the current setting: "))
button_presses = int(input("Please enter the button presses: "))
# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

print(fan_speed(current_setting, button_presses))

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-----------------+----------------+--------+
# | current_setting | button_presses | Output |
# +-----------------+----------------+--------+
# | 3               | 1              | OFF    |
# | 0               | 11             | HIGH   |
# | 0               | 10             | MEDIUM |
# | 3               | 8348           | HIGH   |
# | 2               | 5903787        | LOW    |
# +-----------------+----------------+--------+