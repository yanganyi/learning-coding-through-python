import json
from difflib import get_close_matches as close

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(close(w, data.keys())) > 0:
        yn = input("Did you mean {} instead? Enter Y is yes, or N if no.".format(close(w, data.keys())[0]))
        if yn == "Y":
            return data[close(w, data.keys())[0]]
        else:


    else:
        return "The word doesn't exist. Please double check it."

word =  input("Enter word: ")
a = meaning(word)
print(a)

