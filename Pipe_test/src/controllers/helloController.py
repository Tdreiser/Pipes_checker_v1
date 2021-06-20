from flask import Flask, render_template, url_for
from Pipe_test.src.gateways.MyFirstMongo import getLinks , getLinksInDict
from Pipe_test.src.services.settingsParser import templateFolder
from Pipe_test.src.services.service import uniqueFileNameList
#pipe_name = '1288619'

app = Flask(__name__, template_folder = 'c:/code/Pipes_checker_v1/Pipe_test/templates')

@app.route('/hello')
def hello_world():
    return 'helloworld'

@app.route('/files')
def getAllRecords():
    """Вернет шаблон со всеми записями"""
    allRecordsList = []
    for name in uniqueFileNameList:
        allRecordsList.append(getLinksInDict(name))
    return render_template('TemplateForManyPipes.html', allRecords = allRecordsList)


@app.route('/files/<pipe_name>/')
def getRecordByNamer(pipe_name):
    """Вернет шаблон с одной записью pipe_name"""
    return render_template('TemplateForOnePipe.html',**getLinksInDict(pipe_name))

