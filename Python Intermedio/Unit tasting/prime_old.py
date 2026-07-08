def prime(num):
    if num < 2:
        return False   
    for index in range(2, int(num**0.5) + 1):
        if num % index == 0:
            return False
    return True

def prime_numbers(numbers):
    primes=[]
    for number in numbers:
        if prime(number):
            primes.append(number)
    return primes

def main():
    numbers=[1, 4, 6, 7, 13, 9, 67]
    result=prime_numbers(numbers)
    print( "Prime numbers:",result)
main()
