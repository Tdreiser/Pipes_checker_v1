import Pipe_test.src.controllers.helloController as helloController
import Pipe_test.src.gateways.MyFirstMongo as MyFirstMongo
import Pipe_test.src.gateways.MyFirstSql as MyFirstSql
import Pipe_test.src.services.service as service

if __name__ == '__main__':
    MyFirstSql.bdconstructor(MyFirstSql.data_base, MyFirstSql.cursor)
    for name in service.uniqueFileNameList:  # note: заполнение в БД записей с именами существующих труб
        MyFirstSql.addNameIntoBaseSQL(MyFirstSql.data_base, MyFirstSql.cursor, name)
        MyFirstMongo.addNameIntoBaseMONGO(MyFirstMongo.myCollection, name)

    MyFirstSql.addlinkIntoSQL(service.buildSpecialData(service.dirList, service.workDir),\
                              MyFirstSql.cursor, MyFirstSql.data_base)
    MyFirstMongo.addLinkIntoMONGO(MyFirstMongo.myCollection,\
                                  service.buildSpecialData(service.dirList, service.workDir))

    helloController.app.run()
