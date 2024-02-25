from datetime import datetime as dt

from flask import Flask

from data import db_session
from data.jobs import Job

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'


def main():
    app.run()


def add_job():
    job = Job()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = dt.now()
    job.is_finished = False

    session.add(job)
    session.commit()


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    add_job()
    main()
