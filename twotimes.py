# program
h1=int(input("Enter the hour:"))
m1=int(input("Enter the mins:"))
s=h1*60
t1=s+m1
h2=int(input("Enter the hour:"))
m2=int(input("Enter the mins:"))
m=h2*60
t2=m+m2
t=abs(t1-t2)
print("Enter the mins b/w two times:",t)
