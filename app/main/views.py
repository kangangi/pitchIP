from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from app.models import User, Pitch, Category, Comment
from .forms import UpdateProfile,addPitch,addComment
from .. import db, photos
from datetime import datetime

@main.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    categories = Category.query.all()
    title = "The pitcher"
    return render_template('index.html', title = title, categories = categories )

@main.route('/pitches/<category_id>')
def pitches_by_category(category_id):
    '''
    View pitches page function that displays the picthes available
    '''
    pitches = Pitch.get_category_pitch(category_id)

    return render_template('pitches.html', pitches = pitches)

@main.route('/user/ <uname>/addpitch',methods =['GET', 'POST'])
@login_required
def add_pitch(uname):
    title = "Add pitch"
    form = addPitch()
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    if form.validate_on_submit():
        title = form.title.data
        categorydata = form.category.data
        category_id = (Category.get_category_name(categorydata))
        description = form.description.data
        upvotes = 0
        downvotes = 0
        
        
        new_pitch = Pitch(title=title, category_id = category_id, description = description, user = user, upvotes = upvotes, downvotes = downvotes)
        new_pitch.save_pitch()
        return redirect(url_for("main.index"))


    return render_template("addpitch.html", form = form, title = title)
        


@main.route('/user/<uname>')
def profile(uname):
    user = User. query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    pitches = Pitch.get_user_pitch(user.id)

    return render_template("profile/profile.html", pitches = pitches , user = user)


@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_url = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))

@main.route("/<user>/<pitch_id>/add/comment", methods = ['GET', 'POST'])
@login_required
def comment(user,pitch_id):
    user= User.query.filter_by(id = user).first()
    user_id = user.id
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    pitcher_id = pitch.id
    print('-'*75)
    print(pitcher_id)
    title = "Add Comment"
    form = addComment()
    if form.validate_on_submit:
        content = form.content.data
        new_comment = Comment(content= content, user_id = user_id, pitch_id = pitcher_id)
        new_comment.save_comment()

        return redirect(url_for('main.index'))

    return render_template("addcomment.html", title = title, form = form, pitch = pitch)
