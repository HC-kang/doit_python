print('학생 그룹 점수 합계 및 평균')

score1 = int(input('1번 학생의 점수?'))
score2 = int(input('2번 학생의 점수?'))
score3 = int(input('3번 학생의 점수?'))
score4 = int(input('4번 학생의 점수?'))
score5 = int(input('5번 학생의 점수?'))

total = 0

total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}점')
print(f'평균은 {total/5}점')

