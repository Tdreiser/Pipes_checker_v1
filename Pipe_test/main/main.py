import Pipe_test.src.controllers.helloController as helloController
import Pipe_test.src.gateways.MyFirstMongo as MyFirstMongo
import Pipe_test.src.services.service as service
from Pipe_test.src.services.service import workDir

if __name__ == '__main__':

    #for name in service.uniqueFileNameList:  # заполнение в БД записей с именами существующих труб / КОТОРАЯ ПЛОДИТ КЛОНОВ
#
    #    MyFirstMongo.addNameIntoBaseMONGO(MyFirstMongo.myCollection, name)


    MyFirstMongo.addLinkIntoMONGO(MyFirstMongo.myCollection, service.buildSpecialData(service.dirList,workDir))
    helloController.app.run()
