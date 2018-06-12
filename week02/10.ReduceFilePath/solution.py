import re

def reduce_file_path(path):


    if len(set(path)) == 1:
        return '/'
    if path == '/../':
        return '/'

    while path.endswith('/../'):
        path = re.sub(r'/.*/../', '/', path)
        print(path)


    path = path.replace('./', '/')
    path = re.sub(r'/+', '/', path)
    if path.endswith('/'):
        path = path[:-1]

    return path


#print(reduce_file_path("/etc/../etc/../etc/../"))