def cubesum(str):
    lst = [int(k) for k in str]
    lst2 = []
    for i in lst:
        lst2.append(i ** len(lst))  # list append
    sum = 0
    for j in range(0, len(lst2)):
        sum = sum + lst2[j]
    return sum

def isarmstrong(sum, str):
    if sum == int(str):
        print("The number is an armstrong number")
    else:
        print("The number is not an armstrong number")

str = input("Enter a number: ")
sum = cubesum(str)
isarmstrong(sum, str)
