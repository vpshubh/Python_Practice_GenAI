# import calendar
# def display_calendar(year, month):
#     # Create a TextCalendar instance
#     cal = calendar.TextCalendar()

#     # Generate the month's calendar as a multi-line string
#     month_calendar = cal.formatmonth(year, month)

#     # Print the calendar
#     print(month_calendar)

# def main():
#     # Input year and month from the user
#     year = int(input("Enter year (e.g., 2023): "))
#     month = int(input("Enter month (1-12): "))

#     # Display the calendar for the given month and year
#     display_calendar(year, month)

# main()

import calendar
year= int(input("Enter year: "))
month= int(input("Enter month: "))
print(calendar.month(year, month))