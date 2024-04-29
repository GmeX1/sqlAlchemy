from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from werkzeug.security import generate_password_hash
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'


class RegiterForm(FlaskForm):
    login = StringField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password_repeat', message='Пароли должны совпадать!')
    ])
    password_repeat = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = DecimalField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def main():
    reg_form = RegiterForm()
    if request.method == 'POST' and reg_form.validate_on_submit():
        if len(list(session.query(User).filter(User.email == reg_form.login.data))) > 0:
            return 'Такой пользователь уже существует!'
        user = User()
        user.surname = reg_form.surname.data
        user.name = reg_form.name.data
        user.age = int(reg_form.age.data)
        user.position = reg_form.position.data
        user.speciality = reg_form.speciality.data
        user.address = reg_form.address.data
        user.email = reg_form.login.data
        user.set_password(reg_form.password.data)
        session.add(user)
        session.commit()
    return render_template('home_06.html', form=reg_form)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    app.run()
