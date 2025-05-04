def askSentence():
    sentence = input("Enter a sentence: ")
    return sentence

def askUserLetters():
    symbols = []
    while True:
        ask = input("To escape this process, just type \"quit\".\nWhich letters do you choose to get rid of: ")
        if ask == "quit":
            break
        elif len(ask) > 1:
            print("Please enter a single letter.")
        else:
            symbols.append(ask)
    return symbols

def removeLetters(sentence, symbols):
    for symbol in symbols:
        if symbol not in sentence:
            print('Not in sentence')
        else:
            sentence = sentence.replace(symbol, "")
    return sentence

if __name__ == "__main__":
    print(removeLetters(askSentence(), askUserLetters()))



