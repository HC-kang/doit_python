import random

n = int(input('난수 개수?'))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end = ' ')
    if r == 13:
        print('종료')
        break
else:
    print('난수 생성 종료')




