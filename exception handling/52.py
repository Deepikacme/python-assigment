def factorial(n):
        if n<0:
            raise ValueError("Invalid number")

        fact=1
        for i in range(1,n+1):
            fact=fact*i

        print("Factorial:", fact)
print(not factorial(-5))
factorial(-5)