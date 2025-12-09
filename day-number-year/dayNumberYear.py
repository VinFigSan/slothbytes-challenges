from datetime import datetime

def dayOfYear(userDateInput:str):
    formatDate = datetime.strptime(userDateInput,"%m/%d/%Y")
    beginDate = datetime(formatDate.year, 1, 1)
    return (formatDate-beginDate).days+1

def test_dayOfYear():
    tests = [
        ("12/13/2020", 348),
        ("11/16/2020", 321),
        ("1/9/2019", 9),
        ("3/1/2004", 61),
        ("12/31/2000", 366),  # leap year
        ("12/31/2019", 365),  # non-leap year
    ]

    all_passed = True
    for date_input, expected in tests:
        result = dayOfYear(date_input)
        if result == expected:
            print(f"Passou no teste: entrada '{date_input}', esperado {expected}, retornou {result}")
        else:
            print(f"FALHOU no teste: entrada '{date_input}', esperado {expected}, retornou {result}")
            all_passed = False

    return all_passed

#print(test_dayOfYear())
userDateInput = input("Enter a day of any year on the following format (month/day/year):")
print(f"{userDateInput} is the {dayOfYear(userDateInput)}º of the year {(datetime.strptime(userDateInput, "%m/%d/%Y")).year}")
