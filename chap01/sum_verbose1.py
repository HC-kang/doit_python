print('a부터 b까지 정수의 합')

a = int(input('a의 값 : '))
b = int(input('b의 값 : '))

if a>b:
    a, b = b, a

sum = 0

for i in range(a, b+1):
    if i<b:
        print(f'{i} + ', end = '')
    else:
        print(f'{i} = ', end='')
    sum += i
    
print(sum)