''' Write a program to print twin primes less than 1000. If two consecutive odd numbers are 
both prime then they are known as twin primes '''

def is_prime(num):
    for i in range(2,num):
       if num % i == 0:
           return False
    return True
       
for num in range(3,1000):
    if is_prime(num) and is_prime(num + 2):
        print(f"{num} and {num + 2}")
