from mysql import connector
from copy import deepcopy as dc
from fastapi import Response, status


mydb = connector.connect(
    host='192.168.3.52',
    port = 3306,
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


def getAllData(user):
    my_cursor = mydb.cursor()
    try:
        my_cursor.execute(f'select * from intellect_repo where place="{user}" order by "ID" ')
        row_headers=[x[0] for x in my_cursor.description]
        results = my_cursor.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers,result)))
        return json_data
    except Exception as ex:
        # res.status_code = status.HTTP_510_NOT_EXTENDED
        print(ex)
    finally:
        my_cursor.close()


def groupBySingleValue(user,group_by,group_by_two = None):
    my_cursor = mydb.cursor()
    
    try:
        if group_by_two == None:
            my_cursor.execute(f'select * from intellect_repo where place="{user}" order by {group_by} asc')
        else:
            my_cursor.execute(f'select * from intellect_repo where place="{user}" order by {group_by} asc, {group_by_two} asc')

        row_headers=[x[0] for x in my_cursor.description]
        payments = my_cursor.fetchall()
        json_data =[]
        for result in payments:
            json_data.append(dict(zip(row_headers,result)))
        return json_data


    except Exception as ex:
        print(ex)
    finally:
        my_cursor.close()

def getSortedDataFromDb(user,column_one,filter_one,page_no,no_of_data,column_two = None,filter_two=None,column='ID'):
    my_cursor = mydb.cursor()
    try:
        if filter_two != None:
            my_cursor.execute(f"select * from intellect_repo where {column_one} = '{filter_one}' and {column_two} = '{filter_two}' and place = '{user}' limit {page_no},{no_of_data}")
        else:
            my_cursor.execute(f"select * from intellect_repo where {column_one} = '{filter_one}' and place='{user}'  limit {page_no},{no_of_data}")
        row_headers=[x[0] for x in my_cursor.description]
        payments = my_cursor.fetchall()
        json_data =[]
        for payment in payments:
            json_data.append(dict(zip(row_headers,payment)))
        print(json_data)
        return json_data
    except Exception as ex:
        print(ex)
    finally:
        my_cursor.close()


def getSortedDataWithoutConditionFromDb(user,sort_col,page_no,no_of_data):
    my_cursor = mydb.cursor()
    try:
        my_cursor.execute(f"select * from intellect_repo where place='{user}' limit {page_no}, {no_of_data}")
        row_headers = [x[0] for x in my_cursor.description]
        payments = my_cursor.fetchall()
        json_data =[]
        for payment in payments:
            json_data.append(dict(zip(row_headers,payment)))
        return json_data
    
    except Exception as ex:
        print(ex)
    finally:
        my_cursor.close()