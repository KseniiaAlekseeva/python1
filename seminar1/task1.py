def exist_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


def triangle_type(a, b, c):
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or a == c or b == c:
        print("Isosceles triangle")
    else:
        print("Versatile triangle")


a, b, c = [int(i) for i in input("Enter the triangle sides: ").split()]
if exist_triangle(a, b, c):
    print("Triangle exists")
else:
    print("Triangle don't exist")
triangle_type(a, b, c)
