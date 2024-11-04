import base64

from jinja2 import Environment, FileSystemLoader
import mimetypes, re, datetime, dateutil.parser


def nonbreaking(string):
    return string.replace(' ', '&nbsp;').replace('-', '&#8209;')

def date(date_string, date_format):
    return datetime.datetime.strftime(dateutil.parser.parse(date_string) if date_string else datetime.datetime.now(), date_format)


def replace_regex(string, regex, rep):
    return re.sub(regex, rep, string)


def embed(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        return 'data:%s;base64,%s' % (
            mimetypes.guess_type(file_name)[0] or 'application/octet-stream',
            base64.b64encode(bytes(data)).decode("utf-8")
        )


def render(path, template, content):
    env = Environment(
        loader=FileSystemLoader(path),
        extensions=['jinja2.ext.loopcontrols']
    )

    env.filters['date'] = date
    env.filters['replace_regex'] = replace_regex
    env.filters['embed'] = embed
    env.filters['nonbreaking'] = nonbreaking

    return env \
        .get_template(template) \
        .render(content) \
        .encode('utf-8')
