print("An isosceles triangle at right angles to the lower left")

n: int = int(input("The length of a short side:"))

for i in range(n):
    for j in range(i+1):
        print(j, end="")
    print()
