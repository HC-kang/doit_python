print('왼쪽 아래가 직각인 이등변 삼각형')

n = int(input('짧은 변의 길이'))

for i in range(n):
    for j in range(i+1):
        print(j, end="")
    print()