from flask import Flask
import gateways.MyFirstSql as MyFirstSql

app = Flask(__name__)
linker = ''
for link in MyFirstSql.getRecordByNameSQL(MyFirstSql.cursor, '111')[0][2:]:
    if not link:
        continue
    linker += link + '\n'


@app.route('/hello')
def hello_world():
    return 'Hello World!'
@app.route('/names')
def getRecordByNamer() :
    return linker