# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def checkPrime(num):
    prime = True
    for i in range(2, num):
        if(num % i == 0):
            prime = False

    return (prime)


print('The number is Prime', checkPrime(13))
