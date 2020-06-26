def makeDictionary():
    dict = open("Dictionary.txt", "w+")
    dictPrev = open("C:/Users/Will/Desktop/wordlist.txt", "r")
    words = dictPrev.readlines()
    for word in words:
        if len(word) > 4:
            if word.rfind("-") == -1:
                if word.rfind(".") == -1:
                    if word.rfind("'") == -1:
                        if word.rfind("(") == -1:
                            if word.rfind(")") == -1:
                                if len(word) < 11:
                                    dict.write(word)


def main():
    makeDictionary()


main()