def divi(i):
    lst = []
    for j in range(1,i):
        if i % j == 0:
            lst.append(j)
    return lst
    
def addi(lst):
    sum = 0
    for j in range(0,len(lst)):
        sum = sum + lst[j]
    return sum

def checkit(summ,summ1,i,k):
    if summ == k and summ1 == i and i != k:
        print(f"{i} and {k} is an amicable numbers")
    # else:
    #     print(f"{i} is Not an amicable numbers")

n = int(input("enter number : "))
for i in range(1,n+1):
    lst = divi(i)
    summ = addi(lst)
    for k in range(2,n):
        lst2 = divi(k)
        summ1 = addi(lst2)
        checkit(summ,summ1,i,k)