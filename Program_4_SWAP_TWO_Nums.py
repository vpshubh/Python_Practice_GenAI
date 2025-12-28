""" a= input("Enter first number: ")
b= input("Enter second number: ")
print(f"Original Values:\na = {a}\nb = {b}")
# Swapping the values
a, b = b, a
print("After swapping:")
print(f"a = {a}\nb = {b}") """


# Using no temp variable
def swap(a,b):
    return b, a

def main():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(f"Original Values:\nnum1 = {num1}\nnum2 = {num2}")
    num1, num2 = swap(num1, num2)
    print(f"After swapping:\nnum1 = {num1}\nnum2 = {num2}")


#Using temp variable
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b
def main_with_temp():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(f"Original Values:\nnum1 = {num1}\nnum2 = {num2}")
    num1, num2 = swap_with_temp(num1, num2)
    print(f"After swapping using temp variable:\nnum1 = {num1}\nnum2 = {num2}")

main()
main_with_temp()