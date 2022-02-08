from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    for i in range(len(a) // 2):
        a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
    
if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬')
    nx = int(input('원소 수를 입력'))
    x = [None] * nx
    
    for i in range(nx):
        x[i] = int(input(f'x[{i}] :'))
    
    reverse_array(x)
    
    print('배열 원소를 역순으로 정렬함.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
