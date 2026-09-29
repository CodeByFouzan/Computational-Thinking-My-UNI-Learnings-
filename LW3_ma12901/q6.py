# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition(s) below.
def celsius_to_fahrenheit(celsius_temp):
    F = (celsius_temp*(9/5)) + 32
    return F
def fahrenheit_to_celsius(fahrenheit_temp):
    C =   (fahrenheit_temp - 32)*(5/9)
    return C


def temp_converter(temp, target_scale):
    if target_scale == "C":
        Converted_temp = fahrenheit_to_celsius(temp) #temp is in fahrenheit
        Converted_temp = round(Converted_temp,2)
        print(Converted_temp, "degrees Celsius is the temperature for Fatima")
    elif target_scale == "F":
        Converted_temp = celsius_to_fahrenheit(temp) #temp is in celcius
        Converted_temp = round(Converted_temp,2)
        print(Converted_temp, "degrees Fahrenheit is the temperature for Sana.")


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
temperature = int(input("Please enter the temperature: "))
target_scale = input("Please enter the target scale: ")






# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.

temp_converter(temperature,target_scale)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-------------+--------------+------------------------------------------------------+
# | temperature | target_scale | Output                                               |
# +-------------+--------------+------------------------------------------------------+
# | 95          | C            | 35.0 degrees Celsius is the temperature for Fatima.  |
# | 30          | F            | 86.0 degrees Fahrenheit is the temperature for Sana. |
# | 68          | C            | 20.0 degrees Celsius is the temperature for Fatima. |
# | 22          | F            | 71.6 degrees Fahrenheit is the temperature for Sana.|
# | 86          | C            | 30.0 degrees Celsius is the temperature for Fatima. |
# +-------------+--------------+------------------------------------------------------+