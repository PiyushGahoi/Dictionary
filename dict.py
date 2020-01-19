import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(wrd):
    if wrd in data:
        return data[wrd]
    elif len(get_close_matches(wrd,data.keys()))>0:
        yn=input("Did you mean %s instead?Enter Y for yes and N for no: "%get_close_matches(wrd,data.keys())[0])
        if yn=='Y' or yn=='y':
            return data[get_close_matches(wrd,data.keys())[0]]
        elif yn=='N' or yn=='n':
            return "sorry word not found!"
        else:
            return "Sorry! we didn't get your query."
    else:
        return "Sorry no matching found please try again!"

word=input("Enter word \n")

output=translate(word.lower())
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)