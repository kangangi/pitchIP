from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''

    title = "The pitcher"
    return render_template('index.html', title = title )

@main.route('/pitches')
@login_required
def pitches():
    '''
    View pitches page function that displays the picthes available
    '''
    return render_template('pitches.html')