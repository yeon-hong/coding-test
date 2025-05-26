import datetime
def solution(a, b):

    date = datetime.date(2016, a, b)

    weekday = date.weekday()  

    day_index = (weekday + 1) % 7

    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return days[day_index]
