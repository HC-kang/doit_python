def max3(a: int, b: int, c: int) -> int:
    max: int = a
    if b > max: max = b
    if c > max: max = c
    return max

num: list[int] = [1, 2, 34]

for i in num:
    for j in num:
        for k in num:
            print(f"max3 ({i},{j},{k}) = {max3(i, j, k)}")

max3(1, 2, 45)
