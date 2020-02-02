#Greatest common divisor

def hcfnaive(a, b):
    if (b == 0):
        return a
    else:
        return hcfnaive(b, a % b)
a=int(input("Enter a non-null integer a: "))
b=int(input("Enter a non-null integer b: "))

print("the greatest common divisor of a and b is",hcfnaive(a, b))
