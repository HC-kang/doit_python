print("print *")

n: int = int(input("How many stars to print?"))
w: int = int(input("How many stars in a line?"))

for _ in range(n // w):
    print("*"*w)

print("*" * (n % w), end="")
