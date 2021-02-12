n1=0
n2=1
count=0
nterms=int(input("how many term"))

if nterms<=0:
    print("enter a positive  numbers")
elif nterms==1:
    print("fibanocci series upto ",nterms,"is",n1)
else:
    print("fibonocci series is:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
