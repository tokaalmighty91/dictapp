import json
from difflib import get_close_matches

data=json.load(open('data.json'))

key=input('Enter the word: ')
key=key.lower()
dym=get_close_matches(key,data.keys())

def find_meaning():
    if key in data:
        return data[key]
    elif len(dym)>0:
        for i in dym:
            choice=input('Did you mean '+i + ' Y/N ')
            if choice=='N' or choice=='n':
                if dym.index(i)==2:
                    return 'No close Matches!'
                    continue
            if choice=='Y' or choice=='y':
                return data[i]
                break
    else:
        return 'Word does not exist!'
print(find_meaning())
