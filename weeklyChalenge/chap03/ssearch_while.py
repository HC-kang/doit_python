from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1
        

if __name__ == '__main__':
    num = int(input('원소 수 : '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]'))
        
    xy = int(input('검색값 입력 : '))
    
    idx = seq_search(x, ky)
    
    if idx == -1:
        print('검색값 찾을 수 없음')
    else:
        print(f'검색값은 x[{idx}]에 있음.')