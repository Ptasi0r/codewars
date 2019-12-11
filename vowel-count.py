def getCount(inputStr):
    num_vowels = 0
    vowel = "aeiou"
    for letter in inputStr:
        if letter in vowel:
            num_vowels += 1
    return num_vowels

def getCount2(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

print(getCount("abracadabra"))
