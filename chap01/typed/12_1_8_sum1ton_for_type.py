print("Sum of integers in range 1 to n")

n: int = int(input("enter n:"))

sum = 0

for i in range(1, n+1):
    sum += i

print(f"Sum of 1 to n is {sum}")
