# import math
# a=float(input("Enter Coefficient a: "))
# b=float(input("Enter Coefficient b: "))
# c=float(input("Enter Coefficient c: "))


# #Discriminant formula
# discriminant = (b**2) - (4*a*c)

# #Checking if Discriminant has positive, negative or Zero Values
# if discriminant >0:
#     root1= (-b+ math.sqrt(discriminant))/(2*a)
#     root2= (-b- math.sqrt(discriminant))/(2*a)
#     print(f"Root 1: {root1}")
#     print(f"Root 2: {root2}")
# elif discriminant==0:
#     root= -b/(2*a)  #where b**2 - 4*a*c = 0
#     print(f"Roots Repeated are : {root}")
# else:
#     #Complex roots
#     real_part= -b/(2*a)
#     imaginary_part= math.sqrt(abs(discriminant))/(2*a)
#     print(f"Root 1: {real_part}+{imaginary_part}i")
#     print(f"Root 2: {real_part}-{imaginary_part}i")





import math

def calculate_roots(a, b, c):
    discriminant = (b**2) - (4*a*c)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

def main():
    a=float(input("Enter Coefficient a: "))
    b=float(input("Enter Coefficient b: "))
    c=float(input("Enter Coefficient c: "))
    roots = calculate_roots(a, b, c)
    if len(roots) == 2:
        print(f"Root 1: {roots[0]}")
        print(f"Root 2: {roots[1]}")
    elif len(roots) == 1:
        print(f"Repeated Root: {roots[0]}")
    else:
        print(f"Root 1: {roots[0]}")
        print(f"Root 2: {roots[1]}")

        
main()