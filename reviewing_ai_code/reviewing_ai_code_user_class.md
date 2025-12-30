class User:
    """
    Represents a user.
    """
    def __init__(self, name, age=0, email=None):
        self.name = name
        self.age = int(age)
        self.email = email

    def is_adult(self):
        return self.age >= 18

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"

Note: the above code was written by chatGPT

How the code works:
    - The code creates a class to represent a user
    - The initialization function initializes three variables and assigns them
      to the following:
        - self.name to the name parameter
        - self.age to the integer parsed version of the age parameter, which
          is set to 0 if a value is not passed
        - self.email to the passed email parameter, which is set to None if 
          an email is not parsed
    - The is_adult method determines whether self.age is >= 18, and outputs 
      the boolean True/False value
    - The __repr__ method defines how an instance of the class represents
      itself, e.g.
        - u = User("John")
          print(u) # will print "User(name=John, age=0, email=None)"

Good aspects of the code:
    - Program logic easy to understand
    - All variables appropriately named

Risky aspects of the code:
    - If no name is given when instantiating a user, then a TypeError would
      occur
    - If age isn't an intger then this may cause a ValueError when parsing to
      an integer
    - Currently the program will still work if name and email are not strings,
      however this is likely assumed and future methods may result in errors if 
      they rely on them being strings   

Improvements:
    - name could be set to None by default in the initialization function
    - Raise a TypeError if isinstance(age, int) is False and set self.age to
      age without parsing it to an integer
    - Raise a TypeError if isinstance(name, str) is False in the initialization
      function and then set self.name to name without parsing it to a string
    - Raise a TypeError if isinstance(email, str) is False in the initialization
      function and then set self.email to email without parsing it to a string
    - The docstring could be more descriptive and explain what the default 
      values for name, age and email are and explain what the is_adult and __repr__ functions do 


