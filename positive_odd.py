a=int(input("enter an integer(positive or negative)"))
if a > 0:
    print("the number is positive")
    if a % 2 == 0:
        print("the number is even")
    else:
          print("the number is odd")
elif a < 0:
         print("the number is negative")
else:
        print("the number is zero")
                
