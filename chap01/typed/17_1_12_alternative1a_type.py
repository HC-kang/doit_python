print("Output + and - alternately")

n: int = int(input("How many?:"))

for i in range(1, n+1):
    if i%2:
        print("+", end="")
    else:
        print("-", end="")

print()
