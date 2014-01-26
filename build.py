# coding: utf-8

import mimetypes, time
from jinja2 import Environment, FileSystemLoader
from content import content

def date(str, format):
    return time.strftime(format, time.strptime(str, '%Y-%m'))

def embed(file):
    with open(file, 'rb') as f:
        data = f.read()
        return 'data:' + mimetypes.guess_type(file)[0] + ';base64,' + data.encode('base64').replace('\n', '')

env = Environment(loader=FileSystemLoader('./'))
env.filters['date'] = date
env.filters['embed'] = embed

template = env.get_template('template.html')
print template.render(content).encode('utf-8')
