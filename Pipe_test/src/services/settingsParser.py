import configparser
settings = configparser.ConfigParser()
settings.read('c:\code\settings.ini')
workDir = settings.get('service','workDir')
mongoUrl = settings.get('mongo','mongoUrl')
sqlDB = settings.get('sql','sqlDB')
