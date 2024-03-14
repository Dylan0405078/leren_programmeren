import sys, os
from test_lib import test, report
from data import JOURNEY_IN_DAYS
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


expected = 10
result = JOURNEY_IN_DAYS
test('Journey in days test',expected, result)

   


if __name__ == "__main__":
    report()