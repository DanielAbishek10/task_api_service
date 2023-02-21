from mysql import connector
from copy import deepcopy as dc
from fastapi import Response, status


mydb = connector.connect(
    host='192.168.3.208',
    user='root',
    password='Kanyakumari@31',
    database='mysql'
)

def connectDb():
    list_of_tabel = []
    my_cursor = mydb.cursor()
    my_cursor.execute('show tables')
    for table in my_cursor:
        list_of_tabel.append(table)
    return list_of_tabel


def getAllData():
    my_cursor = mydb.cursor()
    try:
        my_cursor.execute('select * from intellect_repo')
        result = my_cursor.fetchall()
        return result
    except Exception as ex:
        # res.status_code = status.HTTP_510_NOT_EXTENDED
        print(ex)
    finally:
        my_cursor.close()


def groupBySingleValue(group_by):
    my_cursor = mydb.cursor()
    
    try:
        my_cursor.execute(f'select * from intellect_repo order by {group_by} asc')
        payments = my_cursor.fetchall()
        return payments


    except Exception as ex:
        print(ex)
    finally:
        my_cursor.close()