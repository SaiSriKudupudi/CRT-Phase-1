def p(n,m):
    if m==0:
        return 1
    if n==1:
        return 1
    return n*p(n,m-1)
p=p(9,4)
print(p)
