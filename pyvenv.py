#Greatest common divisor

def hcfnaive(a, b):
    if (b == 0):
        return a
    else:
        return hcfnaive(b, a % b)
a=int(input("Saisir un entier non nul a: "))
b=int(input("Saisir un entier non nul b: "))

print("le pgdc de a et b est",hcfnaive(a, b))