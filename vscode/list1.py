l1=[42,36,28,96,4,-1,1]
mini=99
maxi=1
for i in range(0,len(l1)):
    if l1[i]<mini:
        mini=l1[i]
print(mini)
for i in range(0,len(l1)):
    if l1[i]>maxi:
        maxi=l1[i]
print(maxi)
print(mini+maxi)















