def proximo_elemento_a(n):
    return n + 2

def proximo_elemento_b(n):
    return n * 2

def proximo_elemento_c(n):
    return n**2

def proximo_elemento_d(n):
    return (2 * (n // 2 + 1))**2

def proximo_elemento_e(n1, n2):
    return n1 + n2

def proximo_elemento_f(n):
    return n + 1


print("a) 1, 3, 5, 7, ___")
print(proximo_elemento_a(7))

print("\nb) 2, 4, 8, 16, 32, 64, ___")
print(proximo_elemento_b(64))

print("\nc) 0, 1, 4, 9, 16, 25, 36, ___")
print(proximo_elemento_c(36))

print("\nd) 4, 16, 36, 64, ___")
print(proximo_elemento_d(8))

print("\ne) 1, 1, 2, 3, 5, 8, ___")
print(proximo_elemento_e(5, 8))

print("\nf) 2, 10, 12, 16, 17, 18, 19, ___")
print(proximo_elemento_f(19))



#Portanto, as sequências completas seriam:
#a) 1, 3, 5, 7, 9
#b) 2, 4, 8, 16, 32, 64, 128
#c) 0, 1, 4, 9, 16, 25, 36, 1296
#d) 4, 16, 36, 64, 100
#e) 1, 1, 2, 3, 5, 8, 13
#f) 2, 10, 12, 16, 17, 18, 19, 20