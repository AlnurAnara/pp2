#use filter function 
#which will take list of numbers as an agrument and returns only prime numbers from the list.
def filter_prime (n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(list(filter(filter_prime,[1,2,3,4,5,6,7,8,9])))


'''
filter function
1.creat a func
* by labmda function
* by def keyword

labmda:
check_even = labmda x : x % 2==0
print=list(filter(check_even,[1,2,3,4,5,6]))

def:
def check_even(x):
    if x % 2 != 0 :
        return False
    return True

print(list(filter(check_even,[1,2,3,4,5,6,7,8,9])))

'''