print("Output + and - alternately")

n: int = int(input("How many?:"))

for i in range(n):
    if i % 2:
        print("-", end="")
    else:
        print("+", end="")

print()
