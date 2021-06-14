from flask import Flask
from Pipe_test.src.gateways.MyFirstMongo import getLinks

pipe_name = '111'

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/names/' + pipe_name)
def getRecordByNamer():
    return getLinks(pipe_name)
