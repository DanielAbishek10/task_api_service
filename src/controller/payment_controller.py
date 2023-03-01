from fastapi import APIRouter,Response,status
from src.service import payment_service
router = APIRouter()

@router.get('/index')
def index():
    return {'msg': 'empty'}

@router.get('/groupBy',status_code=201)
def getGroupedValues(user,groupByOne=None, groupByTwo=None):
    if groupByOne == 'undefined' or groupByTwo == 'undefined':
        if groupByOne =='undefined' and groupByTwo != 'undefined':
            groupByOne = None
        elif groupByTwo == 'undefined' and groupByOne != 'undefined':
            groupByTwo = None
        else:
            groupByOne,groupByTwo = None,None
    try:   
        print(f"group by one = {groupByOne}, group by two = {groupByTwo}")
        result =payment_service.getGroupedValues(user,groupByOne,groupByTwo)
        return result
    except Exception as ex:
        print(ex)

@router.get('/sortData')
async def getSortedData(user,cardName, page_no, no_of_data, column='ID', column_one=None, column_two=None, is_sorted:bool = False):
    print(user,cardName, column,column_one,page_no,no_of_data, column_two, is_sorted)
    return payment_service.getSortedData(user,cardName, column,column_one,page_no,no_of_data, column_two, is_sorted)