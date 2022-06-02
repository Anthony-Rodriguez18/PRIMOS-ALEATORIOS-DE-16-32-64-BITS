import random  

def EXPMOD(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y>>1
        x = (x * x) % p

    return res

def MILLER_RABIN(d, n):
    a = 2 + random.randint(1, n - 4)
    x = EXPMOD(a, d, n)

    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n 
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True

    # Return compuesto
    return False


def esPrimo( n, s):

    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(s):
        if (MILLER_RABIN(d, n) == False):
            return False

    return True

s = 5

print("10 números primos de 16 bits: ")
count = 0
for _ in iter(int, 1):
  b = random.getrandbits(16)
  if (esPrimo(b, s)):
        print(b, end=', ')
        count += 1
  if count == 10: break
print()
print()

print("10 números primos de 32 bits: ")
count = 0
for _ in iter(int, 1):
  b = random.getrandbits(32)
  if (esPrimo(b, s)):
        print(b, end=', ')
        count += 1
  if count == 10: break
print()
print()

print("10 números primos de 64 bits: ")
count = 0
for _ in iter(int, 1):
  b = random.getrandbits(64)
  if (esPrimo(b, s)):
        print(b, end=', ')
        count += 1
  if count == 10: break