area: int = int(input('Enter S of rectangle'))

for i in range(1, int(area**0.5)+1):
    if area%i == 0:
        print(f"{i} X {area//i}")
