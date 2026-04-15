def verticalText(userTextInput):
    TempText = str(userTextInput).split()
    answer = []
    auxRow = []
    max_lenght = 0
    newCharacter = 0
    for item in TempText:
        max_lenght = len(item) if len(item) > max_lenght else max_lenght
    while newCharacter < max_lenght:
        auxRow = []
        for item in TempText:
            if newCharacter < len(item):
                auxRow.append(item[newCharacter])
            else:
                auxRow.append(" ")
        answer.append(auxRow)
        newCharacter +=1
    return answer

def test_VerticalTest_1():
    result = verticalText("Holy bananas")
    expected = [
        ["H", "b"],
        ["o", "a"],
        ["l", "n"],
        ["y", "a"],
        [" ", "n"],
        [" ", "a"],
        [" ", "s"]
    ]
    assert result == expected
def test_VerticalTest_2():
    result = verticalText("Hello fellas")
    expected = [
        ["H", "f"],
        ["e", "e"],
        ["l", "l"],
        ["l", "l"],
        ["o", "a"],
        [" ", "s"]
    ]
    assert result == expected
def test_VerticalTest_3():
    result = verticalText("Python")
    expected = [
        ["P"],
        ["y"],
        ["t"],
        ["h"],
        ["o"],
        ["n"]
    ]
    assert result == expected
def test_VerticalTest_4():
    result = verticalText("")
    expected = []
    assert result == expected
def test_VerticalTest_5():
    result = verticalText("Hello   world")
    expected = [
        ["H", "w"],
        ["e", "o"],
        ["l", "r"],
        ["l", "l"],
        ["o", "d"]
    ]
    assert result == expected

print(test_VerticalTest_1())
print(test_VerticalTest_2())
print(test_VerticalTest_3())
print(test_VerticalTest_4())
print(test_VerticalTest_5())
# print(verticalText("Holy bananas big and yellow"))
