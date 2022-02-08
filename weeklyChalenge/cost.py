# price	money	count	result
# 3	    20  	4   	10

def solution(price, money, count):
    cost = 0
    for i in range(1, count+1):
        cost += price*i    
    answer = (cost-money) if (cost-money) >0 else 0
    return answer

solution(3, 20, 4)

def solution(price, money, count):
    num = (1+count)*count//2
    cost = num*price
    return (cost-money) if (cost-money) >0 else 0


def solution(price, money, count):
    return max(0,(1+count)*count//2*price-money)

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)