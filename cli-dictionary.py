import json, sys
from urllib.request import urlopen

# receives word to find and the word's language
word_lang = str(input(''))

word = word_lang.split(' ')[0]
lang = word_lang.split(' ')[1]

lg = ''
url = ''

if lang.__eq__('en'):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/{0}/{1}'.format(
        'en', word)
else:
    url = 'https://api.dictionaryapi.dev/api/v2/entries/{0}/{1}'.format(
        'pt-BR', word)

response = urlopen(url)
data = json.loads(response.read())

for obj in data:
    try:
        for i in range(10):
            if i == 0:
                pass
            else:
                print(
                    str(obj).split("definition':")[i].split('.')[0].replace(
                        "'",
                        str(i) + '. '))

    except IndexError as ex:
        break