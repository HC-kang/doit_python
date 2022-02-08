print('1부터 n까지 정수의 합을 구합니다.')

n = int(input('n을 입력 : '))

sum = 0

for i in range(1, n+1):
    sum += i
    
print(sum)