#this function will return a zero division error if you entered 0 as the value of "m", which is one of the runtime error
print("n / m")
n = int(input('Please enter a number from 1 to 10 for "n"... '))
m = int(input('Please enter 0 or 1 for "m"... '))
def runtime_error():
    if m == 0:
        print("0")
    else:
        a = n/m
        print("Result is :",int(a))

#how to fix

#we can add the error by adding the following lines of code
#if m == 0:
#        print("0")
#    else:
#        a = n/m
#        print("Result is :",int(a))



