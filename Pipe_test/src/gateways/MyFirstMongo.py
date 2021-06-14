import pymongo
from Pipe_test.src.services.settingsParser import mongoUrl

def createMongoDB(mongoUrl):

    client = pymongo.MongoClient(mongoUrl)
    db = client['mongo_db']
    return db


db = createMongoDB(mongoUrl)
myCollection = db.test_pipes


def addNameIntoBaseMONGO(collection, name):
    '''Функция заполнения именами труб в БД
    {name : name}'''
    collection.insert_one({'name': name})


def addLinkIntoMONGO(collection, specialData):
    '''Функция которая кладёт ссылки в БД
    {
    name(для заполенения поля name) :
    {equipment(в поле name новые ссылки) : link}
    }'''
    for name in specialData:
        for directory in specialData[name]:
            link = specialData[name][directory]
            collection.update({'name': name}, {'$set': {directory: link}})

def getRecordByNameMONGO(collection, name):
    '''Возвращает строку - ссылкой'''

    return collection.find_one({'name': name})

def getLinks(name):
    '''Возвращает все ссылки связанные с именем файла'''
    # note : есть ли смысл переделать в декоратор для getRecord - семейства функций?
    links = ''
    dicr = getRecordByNameMONGO(myCollection, name)

    for key in dicr.keys():
        if key != 'name' and key != '_id':
            links += str(key) + ' : ' + dicr[key] + ' ' * 10
    return links



