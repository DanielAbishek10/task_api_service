from src.module import mysql_db
from fastapi import Response,status
from operator import itemgetter

def getGroupedValues(user,grouped_value_one = None,grouped_value_two = None):
    group_by = None
    list_of_object =[]
    result = {}
    data ={}
    sorted_dict ={}
    sort = []
    try:
        if grouped_value_one == None != grouped_value_two:
            group_by = grouped_value_two
        elif grouped_value_one != None == grouped_value_two:
            group_by = grouped_value_one
        elif grouped_value_one != None != grouped_value_two:
            returned_dict = createDictValue(user,grouped_value_one,grouped_value_two)
            
            for key in returned_dict:
                grouped_one = key
                records = grouped_one['record']

                sorted_list =[]
                count = 0
                previous_value =''
                for detail in records:  
                    if previous_value != detail[grouped_value_two]:
                        if sorted_dict:
                            sort.append(sorted_dict)

                            sorted_dict = {}
                        previous_value = detail[grouped_value_two]
                        sorted_dict['name'] = f"{grouped_one['name']} - {previous_value}"
                        sorted_dict['record'] = [detail]
                        sorted_dict['count'] = len(sorted_dict['record'])
                        
                    else:
                        sorted_dict.get('record').append(detail)
                        sorted_dict['count'] = len(sorted_dict['record'])

                    count += 1
                    if count == len(records):
                        sort.append(sorted_dict)
                        sorted_dict = {}                            
            result['data'] = sort
                
        else:
            payments = mysql_db.getAllData(user)
            data['name'] = 'all'
            data['count'] = len(payments)
            data['record'] = payments
            list_of_object.append(data)
            result['data'] = list_of_object
        if group_by != None:
            list_of_object = createDictValue(user,group_by)
            result['data'] = list_of_object

        return result
    except Exception as ex:
        print(ex)

def createDictValue(user,group_by_one,group_by_two=None, payments =None):
    previous_value = ''
    sorted_list = []
    sorted_dict = {}
    count = 0
    count1 = 0
    
    try:
        if payments == None:
            payments =  mysql_db.groupBySingleValue(user, group_by_one,group_by_two)
       
        for detail in payments:
            if previous_value != detail[group_by_one]:
               if sorted_dict:
                sorted_list.append(sorted_dict)
                sorted_dict = {}
               previous_value = detail[group_by_one]
               sorted_dict['name'] = previous_value
               sorted_dict['record'] = [detail]
               sorted_dict['count'] = len(sorted_dict['record'])
                
            else:
                sorted_dict.get('record').append(detail)
                sorted_dict['count'] = len(sorted_dict['record'])

            count += 1
            if count == len(payments):
                sorted_list.append(sorted_dict)
                sorted_dict = {}
        print(sorted_list)
        return sorted_list
    except Exception as ex:
        print(ex)

def getSortedData(user,cardName:str, column,column_one,page_no,no_of_data, column_two=None, is_sorted:bool = False,):
    filter_one = None
    filter_two = None
    list_of_name = cardName.split(' - ')
    if(len(list_of_name)>1):
        filter_one = list_of_name[0]
        filter_two = list_of_name[1]
        print('hello')
    # filter_one = cardName.split(' - ')[0]
    else:
        filter_one = cardName
    
        # filter_two= cardName.split('-')[1]
    # print(filter_one,filter_two)
    if filter_one == 'all':
        payment = mysql_db.getSortedDataWithoutConditionFromDb(user,sort_col=column,page_no=page_no,no_of_data=no_of_data)
    else:
        payment = mysql_db.getSortedDataFromDb(user,column_one,filter_one,page_no,no_of_data,column_two,filter_two,column)
    payment = sorted(payment,key=itemgetter(column),reverse=is_sorted)
    return {'record': payment}