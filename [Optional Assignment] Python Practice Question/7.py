def prodDigits(str):
    prod = 1
    lst = [int (i) for i in str]
    for i in range(0,len(lst)):
        prod = prod * lst[i]
    return prod

str = input("Enter a number: ")
ans = prodDigits(str)
print(ans)