def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for n in range(2, 1001):
    if est_premier(n):
        print(n)