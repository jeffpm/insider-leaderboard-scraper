from jinja2 import Environment, FileSystemLoader
import tabulate

import logging
import os

def make_leaderboard_page(scores_list):
    logging.info("producing html table")
    try:
        html_table = tabulate.tabulate(scores_list, headers="firstrow", tablefmt="html", colalign=(None,None,None))
    except Exception as e:
        logging.error(e)
        html_table = "<h2>No scores yet!</h2>"

    # root = "../" + os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join('templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('index.html')

    filename = os.path.join('index.html')
    with open(filename, 'w') as fh:
        fh.write(template.render(
            table = html_table
        ))
    logging.info("wrote html file")
