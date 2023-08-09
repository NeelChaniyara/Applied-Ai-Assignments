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

def checkit(i,summ):
    if i == summ:
        print(f"{i} is Prefect number")
    else:
        print(f"{i} is Not a Perfect number")

n = int(input("enter number : "))
for i in range(1,n+1):
    lst = divi(i)
    summ = addi(lst)
    checkit(i,summ)