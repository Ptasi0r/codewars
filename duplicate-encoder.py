def duplicate_encode(word):
    word = word.lower()
    single = []
    encode_char = ""
    for pos, char in enumerate(word):
        is_single = True
        for index, character in enumerate(word):
            if char == character and pos != index:
                is_single = False
        if is_single:
            single.append(char)

    for char in word:
        if char in single:
            encode_char += "("
        else:
            encode_char += ")"
    return encode_char

# other solution
# def duplicate_encode(word):
#     word = word.upper()
#     result = ""
#     for char in word:
#         if word.count(char) > 1:
#             result += ")"
#         else:
#             result += "("
#
#     return result

# def duplicate_encode(word):
    # return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# from collections import Counter
#
# def duplicate_encode(word):
#     word = word.lower()
#     counter = Counter(word)
#     return ''.join(('(' if counter[c] == 1 else ')') for c in word)

print(duplicate_encode("Success"))
print(duplicate_encode("recede"))