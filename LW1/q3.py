# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------------+------------+
# |           Input            |   Output   |
# |   b     f      B      F    |            |
# +----------------------------+------------+
# |  100   450   1000   1350   |     13       |
# |  200   500   1200   1500   |      9      |
# |  150   500   1050   1500   |     13    |
# +----------------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
b = 100  #Base Pack Grams INTEGER
f = 400  #Fruit Pack Grams INTEGER
B = 1000 #Required Smoothies Base INTEGER
F = 1200 #Required Fruit Mix INTEGER
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
b = int(input("Enter one base pack weight: ")) #INPUT
f = int(input("Enter one fruit pack weight: ")) #INPUT
B = int(input("Enter required base pack weight: ")) #INPUT
F = int(input("Enter required fruit pack weight: ")) #INPUT
No_OF_BasePack = B//b
No_OF_FruitPack = F//f
Total_Ingred_Packs = (No_OF_BasePack + No_OF_FruitPack)
print("The required ingredient packs per week are:", Total_Ingred_Packs)




# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.