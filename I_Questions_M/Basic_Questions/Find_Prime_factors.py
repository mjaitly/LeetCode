def get_prime_factors(num):
    
    # divide the num by 2 umtil odd number is left
    while num % 2 == 0:
        print("2", end = " ")
        num //=  2

    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            print(i, end = " ")
            num //= i
    
    # if number is prime
    if num > 2:
        print(num)

    # print()


if __name__ == "__main__":
    numbers = [315, 4, 13, 6, 278, 18]

    for num in numbers:
        # output = "Prime factors of " + str(num) + " are: " + str(get_prime_factors(num)) 
        print("Prime factors of " + str(num) + " are: ")
        get_prime_factors(num)
        print()

