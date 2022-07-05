print("Sum of integers in range a to b")

a: int = int(input("enter a:"))
b: int = int(input("enter b:"))

if a > b:
    a, b = b, a
    
sum = 0

for i in range(a, b):
    print(f"{i} + ", end="")
    sum += i
print(f"{b} = ", end="")
sum += b

print(sum)
