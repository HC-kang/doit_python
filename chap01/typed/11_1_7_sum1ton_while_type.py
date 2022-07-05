print("Sum of integers in range 1 to n")

n: int = int(input("enter n:"))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"Sum of 1 to n is {sum}")
