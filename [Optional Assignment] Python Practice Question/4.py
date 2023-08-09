def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(n, r):
    if n < r:
        return 0
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    if n < r:
        return 0
    return permutations(n, r) // factorial(r)


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

if n < 0 or r < 0:
    print("n and r must be non-negative integers.")
elif n < r:
    print("n should be greater than or equal to r.")
else:
    print(f"Number of permutations of {n} objects taken {r} at a time: {permutations(n, r)}")
    print(f"Number of combinations of {n} objects taken {r} at a time: {combinations(n, r)}")