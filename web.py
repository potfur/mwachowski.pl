# coding: utf-8
import argparse

from content import content
from jinja import render


def build():
    parser = argparse.ArgumentParser(description='Generate HTML resume.')
    parser.add_argument('-o', dest='output_file', default='index.html', help='Output file')
    args = parser.parse_args()

    html = render('./web/', 'template.html', content)
    with open(args.output_file, 'wb') as file:
        file.write(html)


if __name__ == '__main__':
    build()
