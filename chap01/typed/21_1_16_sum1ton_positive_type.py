print("Sum of integers in range 1 to n")

while True:
    n: int = int(input("Enter n:"))
    if n > 0:
        break
    
sum = 0

i = 1

for i in range(1, n+1):
    sum += i
    i += 1
    
print(f"Sum of 1 to {n} is {sum}")
