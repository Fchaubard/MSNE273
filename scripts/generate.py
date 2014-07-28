#!/usr/bin/env python

import os
import datetime
from jinja2 import Environment, FileSystemLoader

#TMPL_FILES = ['index.html', 'resources.html', 'schedule.html', 'papers.html']
TMPL_FILES = ['index.html','syllabus.html','policies.html','mentors.html','resources.html', 'faq.html']
TMPL_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '../templates'))
OUTPUT_PATH = os.path.realpath(os.path.join(TMPL_DIR, '../deploy'))

def get_page_name(tmpl_file_name):
    return os.path.splitext(tmpl_file_name)[0].lower()

def get_base_params():
    return {'last_modified': datetime.date.today()}

def generate(tmpl_base, tmpl_files, dest_path):
    env = Environment(loader=FileSystemLoader(tmpl_base))
    params = get_base_params()

    for tmpl_name in tmpl_files:
        tmpl = env.get_template(tmpl_name)
        out_file = os.path.join(dest_path, os.path.basename(tmpl_name))
        print('Generating: %s'%out_file)
        params['page_name'] = get_page_name(tmpl_name)
        open(out_file, 'wb').write(tmpl.render(**params))

if __name__=='__main__':
    generate(TMPL_DIR, TMPL_FILES, OUTPUT_PATH)

