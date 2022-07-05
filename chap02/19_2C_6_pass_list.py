def change(lst, idx, val):
    lst[idx] = val
    

x = [11,22,33,44,55]
print('x=', x)

index = int(input('업데이트할 인덱스를 선택 : '))
value = int(input('업데이트할 값을 입력 : '))

change(x, index, value)
print(f'x = {x}')