def add_time(start, duration, day=None):
    start_hours, period = start.split()
    hours, minutes = map(int, start_hours.split(":"))
    if period == "PM" and hours !=12:
        hours += 12
    elif period == "AM" and hours == 12:
        hours = 0

    dur_hours, dur_minutes = map(int, duration.split(":"))
    total_minutes = hours * 60 + minutes + dur_hours * 60 +dur_minutes

    total_hours = total_minutes // 60
    total_minutes = total_minutes % 60
    new_hours = total_hours % 24
    new_period = "AM" if new_hours < 12 else "PM"
    if new_hours == 0:
        new_hours = 12      
    elif new_hours > 12:
        new_hours -= 12
    new_time = f"{new_hours}:{total_minutes:02d} {new_period}"  
    if day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(day.capitalize())
        new_day_index = (start_day_index + total_hours // 24) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"
    if total_hours // 24 > 0:
        days_later = total_hours // 24
        if days_later == 1:
            new_time += " (next day)"
        else:
            new_time += f" ({days_later} days later)"
    return new_time



