def learned_function(first_name, last_name):     #this function will print first and last name
  print(first_name + " " + last_name)

def frames():           #this function will print out 18 lines meant to frame the name
    def lines():
        print('-'*18)
    lines()

print('Input 1')    
frames()        #top frame
learned_function(" Julius", "Only Name")    #using value as an argument
frames()        #bottom frame
#output 1
#------------------
# Julius Only Name
#------------------

print(' ')      #extra space for easy to read
print('Input 2')
no_way = "Julius " + "Only Name"
hey = "Is " + "good"
frames()        #top frame
learned_function(no_way,hey)                #using expression as an argument
frames()        #bottom frame
#output 2
#------------------
#Julius Only Name Is good
#------------------

print(' ')      #extra space for easy to read
print('Input 3')    
frames()        #top frame
this = " I am"
program = "the best"
learned_function(this,program)              #using variable as an argument
frames()        #bottom frame
#output 3
#------------------
# I am the best
#------------------
