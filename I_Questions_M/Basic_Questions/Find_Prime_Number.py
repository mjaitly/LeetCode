'''
def isPrime(num):

    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

'''
# Optimized
'''
Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of smaller factor that has been already checked.
The algorithm can be improved further by observing that all primes are of the form 6k ± 1, with the exception of 2 and 3. This is because all integers can be expressed as (6k + i) for some integer k and for i = ?1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, then to check through all the numbers of form 6k ± 1. (Source: wikipedia)
'''

def is_prime(num):
    # Corner cases 
    if (num <= 1) : 
        return False
    if (num <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (num % 2 == 0 or num % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= num) : 
        if (num % i == 0 or num % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True


'''
Check if a prime number can be expressed as sum of two Prime Numbers
'''

def is_sum_prime(num):
    if is_prime(num - 2):
        return True
    else:
        return False


if __name__ == "__main__":
    numbers = [2, 1, 13, 6, 7, 18]
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]

    for num in numbers:
        output = str(num) + " is prime: " + str(is_prime(num))
        print(output)
    
    for num in prime_numbers:
        print(num, " is sum of two primes: ", str(is_sum_prime(num)))
