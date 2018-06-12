from collections import Iterable
from copy import deepcopy

#data = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': {'f': 4, 'j': 6, 'h': [{'i': 11}, {'k': 12}, {'d': 12}]}}}

#data = {'a': [[{'b': 2}, {'c': 3}]]}

def deep_find(data, key, result = None):
    if result is None:
        result = [data]

    for k, v in data.items():
        if isinstance(v, dict):
            result.append(v)
            deep_find(v, key, result=result)
        if isinstance(v, Iterable) and not isinstance(v, str):
            for i in v:
                if isinstance(i, dict):
                    result.append(i)
                    deep_find(i, key, result=result)

    for i in result:
        if key in i.keys():
            return i[key]


#print(deep_find(data, 'd')) 


def deep_find_all(data, key, result = None):
    final = []
    if result is None:
        result = [data]


    for k, v in data.items():
        if isinstance(v, dict):
            result.append(v)
            deep_find(v, key, result=result)
        if isinstance(v, Iterable) and not isinstance(v, str):
            for i in v:
                if isinstance(i, dict):
                    result.append(i)
                    deep_find(i, key, result=result)
    for i in result:
        if key in i.keys():
            final.append(i[key])
    return final

# print(deep_find_all(data, 'd'))


def deep_update(data, key, val):
    def inner(data, key, val):
        original_data = data
        for k, v in original_data.items():
            if k == key:
                original_data[k] = val
                return original_data
            if isinstance(v, dict):
                inner(v, key, val)
            if isinstance(v, list) and not isinstance(v, str):
                for i in v:
                    if isinstance(i, dict):
                        inner(i, key, val)
        return original_data
    return inner(deepcopy(data), key, val)


# print(deep_update(data, 'k', '5'))  

	

def deep_apply(func, data):
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(k, int):
                data[func(k)] = data.pop(k)
            if isinstance(k, str):
                data[func(k)] = data.pop(k)

            if isinstance(v, dict):
                deep_apply(func, v)

            if isinstance(v, Iterable) and not isinstance(v, str):
                for i in v:
                    if isinstance(i, dict):
                        deep_apply(func, i)
    if isinstance(data, Iterable):
        for i in data:
            if isinstance(i, dict):
                deep_apply(func, i)

    return data



def deep_compare(obj1, obj2):
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        return obj1 == obj2
    if isinstance(obj1, list) and isinstance(obj2, list):
        if ((len(obj1) == len(obj2)) and (all(i in obj2 for i in obj1))):
            return True
        else:
            return False
    

# print(deep_compare(data2, data1))

def deep_find_key(data, key, result = None):
    if result is None:
        result = [data]

    for k, v in data.items():
        if isinstance(v, dict):
            result.append(v)
            deep_find_key(v, key, result=result)
        if isinstance(v, Iterable) and not isinstance(v, str):
            for i in v:
                if isinstance(i, dict):
                    result.append(i)
                    deep_find_key(i, key, result=result)

    for i in result:
        if key in i.keys():
            return key

def deep_find_keys_from_data(data, result = None):
    if result is None:
        result = []

    for k, v in data.items():
        result.append(k)
        if isinstance(v, dict):
            deep_find_keys_from_data(v, result=result)
        if isinstance(v, Iterable) and not isinstance(v, str):
            for i in v:
                if isinstance(i, dict):
                    result.append(i)
                    deep_find_keys_from_data(i, result=result)
    return result

def schema_validator(schema, data, result = None):
    if result is None:
        result = []
    for i in schema:
        if  isinstance(i, list):
            schema_validator(i, data, result=result)
        else:
            result.append(i)

    isTrue = True

    for key in result:
        key_from_data = deep_find_key(data, key)
        if key == key_from_data:
            isTrue = True
        else:
            isTrue = False
    all_keys_from_data = deep_find_keys_from_data(data)
    if len(all_keys_from_data) != len(result):
        isTrue = False

    return isTrue