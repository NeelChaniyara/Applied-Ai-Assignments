def square(lst):
    return lst ** 2

lst = [1,2,3,4,5]

squarenum = list(map(square , lst))
print(squarenum)