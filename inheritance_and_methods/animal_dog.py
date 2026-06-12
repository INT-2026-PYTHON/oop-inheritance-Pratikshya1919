"""
## 1. Animal -> Dog with super()  *(Easy)*

=================================================
ANIMAL AND DOG (INHERITANCE BASICS)
=================================================

Problem Statement:
Write two classes that demonstrate the
simplest case of single inheritance:

   - Animal       (PARENT class)
   - Dog          (CHILD class that inherits
                    from Animal)

The Dog class must EXTEND Animal, not replace
it. Use the `super()` keyword to call the
parent's `__init__` instead of repeating the
code in the child class.

-------------------------------------------------
Instructions:
1. Define the parent class:
      class Animal:
          def __init__(self, name, sound):
              self.name  = name
              self.sound = sound

          def speak(self):
              print(f"{self.name} says {self.sound}")

2. Define the child class:
      class Dog(Animal):
          def __init__(self, name, breed):
              - call super().__init__(name, "Woof")
                so the parent stores name and sound
              - then set self.breed = breed

          def describe(self):
              print(f"{self.name} is a {self.breed}")

3. In the driver code:
      - create one Animal (e.g. a cat) and call
        speak()
      - create at least TWO Dog objects of
        different breeds and call BOTH speak()
        (inherited from Animal) AND describe()
        (defined on Dog)
4. Do NOT use:
   - any external library
   - manually copying parent __init__ code
     into the child (must use super())

-------------------------------------------------
Input Example:
a = Animal("Cat", "Meow")
d1 = Dog("Buddy", "Labrador")
d2 = Dog("Rex",   "Beagle")

Output Example:
Cat says Meow
Buddy says Woof
Buddy is a Labrador
Rex says Woof
Rex is a Beagle

=================================================

"""
# Parent class
class Animal:

    #initialize animal name and sound
    def __init__(self, name, sound):#self refers to the current object that is using the class
        self.name = name 
        self.sound = sound
         # Instance attribute for animal name and sound

    # Method to display the sound made by the animal
    def speak(self):
        print(f"{self.name} says {self.sound}")
        #self is used to refer to the current object and access its attributes and methods


# Child class inheriting properties and methods from Animal
class Dog(Animal):

    # Constructor to initialize dog name and breed
    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # Call parent constructor

        #super() is used to access the parent class's methods and constructor from a child class.

        self.breed = breed

    # Method to display dog details
    def describe(self):
        print(f"{self.name} is a {self.breed}")


# Taking input for Animal object
animal_name = input("Enter animal name: ")
animal_sound = input("Enter animal sound: ")

a = Animal(animal_name, animal_sound)

# Taking input for first Dog object
dog1_name = input("Enter first dog name: ")
dog1_breed = input("Enter first dog breed: ")

# Taking input for second Dog object
dog2_name = input("Enter second dog name: ")
dog2_breed = input("Enter second dog breed: ")

d1 = Dog(dog1_name, dog1_breed)
d2 = Dog(dog2_name, dog2_breed)

# Calling methods
a.speak()

d1.speak()
d1.describe()

d2.speak()
d2.describe()
