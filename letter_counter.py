import string

alphabet = dict.fromkeys(string.ascii_lowercase, 0)

print("Enter a sentence:")
sentence = input().lower()

for letter in sentence:
    if letter.isalpha():
        alphabet.update({letter: alphabet.get(letter) + 1})

print("Get the amount of your chosen letter in the sentence. (Non-letters not counted and all letters are lowercase)")
choose = input()

if choose in alphabet.keys():
    print(f'{choose} appears {alphabet.get(choose)} times.')
else:
    print("Not a valid option.")