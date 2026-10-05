n=int(input("Enter a number: "))
if n<0:
    raise ValueError("Negative number")
print("Number is positive")
print(n)