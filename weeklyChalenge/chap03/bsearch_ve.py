def bin_search(a, key):
    pl = 0
    pr = len(a) - 1
    
    while True:
        pc = (pl + pr) // 2 
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    raise ValueError

if __name__ == '__main__':
    num = int(input('원소 수 입력 : '))
    x = [None] * num
    
    print('오름차순 출력')
    
    x[0] = int(input('x[0] : '))
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i-1]:
                break
            
    ky = int(input('검색할 값을 입력 : '))
    
    try:
        idx = bin_search(x, ky)
    except ValueError:
        print('검색값이 없음')
    else:
        print(f'검색값은 x[{i}]에 있음.')