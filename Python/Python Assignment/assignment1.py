def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return num > 1

def sum_of_primes(n):
    count = 0
    num = 2
    total = 0

    while count < n:
        if is_prime(num):
            total += num
            count += 1
        num += 1

    return total

# Example usage
N = int(input("Enter N: "))
print("Sum of first", N, "prime numbers is:", sum_of_primes(N))


