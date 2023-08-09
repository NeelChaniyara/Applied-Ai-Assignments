def convert(num):
    lst = []
    while True:
        a = int(num % 2)
        num //= 2
        lst.append(a)
        if num == 1:
            break
    lst.append(1)
    lst.reverse()
    print(lst)

num = float(input("enter number"))
convert(int(num))