print("Step 1")
p=int(input("Please Enter a prime number 'P' value: "))
q=int(input("Please Enter a prime number 'Q' value: "))
print("Step 2")
n=p*q
print("Your n value is: ")
print(n)
print("Your Phi value is ")
phi=(p-1)*(q-1)
print(phi)
phi_2=phi
print("Step 3")


def __gcd(a, b):
    # Everything divides 0
    if (a == 0 or b == 0): return 0

    # base case
    if (a == b): return a

    # a is greater
    if (a > b):
        return __gcd(a - b, b)

    return __gcd(a, b - a)


def coprime(a, b):
    if (__gcd(a, b) == 1):
        return a

for x in range(phi):
    if(coprime(x,phi_2)!=p and coprime(x,phi_2)!=q ):
        e= coprime(x,phi_2)

print("Your e value is ")
print(e)

print("Step 4")






