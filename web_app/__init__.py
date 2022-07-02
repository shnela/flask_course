import os

from flask import Flask, render_template, request, session, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, field):
        if field.data and field.data.lower() == 'admin':
            raise ValidationError("You can't log in as admin")


@app.route('/')
def index():
    user_info = {
        'name': session.get('name', 'Unknown'),
        'age': int(request.args.get('age', 42)),
    }
    return render_template('index.html', user_info=user_info)


@app.route('/user/<username>/<int:amount>/')
def profile(username, amount):
    return render_template('profile.html', username=username, amount=amount)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # show diff between GET and POST
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('auth/login.html', form=form)
