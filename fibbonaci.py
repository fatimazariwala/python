# python
terms=int(input("Enter number of terms you want to print :  "))
n1=0
n2=1
count=0

if terms<=0:
    print("Please enter number of terms to be printed ...")

elif terms==1:
    print(n1)
else :
    print("Fibonacci Sequence : ")
    while count<terms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count += 1
    
