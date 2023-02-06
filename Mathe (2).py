import math

#Bei allen zahlen die NICHT gegeben sind "0" eingeben
 
a = 20
b = 0
c = 7
q = 0
p = 0
h = 0
einheit = "m"

if a and b > 0:
    c = math.sqrt(a**2 - b**2)
    q = b**2 / c
    p = c - q
    h = math.sqrt(q * p)

    print("a =",a,einheit)
    print("b =",b,einheit)
    print("")
    print("c =",c,einheit)
    print("q =",q,einheit)
    print("p =",p,einheit)
    print("hc =",h,einheit)

elif b and c > 0:
    q = b**2 / c
    p = c - q
    a = math.sqrt(c * p)
    h = math.sqrt(q * p)

    print("b =",b,einheit)
    print("c =",c,einheit)
    print("")
    print("a =",a,einheit)
    print("q =",q,einheit)
    print("p =",p,einheit)
    print("hc =",h,einheit)

#elif a and c > 0:
    b = math.sqrt(c**2 + a**2)
    q = b**2 / c
    p = c - q
    h = math.sqrt(p * q)

    print("a =",a,einheit)
    print("c =",c,einheit)
    print("")
    print("b =",b,einheit)
    print("q =",q,einheit)
    print("p =",p,einheit)
    print("hc =",h,einheit)