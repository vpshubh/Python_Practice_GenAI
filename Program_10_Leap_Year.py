year = int(input("Enter Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("{0} is a Leap Year".format(year))
# elif (year % 100 == 0):
    # print("{0} is not a Leap Year".format(year))
else:
    print("{0} is not a Leap Year".format(year))