list=[30,10,18,12,3,28,45]
n=len(list)
for i in range(1,n):
    j=i
    while list[j-1]>list[j] and j>0:
        T=list[j]
        list[j]=list[j-1]
        list[j-1]=T
        j=j-1
print(list)
