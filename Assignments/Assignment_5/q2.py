def rectangle_stats(length, width): #function that takes two parameters length and width
    area = int(length) * int(width)
    perimeter = (int(length) + int(width)) * 2 #calculates the perimeter of the rectangle with the given length/width
    return area, perimeter
Height = input("Enter the Length of the rectangle: ") #tells the user to enter a length for the rectangle
Wide = input("Enter the Width of the rectangle: ")
area, perimeter = rectangle_stats(Height, Wide) #calls the function rectangle_stats
print(f"The Area of the rectangle is: {area:.2f}")
print(f"The Perimeter of the rectangle is: {perimeter:.2f}") #print statement about the perimeter of the rectangle