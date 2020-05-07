from os import listdir
from random import choice

filename = choice(
    [entry for entry in listdir("teaching/madlib/madlibs") if ".txt" in entry])

madlib_types = {'n': "noun",
                'a': 'adjective',
                'av': 'abverb',
                'pln': 'plural noun',
                'pn': 'proper noun',
                'v': 'verb',
                'g': 'game',
                'ving': 'verb ending in "ing"',
                'pl': 'plant',
                'bp': 'body part',
                'p': 'place',
                'nu': 'number'
                }

madlib = ""
with open("teaching/madlib/madlibs/" + filename, 'r') as file:
    for line in file:
        madlib += line.strip() + "\n"
try:
    while madlib.index('{') != -1 and madlib.index('}') != -1:
        first = madlib.index('{')
        last = madlib.index('}')
        madlib = madlib[:first] + input(
            "Enter a " + madlib_types[madlib[first + 1:last]] + ": ") + madlib[last + 1:]
except:
    pass

print(madlib)
