# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Simple function

# def greet():
#   print("Hello Angela")
#   print("How do you do Jack Bauer?")
#   print("Isn't the weather nice today?")
# greet()

#Functions that allow for input

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")
# greet_with_name("Apollo")

##you are calling the function on line 19, but you can modify it by changing the input. 

## when we call this function name is the paramater
#the PARAMETER is the name of the data that that is being passed in

# The argument is the actual data 

########FUNCTIONS WITH MORE THAN ONE INPUT#####

# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}? ")
# greet_with("Apollo", "New York")

# make sure it matches with the position 
###when you call it on line 33 greet_with it goes by position. So if you did Nowhere, Jack, it would not make sense. 

##FUNCTIONS WITH KEYWORD ARGUMENTS
# def function (a=1, b=2, c=3)not based on position

def greet_with(name="Angela", location="London"):
  print(f"Hello {name}")
  print(f"What is it like in {location}? ")
greet_with("Apollo", "New York")
