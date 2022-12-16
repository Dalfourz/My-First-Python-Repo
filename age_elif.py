age = 20
if age <18:
  print("still a kid")
elif age>= 50: # at this point we already know that the age MUST be 18 or higher from the first test
  print("An adult, welcome!")
  print("and an elderly as well!")
else: # We can only get to this point if the age is higher than 18 but lower than 50
  print("An adult, welcome!")
  print("but not above 50.")
