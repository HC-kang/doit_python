print('*를 출력')
n = int(input('몇개?'))
w = int(input('몇개마다 줄바꿈?'))

for i in range(n):
    print('*', end='')
    if i%w == w-1:
        print()

if n%w:
    print()