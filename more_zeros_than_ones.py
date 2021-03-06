import codewars_test as test

# Create a moreZeros function which will receive a string for input, and return an array containing only the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.
#
# You should remove any duplicate characters, keeping the first occurence of any such duplicates, so they are in the same order in the final array as they first appeared in the input string.
#
# Examples
#
# 'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
#                True       True       False      True       False
#
#         --> ['a','b','d']
#
# 'DIGEST'--> ['D','I','E','T']
# All input will be valid strings of length > 0. Leading zeros in binary should not be counted.

def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def more_zeros(s):
    s = remove_duplicates(s)
    print(s)
    arr = []
    for letter in s:
        binary = bin(ord(letter))[2:]
        if binary.count("0") > binary.count("1"):
           arr.append(letter)
    return arr


test.assert_equals(more_zeros('abcde'), ['a', 'b', 'd'])
test.assert_equals(more_zeros('thequickbrownfoxjumpsoverthelazydog'), ['h', 'b', 'p', 'a', 'd'])
test.assert_equals(more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'),
                   ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D'])
test.assert_equals(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'),
                   ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q',
                    'R', 'T', 'X', '0'])
test.assert_equals(more_zeros('DIGEST'), ['D', 'I', 'E', 'T'])