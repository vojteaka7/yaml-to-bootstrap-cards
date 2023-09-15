from yaml import load, dump
import sys
from jinja2 import PackageLoader, select_autoescape
import jinja2

# Jinja2 setup
env = jinja2.Environment(
    loader=PackageLoader("load_yaml"),
    autoescape=select_autoescape()
)
template = env.get_template('cards.html')

# PyYAML setup
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# load the data file
with open(f'{sys.argv[1]}.yaml', encoding='utf-8') as f:
    zadani = load(f.read(), Loader)

# how many columns?
columns = int(sys.argv[2])

output = template.render(cards=zadani, columns=columns)

with open(f'{sys.argv[1]}.html', 'w', encoding='utf-8') as f:
    f.write(output)
