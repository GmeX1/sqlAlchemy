from flask import Flask

from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'


def main():
    app.run()


def add_users():
    global session
    users = [User() for _ in range(4)]

    users[0].surname = "Scott"
    users[0].name = "Ridley"
    users[0].age = 21
    users[0].position = "captain"
    users[0].speciality = "research engineer"
    users[0].address = "module_1"
    users[0].email = "scott_chief@mars.org"
    users[0].hashed_password = "cap"

    users[1].surname = "Sanders"
    users[1].name = "Teddy"
    users[1].age = 23
    users[1].position = "colonist"
    users[1].speciality = "programmer"
    users[1].address = "module_2"
    users[1].email = "teddy_san@mars.org"
    users[1].hashed_password = "progmastah"

    users[2].surname = "Newell"
    users[2].name = "Gabe"
    users[2].age = 48
    users[2].position = "colonist"
    users[2].speciality = "resource manager"
    users[2].address = "module_3"
    users[2].email = "gaben@mars.org"
    users[2].hashed_password = "manana"

    users[3].surname = "Scott"
    users[3].name = "Travis"
    users[3].age = 25
    users[3].position = "colonist"
    users[3].speciality = "journalist"
    users[3].address = "module_4"
    users[3].email = "travvis@mars.org"
    users[3].hashed_password = "ISTHATTRAVISSCOTT"

    session.add_all(users)
    session.commit()


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    add_users()
    main()
