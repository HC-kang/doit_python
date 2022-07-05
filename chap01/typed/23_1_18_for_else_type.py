import random

n: int = int(input("Number of random numbers?:"))

for _ in range(n):
    r: int = random.randint(10, 99)
    print(r, end="")
    if r == 13:
        print("Done")
        break
else:
    print("Random Number Generate Done")