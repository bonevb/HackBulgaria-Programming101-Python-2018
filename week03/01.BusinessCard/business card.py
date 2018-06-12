import json


filename = 'data.json'

def open_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

a = open_file(filename)

def generate_head(a, name):
    for i in a['people']:
        if i['first_name'] == name:
            return '<!DOCTYPE html><html><head><title>{} {}</title><link rel="stylesheet" type="text/css" href="styles.css"></head><body>'.format(i['first_name'], i['last_name'])


def generate_class_business_card(a, name):
    for i in a['people']:
        if i['first_name'] == name:
            return  """<div class="business-card male"><h1 class="full-name">{first_name} {last_name}</h1><img class="avatar" src="avatars/{first_name}.png"><div class="base-info"><p>Age: {age}</p><p>Birth date: {date}</p>
            <p>Birth place: {place}</p><p>Gender: {gender}</p></div>""".format(first_name = i['first_name'], last_name = i['last_name'], age = i['age'], date = i['birth_date'], place = i['birth_place'], gender =i['gender']  )




def generate_interests(a, name):
    person_interests = []
    for i in a['people']:
        if i['first_name'] == name:
            person_interests.append(i['interests'])
    result = '<div class="interests"><h2>Interests:</h2><ul>'
    for i in person_interests:
        for j in i:
            result += '<li>{}</li>'.format(j)
    return result + '</ul></div>'


def generate_skills(a, name):
    person_skills = []
    for i in a['people']:
        if i['first_name'] == name:
            person_skills = i['skills']
    result = '<div class="skills"><h2>Skills:</h2><ul>'
    #print(len(person_skills))
    for i in person_skills:
        result += '<li>{skill} - {points}</li>'.format(skill = i['name'], points = i['level'])
    result = result + '</ul></div>'
    return result + '</ul></div></div></body></html>'


def generate_file(name):
    html_file = name+'.html'
    with open(html_file, 'a') as f:
        f.write(generate_head(a, name))
        f.write(generate_class_business_card(a, name))
        f.write(generate_interests(a, name))
        f.write(generate_skills(a, name))

for i in a['people']:
    generate_file(i['first_name'])




#print(generate_head(a, 'Ivo'))
#print(generate_class_business_card(a, 'Ivo'))
#print(generate_interests(a, 'Ivo'))
#print(generate_skills(a, 'Ivo'))
#generate_file('Ivo')



