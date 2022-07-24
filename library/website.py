from jinja2 import Environment, FileSystemLoader
import tabulate

import logging
import os

def make_leaderboard_page(scores_list):
    logging.info("producing html table")
    html_table = tabulate.tabulate(scores_list, headers="firstrow", tablefmt="html", colalign=(None,None,None))

    # root = "../" + os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join('templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('index.html')

    filename = os.path.join('html', 'index.html')
    with open(filename, 'w') as fh:
        fh.write(template.render(
            table = html_table
        ))
    logging.info("wrote html file")
