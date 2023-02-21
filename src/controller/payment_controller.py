from fastapi import APIRouter,Response,status
from src.service import payment_service
router = APIRouter()

@router.get('/index')
def index():
    return {'msg': 'empty'}

@router.get('/groupBy',status_code=200)
def getGroupedValues(groupByOne = None, groupByTwo = None):
    if groupByOne == 'undefined' or groupByTwo == 'undefined':
        print('1')
        if groupByOne =='undefined':
            print('2')
            groupByOne = None
        elif groupByTwo == 'undefined':
            print('3')
            groupByTwo = None
        else:
            print('4')
            groupByOne,groupByTwo = None
    try:   
        print(f"group by one = {groupByOne}, group by two = {groupByTwo}")
        result =payment_service.getGroupedValues(groupByOne,groupByTwo)
        print(result)
        return result
    except Exception as ex:
        print(ex)
