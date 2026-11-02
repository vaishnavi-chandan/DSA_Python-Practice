def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
            return "Prime Number."
    else:
         return "Not a Prime number."
print(is_prime(5))