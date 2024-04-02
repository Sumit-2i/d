n=2
p=5
def poww(n,p):
    if p==1:
        return n
    return n*poww(n,p-1)
print(poww(n, p))
print(pow(2,5))