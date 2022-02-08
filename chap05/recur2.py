def recur(n: int) -> int:
    if n>0:
        recur(n-2)
        print(n)
        recur(n-1)
    
x = int(input('n을 입력 : '))

recur(x)