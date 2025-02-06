def filter_prime (n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(list(filter(lambda x : filter_prime(x),[1,2,3,4,5,6,7,8,9])))
