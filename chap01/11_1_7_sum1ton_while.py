print('1부터 n까지 정수의 합')

n = int(input('n입력 : '))

sum = 0
i = 1

while i<=n:
    sum += i
    i +=1
    
print(f'1부터 n까지의 합은 {sum}입니다.')