print('* 출력')

n = int(input('몇 개?'))
w = int(input('몇개마다?'))

for _ in range(n//w):
    print('*'*w)


print('*' * (n%w), end = '')
# rest = n%w

# if rest:
#     print('*'*rest)