def power(p, n):
    if n == 0:
        return 1
    return p * power(p, n - 1)

p = float(input("Enter prinicipal amount: "))
n = int(input("Enter number of years: "))

print("p^n =", power(p, n))
