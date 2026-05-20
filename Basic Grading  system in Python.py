score=float(input("Enter the total marks "))
a=float(input("Enter the maximum possible marks "))
if a==0:
    print("Maximum marks are wrong recheck")
else:
    d=(score/a)*100
    if 100>=d>90:
        print("The grade is A")
        print("Your percentage is: ", d)
    elif 90>=d>80:
        print("The grade is B")
        print("Your percentage is: ", d)
    elif 80>=d>60:
        print("The grade is C")
        print("Your percentage is: ", d) 
    elif 60>=d>35:
        print("The grade is D")
        print("Your percentage is: ", d)
    elif 35>=d>0:
        print("The grade is E essential repeat required")
        print("Your percentage is: ", d)
    else:
        print("Marks are wrong recheck")
