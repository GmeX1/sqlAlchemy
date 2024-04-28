from datetime import datetime as dt

from flask import Flask, render_template

from data import db_session
from data.jobs import Job

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'


@app.route('/')
def main():
    jobs = session.query(Job).all()
    return render_template('main_07.html', jobs=jobs)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    app.run()
