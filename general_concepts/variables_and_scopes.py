# Variables can be used to store different types of data.
# Here also eg number is inferred to be an integer or eg text is inferred to be a string.
text = "Hello World!"
number = 42
boolean = True
liste = [1, 2, 3, 4, 5]
tupel = (1, 2, 3, 4, 5)
dictionary = {"key1": "value1", "key2": "value2"}

print("before function: " + text)

# scoping example
def scoping_function(): 
    print("inside function: " + text)
    function_text = "Hello World!"
    return function_text

scoping_function()

print("after function: " + text)

# function_text cannot be accessed from outside the function as it is has local scope
#print(function_text)

# primitive data types example
text = "Hello World!"
number = 42
boolean = True

