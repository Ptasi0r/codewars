def toJadenCase(string):
    final_string = string[0].upper()
    for i in range(1, len(string)):
        print(string[i] == " ")
        if string[i-1] == " ":
            final_string += string[i].upper()
        else:
            final_string += string[i]
    return final_string

#other sollution

def toJadenCase2(string):
    return " ".join(w.capitalize() for w in string.split())

print(toJadenCase("How can mirrors be real if our eyes aren't real"))