area = int(input('직사각형의 넓이를 입력하세요'))

for i in range(1, int(area**0.5)+1):
    if area%i==0:
        print(f'{i} X {area//i}')    