def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
# def fahrenheit_to_celsius(fahrenheit):
#     """Convert Fahrenheit to Celsius."""
#     return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return (celsius+273)

def main():
    celsius= int(input("Temperature in Degree Celsius: "))
    # farhenheit = int(input("Temperature in fahrenheit: "))
    Fahrenheit = celsius_to_fahrenheit(celsius)
    # Celsius= fahrenheit_to_celsius(farhenheit)
    Kelvin= celsius_to_kelvin(celsius)
    print(f"Temperatures accordingy: {celsius} *Celsius = {Fahrenheit} *Farhenheit and  {Kelvin} K")

main()