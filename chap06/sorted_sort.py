print('sorted() 함수로 정렬하기')
num = int(input('원소 수 입력 '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}] : '))
    
x = sorted(x)
print('오름차순으로 정렬')
for i in range(num):
    print(f'x[{i}] = {x[i]}')
    
x = sorted(x, reverse = True)
print('내림차순으로 정렬')
for i in range(num):
    print(f'x[{i}] = {x[i]}')