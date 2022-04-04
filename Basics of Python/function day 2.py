
def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a-1)

f = fact(5)
print(f)
