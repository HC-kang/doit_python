def med3(a: int, b: int, c: int) -> int:
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

num: list[int] = [1, 2, 34]

for i in num:
    for j in num:
        for k in num:
            print(f"med3 ({i},{j},{k}) = {med3(i,j,k)}")
            
med3(1, 2, 43)
