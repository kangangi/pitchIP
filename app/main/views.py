from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''

    title = "The pitcher"
    return render_template('index.html', title = title )