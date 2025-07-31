# Match-case statement

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case _:
            return "Not a valid day"
    
print(day_of_week(1))