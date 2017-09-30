#!/usr/bin/python3
from math import sqrt

def is_prime(num):
    if num == 2:
        return True
    if num < 2:
        return False
    
    if num%2 == 0:
        return False
    
    for i in range(3,int(sqrt(num))+1,2):
        if num%i == 0:
            return False
    return True
        

try:
    num = int(input('Enter number: '))
    if is_prime(num):
        print('%d is prime'%num)
    else:
        print('%d is not prime'%num)

except Exception as e:
    print(str(e))

