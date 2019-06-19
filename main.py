import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))


def meaning(word):
    word=word.lower()
    if (word in data):
        return (data[word])
    elif(0<len(get_close_matches(word,data.keys(),3,0.72))):
        ans=input("Did you mean %s? Type Y for Yes or N for No: "%get_close_matches(word,data.keys(),3,0.72)[0].upper()).upper()
        if(ans=="Y"):
            return data[get_close_matches(word,data.keys(),3,0.72)[0]]
        else:
            return ["The word doesn't exist. Please double check it"]
    else:
        return ["The word doesn't exist. Please double check it"]


#print (help(get_close_matches))


print(*meaning(input()), sep="\n")
