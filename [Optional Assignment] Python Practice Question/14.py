def even(lst):
    if lst % 2 == 0:
        return lst

def square(evennum):
    return evennum ** 2

lst = range(1,11)

evennum = list(filter(even , lst))
squarenum  = list(map(square, evennum))
print(squarenum)