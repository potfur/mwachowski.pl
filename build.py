import mimetypes
from email.utils import formatdate
from jinja2 import Environment, FileSystemLoader

def embed(file):
    with open(file, "rb") as f:
        data = f.read()
        return 'data:' + mimetypes.guess_type(file)[0] + ';base64,' + data.encode('base64').replace('\n', '')

env = Environment(loader=FileSystemLoader('./'))
env.filters['embed'] = embed

template = env.get_template('template.html')

print template.render(authorship="105788185695209510820", analytics="UA-3665481-3", lastmod=formatdate()).encode('utf-8')
