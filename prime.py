# program
for num in range(1,40):
    if num==2:
        print(num)
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break
