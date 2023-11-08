num=int(input("enter the number :"))
factorial=1
if num<0:
    print("sorry ,factorial does not exist for the mumbers less than 1")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num +1):
        factorial=factorial*i
    print("th factorialof ",num,"is",factorial)   
