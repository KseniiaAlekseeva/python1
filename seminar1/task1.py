def existTriangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


def triangleType(a, b, c):
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or a == c or b == c:
        print("Isosceles triangle")
    else:
        print("Versatile triangle")


print("Enter the triangle sides: ")
a, b, c = [int(i) for i in input().split()]
if existTriangle(a, b, c):
    print("Triangle exists")
else:
    print("Triangle don't exist")
triangleType(a, b, c)
