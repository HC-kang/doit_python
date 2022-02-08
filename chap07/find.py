text = input('문자열 입력 : ')
ptn = input('검색할 패턴 : ')

c = text.count(ptn)

if c == 0:
    print('검색한 내용이 없습니다.')
elif c == 1:
    print(f'검색한 ptn의 인덱스 : {text.find(ptn)}')
else:
    print(f'검색한 ptn의 맨 앞 인덱스 : {text.find(ptn)}')
    print(f'검핵한 ptn의 맨 뒤 인덱스 : {text.rfind(ptn)}')
