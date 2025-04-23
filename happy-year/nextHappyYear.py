# Happy Year
# A happy year is a year that has all distinct digits (no repeated digits).
def is_happy_year(year:int):
    while True:
        digits = str(year)
        if len(set(digits)) == len(digits):
            return year
        year += 1

print("Enter a year:")
year = int(input())
print(f"{is_happy_year(year +1)} is the next happy year with all numbers being different.")