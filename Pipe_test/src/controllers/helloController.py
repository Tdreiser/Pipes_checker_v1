from flask import Flask, render_template
from Pipe_test.src.gateways.MyFirstMongo import getLinks , getLinksInDict
from Pipe_test.src.services.settingsParser import templateFolder
pipe_name = '1288619'

app = Flask(__name__, template_folder=templateFolder)

@app.route('/hello')
def hello_world():
    return 'helloworld'


@app.route('/names/%s' % pipe_name)
def getRecordByNamer():
    return render_template('Template.html',**getLinksInDict(pipe_name))
