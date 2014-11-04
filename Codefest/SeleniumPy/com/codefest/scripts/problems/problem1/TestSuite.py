__author__ = 'sandeeps'

from com.codefest.scripts.common.Utilities import Utilities

class TestSuite():
    serve = Utilities()

    def testParkingCost(self, record, actual_cost, expected_cost):

            if actual_cost == expected_cost:
                print 'testParkingCost: Passed'
                result = 'Passed'
                comments = 'Well done! Parking Cost is correct!'
            elif actual_cost != expected_cost:
                print 'testParkingCost: Failed: Cost is not as per expected!'
                result = 'Failed'
                comments = 'Cost is not as per expected!'

            print('---------------------------------------------------------------')

            testresult = ['testParkingCost', record[0], record[1], record[2], record[3], record[4], str(actual_cost), str(expected_cost), ' - ', ' - ', result, comments]

            TestSuite.serve.writeCSV(testresult)

    def testParkingTime(self, record, actual_time,expected_time):
        if actual_time == expected_time:
            print 'testParkingTime: Passed'
            result = 'Passed'
            comments = 'Well done! Parking Time is correct!'
        elif actual_ptime != expected_time:
            print 'testParkingTime: Failed: Parking Time is not as per expected!'
            result = 'Failed'
            comments = 'Parking Time is not as per expected!'

        print('---------------------------------------------------------------')

        testresult = ['testParkingTime', record[0], record[1], record[2], record[3], record[4], '-', '-', str(actual_time), str(expected_time), result, comments]

        TestSuite.serve.writeCSV(testresult)
