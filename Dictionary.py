import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word == word.lower()
    if word in data:
        return data[word]
    elif word == word.upper() in data:
        return data[word.upper()]
    elif word == word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())[0]) > 0:
        print("Did you mean %s instead? " %get_close_matches(word, data.keys())[0])
        decide = input("Type Y for yes and N for No: ").upper()
        if decide == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "N":
            print("Check spelling or word: ")
        else:
            print('Wrong input, type Y or N')

    else:
        print("Word not found!")



word = input("Type the word and press Enter to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)