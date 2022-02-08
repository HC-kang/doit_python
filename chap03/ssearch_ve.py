from typing import Any, Sequence

def seq_search(a:Sequence, Key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    raise ValueError

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요. :'))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))
        
    ky = int(input('검색할 값 입력'))
    
    try:
        idx = seq_search(x, ky)
    except ValueError:
        print('검색값이 없습니다')
    else:
        print(f'검색 값은 x[{idx}]에 있습니다')