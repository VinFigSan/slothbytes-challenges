def dailyTemperatures(temperaturesList):
    countDaysOutput = []
    for days in range(len(temperaturesList)):
        foundHigher = 0
        for nextDay in range(days + 1, len(temperaturesList)):
            if temperaturesList[days] < temperaturesList[nextDay]:
                foundHigher = nextDay - days
                break
        countDaysOutput.append(foundHigher)
    return countDaysOutput

def test_dailyTemperature_case1():
    result = (dailyTemperatures([30,38,30,36,35,40,28]))
    expected = ([1,4,1,2,1,0,0])
    assert result == expected
def test_dailyTemperature_case2():
    result = (dailyTemperatures([22,21,20]))
    expected = ([0,0,0])
    assert result == expected
def test_dailyTemperature_case3():
    result = dailyTemperatures([50])
    expected = [0]
    assert result == expected
def test_dailyTemperature_case4():
    result = dailyTemperatures([10,20])
    expected = [1,0]
    assert result == expected
def test_dailyTemperature_case5():
    result = dailyTemperatures([20,10])
    expected = [0,0]
    assert result == expected
def test_dailyTemperature_case6():
    result = dailyTemperatures([30,30,30])
    expected = [0,0,0]
    assert result == expected
def test_dailyTemperature_case7():
    result = dailyTemperatures([10,20,30,40])
    expected = [1,1,1,0]
    assert result == expected
def test_dailyTemperature_case8():
    result = dailyTemperatures([40,30,20,10])
    expected = [0,0,0,0]
    assert result == expected
def test_dailyTemperature_case9():
    result = dailyTemperatures([30,20,10,40])
    expected = [3,2,1,0]
    assert result == expected
def test_dailyTemperature_case10():
    result = dailyTemperatures([30,30,35])
    expected = [2,1,0]
    assert result == expected

# print(dailyTemperatures([30,38,30,36,35,40,28]))
