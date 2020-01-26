def increment_string(strng):
    if strng == '':                              # if its an empty string
        return '1'

    elif strng[-1].isalpha():                    # if string ends with an alphabet
        strng = strng + '1'
        return strng

    else:                                        # is string ends with a digit
        final_string = ''
        num_string = ''
        rev_string = strng[::-1]                 # reverse the string
        for i, x in enumerate(rev_string):

            if x.isdigit():                      # all the digits add to num_string
                num_string += x
            else:
                final_string = rev_string[i:]    # as soon as caracters start add the est of the strg to final string
                break

        final_string = final_string[::-1]
        length = len(num_string)                 # used for zfill()
        num_string = int(num_string[::-1]) + 1   # reverse num string convert into int and add 1

        x = final_string + str(num_string).zfill(length)
        return x
