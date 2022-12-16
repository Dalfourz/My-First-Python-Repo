#defining the power of pi
#calculate the volume of the sphere
def print_volume(r):
    pi = 3.1415926535897932
    sphere_volume = (4/3)*pi*(r**3)
    print(sphere_volume)

#defining the value of the radius
print('Sphere volume 1 is:')
print_volume(10)    #input 1, r = 10
print(' ')  #blank spare for easy to read
#output 1
#Sphere volume 1 is:
#4188.790204786391

print('Sphere volume 2 is:')
print_volume(15)    #input 2 r = 15
#output 2
#Sphere volume 2 is:
#14137.166941154068

print(' ')  #blank spare for easy to read
print('Sphere volume 3 is:')
print_volume(50)    #input 3 r = 50
#output 3
#Sphere volume 3 is:
#523598.7755982988
