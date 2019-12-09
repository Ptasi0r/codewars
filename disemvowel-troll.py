def disemvowel(string):
    vowels = "aeoiuAEIOU"
    final_string = ""
    for letter in string:
        if letter not in vowels:
            final_string += letter
    return final_string

#other sollution:
def disemvowel2(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

print(disemvowel("This website is for losers LOL!"))