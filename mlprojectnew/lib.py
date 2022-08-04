from datetime import date
from datetime import datetime


def try_me(birth_month,birth_day,birth_year):
    if ((date.today().month==birth_month) & (date.today().day==birth_day)):
        age=round((date.today()-date(birth_year,birth_month,birth_day)).days/365)
        message=f"Today is your birthday! Happy Birthday! You are {age} years old"
    else:
        message=f"Its not your birthday today, please come back later to get a wish from me"
    return message

if __name__ == "__main__":
    # My Birthday
    birth_month,birth_day,birth_year=8,4,1990
    message = try_me(birth_month,birth_day,birth_year)
    print(message)
