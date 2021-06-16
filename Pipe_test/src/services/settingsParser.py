import configparser
settings = configparser.ConfigParser()
settings.read('C:\code\Pipes_checker_v1\settings.ini')
workDir = settings.get('service','workDir')
mongoUrl = settings.get('mongo','mongoUrl')
templateFolder = settings.get('template','templateFolder')