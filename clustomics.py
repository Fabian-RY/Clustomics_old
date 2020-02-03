# -*- coding: utf-8 -*-

import flask

import database
import pymysql

app = flask.Flask(__name__)

@app.route('/')
def clustomics():
    return '<h1>Clustomics main page</h1>'

@app.route('/<user>', methods=['GET','POST'])
def projects(user):
    user_projects = database.get_projects_from_user(user)
    print(user_projects)
    return flask.render_template('my_projects.html', projects=user_projects)

@app.route('/<user>/settings')
def setttings(user):
    user_projects = database.get_projects_from_user(user)
    text = '<h1>Welcome, '+user+'</h1><br />'
    #for project in user_projects:
        #pass
    return text


@app.route('/<user>/new_project', methods=['POST'])
def new_project(user):
    name = 'test_project'
    group = 'test_group'
    database.create_new_project(user, name, group)
    return 'New Project'

@app.route('/login', methods=['GET', 'POST'])
def login():
    return flask.render_template('template_login.html')

@app.route('/signup')
def signup():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)