import math

# Function to calculate area of a circle
def area_circle(radius):
    return math.pi * radius ** 2

# Function to calculate area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

if __name__ == "__main__":
    print("Choose a shape to calculate area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        r = float(input("Enter the radius of the circle: "))
        area = area_circle(r)
        print(f"Area of Circle: {area:.2f}")

    elif choice == "2":
        l = float(input("Enter the length of the rectangle: "))
        w = float(input("Enter the width of the rectangle: "))
        area = area_rectangle(l, w)
        print(f"Area of Rectangle: {area:.2f}")

    elif choice == "3":
        b = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = area_triangle(b, h)
        print(f"Area of Triangle: {area:.2f}")

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
