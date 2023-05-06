#Variables
text = "Hello World!"
number = 42
boolean = True
liste = [1, 2, 3, 4, 5]
tupel = (1, 2, 3, 4, 5)
dictionary = {"key1": "value1", "key2": "value2"}

#Functions
def scoping_function():
    text
    function_text = "Hello World!"
    print("Hello World!")
    return function_text


#function_text cannot be accessed from outside the function as it is has local scope
#print(function_text)

#primitive data types example
text = "Hello World!"
number = 42
boolean = True

