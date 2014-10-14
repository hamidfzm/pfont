from flask import render_template

from app.utilis.decorators import title
from . import mod


@mod.route('/')
@title('Resume')
def index():
    return render_template('index.html')