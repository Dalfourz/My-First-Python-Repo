import math
def my_sqrt(a):
    x = 1
    while True:
         y = (x + a/x) / 2.0
         if y == x:
              break
         x = y
    return x

def test_sqrt():
    a = 0
    for a in range(25):
        a = a + 1
        c = my_sqrt(a)
        d = math.sqrt(a)
        e = abs(c - d)
        print("a = ", a,"| my_sqrt = ", c, "| math.sqrt = ", d, "| diff = ", e)
    return

test_sqrt()


