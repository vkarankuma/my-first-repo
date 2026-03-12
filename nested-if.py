num = int(input ("enter your value: "))

if(num % 2 == 0):
    print("even number")
    if(num > 0):
        print("positive number")
    else:
        print("not a positive number")
else:
    print("it is an odd number")