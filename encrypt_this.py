def encrypt_this(text):
    text = text.split()
    string = []
    for word in text:
        word = list(word)
        print(word)
        word[0] = str(ord(word[0]))
        if len(word) > 1:
            word[1], word[-1] = word[-1], word[1]
        string.append("".join(word))
    print(string)
    return " ".join(string)


print(encrypt_this("A wise old owl lived in an oak"))