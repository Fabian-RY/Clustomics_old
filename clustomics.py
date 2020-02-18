# -*- coding: utf-8 -*-

import flask
import datetime as dt

import matplotlib.pyplot as plt

import database
import clustering

import pandas as pd 
import seaborn 

algs = {0: 'K-means', 
        1:'Hierarchichal'}

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'projects'

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

def plot(list_info, list_group, path):
    data_numbers=pd.DataFrame(list_info)
    data_group=pd.DataFrame(list_group,columns=["grupo"])

    number_groups=len(set(data_group["grupo"]))

    colors=seaborn.color_palette(palette="Set1", n_colors=number_groups)

    color=[]
    for i in range(len(data_group)):
        color.append(colors[data_group["grupo"][i]])

    plt.scatter(x=data_numbers[data_numbers.columns[0]],y=data_numbers[data_numbers.columns[1]],color=color)
    
    plt.savefig(path)

@app.route('/<user>/<proj>')
def project_info(user, proj):
    project_ = database.get_info_from_project(proj)
    print(project_)
    results = database.get_result_from_project(proj)
    return flask.render_template('project.html', 
                                     project=project_[0], 
                                     results=results,
                                     username=user)
@app.route('/<user>/<project>/new_run', methods=['POST'])
def new_run(user, project):
    f = flask.request.files['file']
    f.save('ajsd.csv')
    f = open('ajsd.csv')
    array = []
    for line in f:
        data = line.split()
        data = tuple(float(x) for x in data)
        array.append(data)
    date = str(dt.datetime.now())[:-7]
    print(flask.request.form)
    algorithm = int(flask.request.form['algorithm'])
    groups = int(flask.request.form['groups'])
    distance = flask.request.form['distance']
    linkage = flask.request.form['type']
    print(groups, distance, linkage)
    result = clustering.cluster(array, groups, distance, linkage )
    id_ = database.get_id_from_project(project, user)[0]['id_project']
    group_name = database.get_id_from_project(project, user)[0]['group_name']
    path = str(user+'_')
    database.save_result(id_, project, float(result[1]), date, algorithm, groups,
                         distance, linkage, group_name, user, path +'.csv')
    points = zip(array, result[0])
    npath = 'static/img/'+path+'.png'
    plot(array, result[0], npath)
    npath= '../../'+npath
    return flask.render_template('run.html',
                                 project_name=project,
                                 algorithm=algs[algorithm],
                                 user_name=user,
                                 date=date,
                                 group_name=group_name,
                                 validation_parameter=float(result[1]),
                                 number_of_groups=groups,
                                 distance=distance,
                                 points=points,
                                 input_=array,
                                 img_path=npath,
                                 groups=result[0],
                                 linkage=linkage)

@app.route('/<user>/<project>/results', methods=['POST','GET'])
def run_results(user, project, id_project, datetime):
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

@app.route('/<user>/settings')
def settings():
    return flask.render_template('settings.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
