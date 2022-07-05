print("An isosceles triangle at right angles to the lower left")

n: int = int(input("Enter n:"))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print()
