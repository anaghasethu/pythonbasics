import numbers


x=78
y=78

if x>y:
    print(f"{x} is greater than {y}")
elif x==y:
    print(f"{x} is equal to {y}")
else:
    print(f"{y} is greater than {x}")


if x>1 or y<60:
    print("Great..!")
else:
    print("Sorry Try again..!")


numbers = [1,4,7,2,99,56,27,77]

if x in numbers:
    print(f"Found {x}")
else:
    print(f"{x} not found")

if x not in numbers:
    print("Not found")
else:
    print("Found")