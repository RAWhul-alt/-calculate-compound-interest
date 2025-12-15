p=float(input("enter the princeple amount"));
t=float(input("enter time"));
r=float(input("enter the rate of intrest"));
a=(p*((1+r)/100))**t;
c=a-p;
print ("the compound intrest is ",c);
