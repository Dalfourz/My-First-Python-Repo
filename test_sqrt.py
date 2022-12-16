import math                 #importing the math function
def my_sqrt(a):             #the square root function using Newton's method
    x = 1
    while True:
         y = (x + a/x) / 2.0
         if y == x:
              break
         x = y
    return x                #returning the x value

def test_sqrt():
    a = 0
    while a < 25:           #looping range 1- 25 using while loop
        a = a + 1           #incrimental increase
        c = my_sqrt(a)      #my_sqrt function
        d = math.sqrt(a)    #the built-in math sqrt python function
        e = abs(c - d)      #the difference between the my_sqrt and math.sqrt
        print("a = ", a,"| my_sqrt = ", c, "| math.sqrt = ", d, "| diff = ", e)
    return

test_sqrt()
