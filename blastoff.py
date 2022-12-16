#new recursion that expect a new argument and counts up
def countup(n):
     if n >= 0:
          print('Blastoff!')
     else:
          print(n)
          countup(n+1)
countup(-3)

#output
#-3
#-2
#-1
#Blastoff!
 
