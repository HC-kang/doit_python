print('Enter a two-digit Positive number:')

while True:
    no: int = int(input('숫자는?'))
    if no > 9 and no < 100:
        break

print(no)
