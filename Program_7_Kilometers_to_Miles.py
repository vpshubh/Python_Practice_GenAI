def kilometers_to_miles(kilometers):
    """Convert kilometers to miles.

    Args:
        kilometers (float): Distance in kilometers.
    Returns:
        float: Distance in miles.
    """
    miles = kilometers * 0.621371
    return miles

def main():
    try:
        km_input = float(input("Enter distance in kilometers: "))
        miles_output = kilometers_to_miles(km_input)
        print(f"{km_input} kilometers is equal to {miles_output:.2f} miles.")
    except ValueError:
        print("Please enter a valid number.")
main()