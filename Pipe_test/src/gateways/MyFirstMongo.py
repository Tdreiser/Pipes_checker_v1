import pymongo


def createMongoDB():

    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['mongo_db']
    return db


db = createMongoDB()
Mycollection = db.test_pipes


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
    return collection.find_one({'name': name})





