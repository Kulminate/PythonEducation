from SomeNumber import SomeNumber

class TestSomeNumber:

    test_list: list = (-10, -1, 0, 1, 15)

    @staticmethod
    def test_setN():
        test_list = (-10, -1, 0, 1, 15)
        result_list = []
        for i in test_list:
            if SomeNumber.setN(SomeNumber(i)) == None:
                result_list.append(f'Test number: {i}. Returned None. Test passed')

            else:
                result_list.append(f'Test number: {i}. Returned {SomeNumber.setN(i)}. Test failed')
        print(f'Test list is {test_list}')
        for result in result_list:
            print(result)

    @staticmethod
    def test_is_positive():
        test_list = (-10, -1, 0, 1, 15)
        result_list = []
        for i in test_list:
            if SomeNumber.isPositive(SomeNumber(i)) == 'positive' and i > 0 \
            or SomeNumber.isPositive(SomeNumber(i)) == 'negative' and i < 0 \
            or SomeNumber.isPositive(SomeNumber(i)) == 'null' and i == 0:
                result_list.append(f'Test number: {i}. Returned {SomeNumber.isPositive(SomeNumber(i))}. Test passed')

            else:
                result_list.append(f'Test number: {i}. Returned {SomeNumber.isPositive(SomeNumber(i))}. Test failed')
        print(f'Test list is {test_list}')
        for result in result_list:
            print(result)








