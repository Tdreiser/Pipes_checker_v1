import sqlite3
data_base = sqlite3.connect(r'c:/code/venv/sql_datatbase/sql_db.db')
cursor = data_base.cursor()


def bdconstructor(data_base,cursor):
    '''Создаем таблицу в БД с ссылками'''

    cursor.execute(''' CREATE TABLE IF NOT EXISTS pipes_test (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    link_US1 TEXT,
                    link_US2 TEXT,
                    link_US4 TEXT,
                    link_RK1 TEXT,
                    link_RK2 TEXT,
                    UNIQUE (name) ON CONFLICT REPLACE)''')
    data_base.commit()


def addNameIntoBaseSQL(data_base, cursor, name):
    '''функция которая добавит запись в БД с пустыми полями кроме поля name'''

    cursor.execute(''' 
    INSERT INTO pipes_test (name) 
    values('%s')''' % name
                   )
    data_base.commit()


def addlinkIntoSQL (specialData,cursor,data_base):
    ''' Функция которая кладет ссыылки в БД
    {
    name(для заполнения в строки) :
    {equipment(для заполнения в столбцы) : link}
    }'''

    for name in specialData:
        for directory in specialData[name]:
            link = specialData[name][directory]
            cursor.execute( '''
            UPDATE pipes_test
            set 'link_%s' = '%s'
            WHERE name = %s
            '''% (directory, link, name))
    data_base.commit()

def getRecordByNameSQL(cursor,name):
    '''Ф - я вернет список имеющихся записей труб в БД'''

    cursor.execute( ''' 
    SELECT * FROM pipes_test
    WHERE name = %s '''%name )
    li = []
    for item in cursor.fetchall():
        li.append(item)
    return li


