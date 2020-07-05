# 1. Create a variable, paragraph, that has the following content:
# "Python is a great language!", said Fred. "I don't ever remember
# having this much fun before."

paragraph = """
Python is a great language!", said Fred. "I don't ever remember
having this much fun before.
"""
print(paragraph)

# 2. Write an if statement to determine whether a variable holding a year
# is a leap year.


def leapYearFinder(num):
    leapYear = False
    if(num % 4 == 0):
        if(num % 400 == 0):
            leapYear = True
        elif(num % 100 == 0):
            leapYear = False
        else:
            leapYear = True
    else:
        leapYear = False

    return leapYear

year = 2058
print(f' {year} is a leap year : {leapYearFinder(1700)} ')





