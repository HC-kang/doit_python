print("Print *")

n: int = int(input("How many stars to print?"))
w: int = int(input("How many stars in a line?"))

for i in range(n):
    print("*", end="")
    if i % w == w - 1:
        print()

if n % w:
    print()
