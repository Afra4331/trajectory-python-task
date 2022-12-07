a=int(input("Enter first number\n"))
b=int(input("Enter second number\n"))
c=input("Enter the operator(+,-,*,/,%)\n")
if(c=='+'):
    print("Sum of these numbers is ",a+b)
elif(c=='-'):
    print("Subtraction of these numbers is ",a-b)
elif(c=='*'):
    print("Multiplication of these number is ",a*b)
elif(c=='/'):
    if(b==0):
        c=int(input("Enter another second number\n"))
        print("Division of these numbers is ",a/c)
    else:
        print("Division of these numbers is ",a/b)
else:
    print("Remainder is ",a%b)

        

