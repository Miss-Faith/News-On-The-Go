from flask import render_template
from . import main
from ..request import get_source
from ..models import Source

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source = get_source()
    return render_template('index.html',source_list=source)