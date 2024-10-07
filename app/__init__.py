from jinja2 import Environment, FileSystemLoader
from typer import Typer

env = Environment(loader=FileSystemLoader('app/templates/'))
app = Typer(no_args_is_help=True)

from .compiler import app as compile_app
app.add_typer(compile_app, name="compile")
