def is_leap_year(year):
    
    if year % 100 == 0:
        return False
    elif year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        return False
    
    
result = is_leap_year (2016)
print(result)
