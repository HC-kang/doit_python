print("Maximum value of three integer")

a: int = int(input("integer a: "))
b: int = int(input("integer b: "))
c: int = int(input("integer c: "))

max = a

if b > max: max = b
if c > max: max = c

print(f"the maximum value is {max}")
