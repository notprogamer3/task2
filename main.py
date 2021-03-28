from flask import Flask
from flask import render_template
from data import db_session, users, jobs
from data.users import User
from  data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    job1s = db_sess.query(Jobs).all()
    return render_template('index.html', j=job1s)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')