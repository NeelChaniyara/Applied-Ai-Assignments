def find_prime_factors(number):
    print(f"Prime factors of {number}:")
    
    # Start with the smallest prime number
    divisor = 2
    
    while number > 1:
        # Check if the current divisor is a factor
        if number % divisor == 0:
            # If it's a factor, print it and reduce the number
            print(divisor)
            number //= divisor ; ''' number = number // divisor '''
        else:
            # If not a factor, try the next number
            divisor += 1

num = int(input("Enter a positive integer: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    find_prime_factors(num)
