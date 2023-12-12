import calendar

def display_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    year_month_str = f"{month_name} {year}"

    print(f"Calendar for {year_month_str}")
    print(" Mo Tu We Th Fr Sa Su")

    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:2d} "
        print(week_str)

# Example: Display the calendar for November 2023
display_calendar(2023, 11)
