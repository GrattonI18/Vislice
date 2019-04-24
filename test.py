# Napiši program, ki izpiše vsa 200 praštevila manjša od 200

def je_prast(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for x in range(2, 200):
    if je_prast(x):
        print(x)