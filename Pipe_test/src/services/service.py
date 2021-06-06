import os

def directoryDict():
    '''Фукнкция которая вернет словарь со ссылками на директории
    формата{key_equipment : directory_link}'''

    s = 'D:/test_directories/%s'
    Ldirs = ['US1', 'US2', 'US4', 'RK1', 'RK2']
    mydict = {}
    for directory in Ldirs:
        mylink = 'D:/test_directories/%s' %directory
        mydict[directory] = mylink
    return mydict

dir_dict = directoryDict()
uniqueFileNameList = []

def findUniqFileName(directory_dict, uniqueFileNameList):
    '''Функция сбора всех уникальных имен файлов по директориям
     вернет множество'''

    for directory in directory_dict:
        uniqueFileNameList += os.listdir(directory_dict[directory])
    uniqueFileNameList = set([item.split('.')[0] for item in uniqueFileNameList])
    return uniqueFileNameList

uniqueFileNameList = findUniqFileName(dir_dict, uniqueFileNameList)

def buildSpecialData():
    '''Функция сбора ссылок в словарь формата
    {
    name(для заполнения в строки) :
    {equipment(для заполнения в столбцы) : link}
    }'''
    specialData = {}
    link_list = []
    for directory in os.listdir('D:/test_directories'):
        for pipe_file_name in os.listdir('D:/test_directories/%s' %directory):
            if pipe_file_name.split('.')[0] not in specialData:
                specialData[pipe_file_name.split('.')[0]] = {directory :'D:/test_directories/%s/%s'%(directory, pipe_file_name)}
            else:
                specialData[pipe_file_name.split('.')[0]].update({directory :'D:/test_directories/%s/%s'%(directory, pipe_file_name)})

    return specialData

