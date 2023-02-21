from src.module import mysql_db
from fastapi import Response,status

def getGroupedValues(grouped_value_one = None,grouped_value_two = None):
    group_by = None
    sorted_dict = {}
    try:
        if grouped_value_one == None != grouped_value_two:
            group_by = grouped_value_two
            print(group_by)
        elif grouped_value_one != None == grouped_value_two:
            group_by = grouped_value_one
            print(group_by)
        elif grouped_value_one != None != grouped_value_two:
            sorted_dict = createDictValue(grouped_value_one)
            
            for key,val in sorted_dict.items():
                
                previous_value =''
                print(sorted_dict[key])
                second_sorted_dict = {}
                for detail in sorted_dict[key]:
                    if previous_value != detail[grouped_value_two]:
                        previous_value = detail[grouped_value_two]
                        second_sorted_dict[detail[grouped_value_two]] = [detail]
                    else:
                        second_sorted_dict.get(previous_value).append(detail)
                # print(f'==>{second_sorted_dict}')
                sorted_dict[key] = second_sorted_dict
                
                    # print(sorted_dict.get(key))
                    # for x in sorted_dict.get(key):
                    #     print(x)
                    # if previous_value != value[grouped_value_two]:
                    #     previous_value = value[grouped_value_two]
                    #     sorted_dict[value[grouped_value_two]] = [value]
                    # else:
                    #     sorted_dict.get(value.get(grouped_value_two))
                    #     print(f'value =>{sorted_dict}')
                    # print(f'====>>>>{sorted_dict}')
        else:
            print('hello')
            payments = mysql_db.getAllData()
            sorted_dict['result'] = payments
        if group_by != None:
            sorted_dict = createDictValue(group_by)
        return sorted_dict
    except Exception as ex:
        print(ex)

def createDictValue(group_by,payments = None):
    previous_value = ''
    sorted_list = []
    sorted_dict = {}
    try:
        if payments == None:
            payments =  mysql_db.groupBySingleValue(group_by)
        for payment in payments:
            detail = dict() 
            detail['amount'] = payment[0]
            detail['pay'] = payment[1]
            detail['place'] = payment[2]
            detail['paymentReason'] = payment[3]
            detail['IFSCcode'] = payment[4]
            detail['ID'] = payment[5]
            detail['entryTime'] = payment[6]
            detail['status'] = payment[7]
            detail['currencyType'] = payment[8]
            sorted_list.append(detail)
        for detail in sorted_list:
            if previous_value != detail[group_by]:
                previous_value = detail[group_by]
                sorted_dict[detail[group_by]] = [detail]
            else:
                sorted_dict.get(previous_value).append(detail)
        return sorted_dict
    except Exception as ex:
        print(ex)