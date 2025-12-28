""" base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
print(f"The area of triangle with Base: {base}, Height: {height} is {area_triangle}") """



def area_triangle_func(base, height):
    return 0.5 * base * height

def main():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area_triangle = area_triangle_func(base,height)
    print(f"The area of triangle with Base: {base}, Height: {height} is {area_triangle}")

main()