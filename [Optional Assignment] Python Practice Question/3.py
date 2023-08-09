def is_prime(num):
    for i in range(2,num):
       if num % i == 0:
           return False
    return num

a = int(input("enter number"))
p = a
lst = []
for num in range(2,(a+1)):
    if is_prime(num):
        lst.append(num)
# print(lst)
while a != 0:
    for j in lst:
        for iit in range(1,p):
            lst2 = [iit]
            if a / j in lst2:
                a = a/j
                print(j)
