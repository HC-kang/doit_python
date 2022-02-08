text = input('문자열 입력 : ')
ptn = input('검색 할 문자열 : ')

c = text.count(ptn)

if c == 0:
    print('패턴이 없습니다.')
elif c == 1:
    print(f'검색할 패턴의 인덱스는 : {text.index(ptn)}')
else:
    print(f'검색할 패턴의 인덱스 맨 앞은 : {text.index(ptn)}')
    print(f'검색할 패턴의 맨 뒤 인덱스는 : {text.rindex(ptn)}')