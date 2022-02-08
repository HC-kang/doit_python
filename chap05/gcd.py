def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
        
if __name__ == '__main__':
    print('두 정수의 최대공약수를 구합니다.')
    x = int(input('첫 번째 정수 : '))
    y = int(input('두 번째 정수 : '))
    
    print(f'두 정수의 최대공약수는 {gcd(x, y)}입니다.')