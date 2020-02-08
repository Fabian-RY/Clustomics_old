# -*- coding: utf-8 -*-

import flask
import datetime as dt

import database

app = flask.Flask(__name__)

@app.route('/')
def clustomics():
    return '<h1>Clustomics main page</h1>'

@app.route('/<user>', methods=['GET','POST'])
def projects(user):
    user_projects = database.get_projects_from_user(user)
    response = flask.render_template('my_projects.html', projects=user_projects, username=user)
    return response

@app.route('/<user>/settings')
def settings(user):
    user_info = database.get_info_from_user(user)
    text = '<h1>Welcome, '+user+'</h1><br />'
    #for project in user_projects:
        #pass
    return text

@app.route('/<user>/<proj>')
def project_info(user, proj):
    project_ = database.get_info_from_project(proj)
    results = database.get_result_from_project(proj)
    print(project_)
    return flask.render_template('project.html', 
                                     project=project_[0], 
                                     results=results,
                                     username=user)
    
@app.route('/<user>/<project>/new_run', methods=['GET','POST'])
def new_run(user, project):
    print(user, project)
    date = dt.datetime.now()[:-7]
    data = database.get_info_from_project(project)
    print(data, date)
    return user

@app.route('/<user>/new_project', methods=['POST'])
def new_project(user, name, group):
    database.create_new_project(user, name, group)
    return flask.url_for('projects', user=user)


@app.route('/<user>/<project>/results', methods=['POST','GET'])
def run_results(id_project, datetime, user):
    run = database.get_run_results(id_project, datetime, user)
    run=run[0]
    return flask.render_template('run.html', 
                                     project_name=run['project_name'], 
                                     algorithm=run['algo_rithm'],
                                     user_name=run['user'],
                                     group_name=run['group_name'],
                                     validation_parameter=run['validation_result'],
                                     number_of_groups=run['groups'],
                                     distance=run['distance'],
                                     linkage=run['linkage'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    return flask.render_template('template_login.html')

@app.route('/signup')
def signup():
    return "Sign up"

@app.route('/about_us')
def about():
    return flask.render_template('about_us.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
