# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
    if len(strng) > 2:
        if strng[-1].isdigit():
            is_letter = False
            letters = ""
            digits = ""
            index_l = 0
            for index, letter in enumerate(strng[::-1]):
                if letter.isdigit():
                    digits += letter
                else:
                    is_letter = True
                    index_l = index
                    break
            index_l = len(strng) - index_l
            letters = strng[:index_l]
            digits = digits[::-1]
            zeros = ""
            for digit in digits:
                if digit == "0":
                    zeros += "0"
                    digits = digits[1:]
                else:
                    break
            if len(digits) == 0:
                digits = "0"
                zeros = zeros[1:]

            print(f"digits: {digits}, letters: {letters}, zeros: {zeros}")

            if len(str(int(digits) + 1)) > len(digits):
                zeros = zeros[1:]
            digits = str(int(digits) + 1)
            if is_letter:
                strng = letters + zeros + digits
            else:
                strng = zeros + digits
        else:
            strng += '1'
    elif len(strng) == 1:
        if strng.isdigit():
            return str(int(strng) + 1)
        else:
            return strng + '1'
    else:
        strng += '1'
    return strng




# print(increment_string("foo"))
# print(increment_string("foobar001"))
# print(increment_string("foobar1"))
# print(increment_string("foobar00"))
# print(increment_string("foobar99"))
# print(increment_string("foobar099"))
# print(increment_string(""))
# print(increment_string("009"))
print(increment_string("1"))
