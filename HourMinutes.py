def angle(hours, minutes):
    if (hours == 12):
        hours = 0
    elif (hours > 12):
        hours = hours - 12

    if (minutes == 60):
        minutes = 0

    minute_angle = minutes * 6
    hours_angle = hours * 30
    return abs(hours_angle - minute_angle)


print(angle(0, 30))
