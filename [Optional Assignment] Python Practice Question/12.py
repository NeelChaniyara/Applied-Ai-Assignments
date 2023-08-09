def odd(lst):
    if lst % 2 != 0:
        return lst

lst = range(1,11)
oddnum = list(filter(odd , lst))
print(oddnum)