def generate_fibonnaci(num):
    if num > 0:
        print(" 0 1 1", end = " ")
        first = 1
        second = 1
        third = 2
        while third <= num:
            third = first + second
            if third <= num:    
                print(third, end = " ")
            first = second
            second = third


def get_nth_fibonacci_num(n):
    if n < 0:
        return "Incorrect input"

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    first = 0
    second = 1
    
    for i in range(2, n):
        thrid = first + second
        first = second
        second = thrid
    
    return thrid


def is_perfect_square(num):
    sqrt = int(num ** 0.5)
    return num == sqrt * sqrt

    
def is_fibonacci_num(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


if __name__ == "__main__":
    num = 10
    number = 21
    generate_fibonnaci(num)
    print("\n", get_nth_fibonacci_num(9))
    print(is_fibonacci_num(number))