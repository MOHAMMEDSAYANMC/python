total=0
list=[]
n=int(input("enter number of elements in list"))
print("enter the values")
for i in range(0,n):
    a=int(input())
    list.append(a)
for b in list:
    total+=b
print("sum of values in ",list," is",total)



