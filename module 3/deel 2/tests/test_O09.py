import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions import getCashInGoldFromPeople

testarg_people_test1 = [{
    'cash' : {
        'platinum' : 1,
        'gold' : 2,
        'silver' : 3,
        'copper' : 12
    }
}]
expected = 2.0
result = getCashInGoldFromPeople(testarg_people_test1)
test('getItemsValueInGold - test 1',expected, result)


testarg_people_test2 = [{
    'cash' : {
        'gold' : 231,
        'platinum' : 2,
        'copper' : 66,
        'silver' : 33
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 11,
        'silver' : 6,
        'copper' : 2
    }
}]
expected = 242.0
result = getCashInGoldFromPeople(testarg_people_test2)
test('getItemsValueInGold - test 2',expected, result)


testarg_people_test3 = [{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
}]
expected = 0.0
result = getCashInGoldFromPeople(testarg_people_test3)
test('getItemsValueInGold - test 3',expected, result)


if __name__ == "__main__":
    report()