sum1=0
sum2=0
for i in range(1,31):
    if i%6==0:
        sum1=sum1+i
#print(sum1)
    else:
        sum2=sum2+i
#print(sum2)
print(sum2-sum1)