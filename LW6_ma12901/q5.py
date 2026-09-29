# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def expand_message(encoded_message):
    # WRITE YOUR CODE HERE
    skip_until = 0
    s = ""
    for x in range(len(encoded_message)):
        if x < skip_until:
             continue
        if encoded_message[x].isdigit() == True:
            digindex1 = x
            digindex2 = digindex1 + 1
            if encoded_message[x+1].isdigit() == True:
                    digindex2 = x + 2
            brac_1 = digindex2
            for y in range(brac_1,len(encoded_message)):
                if encoded_message[y] == "]":
                    brac_2 = y
                    break
            count = int(encoded_message[digindex1:digindex2])
            Bef = encoded_message[0:digindex1]    
            Aft = encoded_message[brac_2+1:]
            s += count * encoded_message[brac_1+1:brac_2]
            skip_until = brac_2 + 1
        else:
             s += encoded_message[x]
    return s
        
        


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    # print(expand_message('3[ha]'))
    # # Should print: hahaha

    # print(expand_message('2[go] team!'))
    # # Should print: gogo team!

    print(expand_message('2[abc]3[cd]ef'))
    # Should print: abcabccdcdcdef

    # print(expand_message('12[!] done'))
    # # Should print: !!!!!!!!!!!! done

    # print(expand_message('3[ac]'))
    # # Should print: acacac

    # print(expand_message('3[a]2[bc]'))
    # # Should print: aaabcbc

    # print(expand_message('ab9[cd]2[ef]g'))
    # # Should print: abcdcdcdcdcdcdcdcdcdefefg

    # print(expand_message('2[a]2[b]cd'))
    # # Should print: aabbcd

#     -----------------------------------------#
#     ADD YOUR OWN TEST CASES BELOW            #
#     -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py