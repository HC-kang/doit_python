from enum import Enum
from stack import Stack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end = '')
        print()
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
s = Stack(8)

while True:
    print(f'현재 데이터 수 : {len(s)} / {s.capacity}')
    menu = select_menu
    
    if menu == Menu.푸시:
        x = int(input('데이터:'))
        try:
            s.push(x)
        except IndexError:
            print('스택이 가득 찼습니다.')
    
    elif menu == Menu.팝:
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except IndexError:
            print('스택이 비어있습니다.')
    
    elif menu == Menu.검색:
        x = int(input('검색할 값 입력 : '))
        if x in s:
            print(f'{s.count(x)} 개를 포함하고, 맨 앞쪽의 위치는 {x.find(x)}입니다.')
        else:
            print('검색 값은 포함되어있지 않습니다.')
        
    elif menu == Menu.덤프:
        s.dump()
        
    else:
        break
    