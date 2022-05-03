from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_article
from ..models import Source,Article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source = get_source()
    return render_template('index.html',source_list=source)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    
    articles = get_article(id)
    return render_template('articles.html',article_list=articles,id=id )
