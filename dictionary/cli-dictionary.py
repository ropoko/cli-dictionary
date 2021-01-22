# -*- coding: utf-8 -*-

import sys
import json
import requests
from dictionary.language import language
#from dictionary.language import language

def main(word, lang):
    word = word.encode('utf-8')

    # upper() because in list of language.py all the abbreviation are uppercased.
    lang = lang.upper()

    if lang in language:
       url = language[lang] + word.decode('utf-8')
       meaning(url)
    else:
       print("""
           select a valid language:
           en <english> | pt <portuguese>
           hi <hindi>   | es <spanish>
           fr <french>  | ja <japanese>
           ru <russian> | de <german>
           it <italian> | ko <korean>
           zh <chinese> | ar <arabic>
           tr <turkish>
       """)

def meaning(url):
    header = {
        "Accept": "charset=utf-8"
    }

    response = requests.request('GET', url, headers=header)
    
    data = json.loads(response.text.encode('utf-8'))

    for obj in data:
        try:
            definitions = obj['meanings'][0]['definitions']
            i = 0

            for definition in definitions:
                i = i + 1
                print(str(i) + '. ' + definition['definition'])

        except (IndexError, TypeError):
            print('sorry, we could not find the word you are looking for :(')
            break

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
