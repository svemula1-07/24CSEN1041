def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)  

number = int(input("Enter a non-negative number: "))

factorial_number = 1

if number < 0:
    print("Entered a negative number. Factorial cannot be determined")
else:
    for i in range(1, number + 1):   
        factorial_number *= i
    print(f"Factorial of {number} is {factorial_number}")

    
    print(f"\nUsing recursive method Factorial of {number} is {recursive_factorial(number)}")


 OUTPUT
Enter a non-negative number: 6
Factorial of 6 is 720

Using recursive method Factorial of 6 is 720

