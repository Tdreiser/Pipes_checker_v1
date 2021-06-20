import os
from Pipe_test.src.services.settingsParser import workDir

dirList = os.listdir(workDir)

def directoryDict(directoryList, workingDirectory):
    '''Фукнкция которая вернет словарь со ссылками на директории
    формата{key_equipment : directory_link}'''

    mydict = {}
    for directory in directoryList:
        mylink = workingDirectory + '%s' % directory
        mydict[directory] = mylink
    return mydict

dir_dict = directoryDict(dirList,workDir)
uniqueFileNameList = []

def findUniqFileName(directory_dict, uniqueFileNameList):
    '''Функция сбора всех уникальных имен файлов по директориям
     вернет множество'''

    for directory in directory_dict:
        uniqueFileNameList += os.listdir(directory_dict[directory])
    uniqueFileNameList = set([item.split('.')[0] for item in uniqueFileNameList])
    return uniqueFileNameList

uniqueFileNameList = findUniqFileName(dir_dict, uniqueFileNameList)

def buildSpecialData(dirList,workingDirectory):
    '''Функция сбора ссылок в словарь формата
    {
    name(для заполнения в строки) :
    {equipment(для заполнения в столбцы) : link}
    }'''

    specialData = {}
    for directory in dirList:
        for pipe_file_name in os.listdir(workingDirectory + '%s' % directory):
            if pipe_file_name.split('.')[0] not in specialData:
                specialData[pipe_file_name.split('.')[0]] = {directory: workingDirectory +\
                                                                        '%s/%s' % (directory, pipe_file_name)}
            else:
                specialData[pipe_file_name.split('.')[0]].update({directory: workingDirectory +\
                                                                             '%s/%s' % (directory, pipe_file_name)})

    return specialData

