print('세 정수의 최댓값')

a = int(input('정수 a : '))
b = int(input('정수 b : '))
c = int(input('정수 c : '))

max = a

if b > max: max = b
if c > max: max = c

print(f'최댓값은 {max}입니다.')