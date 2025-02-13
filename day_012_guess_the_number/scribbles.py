

def is_prime(num):
    if num == 2:
        return True
    for check in range (2, 1+round(int(((num**0.5))),0)):
        if num % check == 0:
            return False
    return True

print (is_prime(4))