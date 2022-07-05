def med3(a:int, b:int, c:int):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    if (c >= b and a <= b) or (c <= b and a >= b):
        return b
    return c

num: list[int] = [1, 2, 34]

for i in num:
    for j in num:
        for k in num:
            print(f"med3 ({i},{j},{k}) = {med3(i,j,k)}")
            
med3(1, 2, 43)
