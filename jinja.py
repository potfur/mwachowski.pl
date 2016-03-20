from jinja2 import Environment, FileSystemLoader
import mimetypes, time, re


def date(date_string, date_format):
    return time.strftime(date_format, time.strptime(date_string, '%Y-%m'))


def replace_regex(string, regex, rep):
    return re.sub(regex, rep, string)


def embed(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        return 'data:%s;base64,%s' % (mimetypes.guess_type(file_name)[0], data.encode('base64').replace('\n', ''))


def render(path, template, content):
    env = Environment(
        loader=FileSystemLoader(path),
        extensions=['jinja2.ext.loopcontrols']
    )

    env.filters['date'] = date
    env.filters['replace_regex'] = replace_regex
    env.filters['embed'] = embed

    return env \
        .get_template(template) \
        .render(content) \
        .encode('utf-8')
