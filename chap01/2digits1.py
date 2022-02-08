print('2자리 양수를 입력')

while True:
    no = int(input('값?'))
    if no>9 and no<100:
        break

print(no)