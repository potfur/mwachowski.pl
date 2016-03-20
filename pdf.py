# coding: utf-8
import argparse

import pdfkit
from content import content
from jinja import render


def build():
    parser = argparse.ArgumentParser(description='Generate PDF resume.')
    parser.add_argument('-o', dest='output_file', default='cv.pdf', help='Output file')
    args = parser.parse_args()

    html = render('./pdf/', 'template.html', content)
    pdfkit.from_string(html, args.output_file, options=dict(encoding="UTF-8"))


if __name__ == '__main__':
    build()
