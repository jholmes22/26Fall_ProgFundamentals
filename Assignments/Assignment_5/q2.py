def rectangle_stats(length, width):
    area = int(length) * int(width)
    perimeter = (int(length) + int(width)) * 2
    return area, perimeter
Height = input("Enter the Length of the rectangle: ")
Wide = input("Enter the Width of the rectangle: ")
area, perimeter = rectangle_stats(Height, Wide)
print(f"The Area of the rectangle is: {area:.2f}")
print(f"The Perimeter of the rectangle is: {perimeter:.2f}")