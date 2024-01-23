print("simple calculator")
num1=float(input("enter the number one here : "))
num2=float(input("enter the number two here :" ))
print(" press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for dividation")
choice = int(input(" enter your choice from 1-4 : "))
if choice == 1 :
    print ("the addition of two numbers is " ,num1 + num2)
elif choice == 2 :
    print("the substraction of two numbers is ",num1 - num2)
elif choice == 3 :
    print("the mutipication of two numbers is" ,num1 * num2)
elif choice == 4:
    print("the dividition of two numbers is ",num1/num2)
else:
    print( "invalid input")




    
