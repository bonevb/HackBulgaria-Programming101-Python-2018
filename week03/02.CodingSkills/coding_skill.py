import sys
import json
from operator import itemgetter


# filename = sys.argv[1]
filename = 'data.json'


def best_coders(filename):

    with open(filename, 'r') as f:
        data = json.load(f)
        language = set()
        for i in range(len(data['people'])):
            for i in data['people'][i]['skills']:
                language.add(i['name'])

    coders = dict()

    for i in language:
        coders[i] = []
        # print(coders)

        for i in coders.keys():
            for j in range(len(data['people'])):
                for p in data['people'][j]['skills']:
                    if p['name'] == i:
                        coders[i].append(
                            (data['people'][j]['first_name'], data['people'][j]['last_name'], p['level']))

    for key, value in coders.items():
    	value = sorted(value, key=itemgetter(2))
    	print('{lang} - {name} {name}'.format(lang = key, name = value[-1][0]))




best_coders(filename)
