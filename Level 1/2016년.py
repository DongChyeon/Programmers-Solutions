import datetime as dt

def solution(a, b):
    week = [ "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN" ]

    day = dt.datetime(2016, a, b)
    
    return week[day.weekday()]