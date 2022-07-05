print('오른쪽 아래가 직각인 이등변삼각형')

n = int(input('n입력'))

# for i in range(n):
#     for j in range(n):
#         if n-j<=i : print('*', end='')
#         else: print(' ', end='')
            
#     print()
    
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print()