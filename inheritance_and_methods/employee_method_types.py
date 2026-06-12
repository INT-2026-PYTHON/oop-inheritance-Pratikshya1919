"""
## 3. Employee Class with Instance, Class & Static Methods  *(Medium)*

=================================================
EMPLOYEE: INSTANCE vs CLASS vs STATIC METHODS
=================================================

Problem Statement:
Write a Python class called `Employee` that
demonstrates the THREE method types in
Python:

   1. INSTANCE method  -> takes `self`
   2. CLASS method     -> decorated with
                          @classmethod,
                          takes `cls`
   3. STATIC method    -> decorated with
                          @staticmethod,
                          takes neither

The class also has a CLASS attribute used by
the class method, and INSTANCE attributes set
in __init__.

-------------------------------------------------
Instructions:
1. Define the class:
      class Employee:
          company    = "Acme Corp"   # class attr
          raise_pct  = 5             # class attr

          def __init__(self, name, salary):
              self.name   = name
              self.salary = salary

2. INSTANCE method:
      def apply_raise(self):
          - increase self.salary by raise_pct %
            (read Employee.raise_pct)

3. CLASS method:
      @classmethod
      def set_raise_percentage(cls, new_pct):
          - cls.raise_pct = new_pct
          - this changes the class attribute
            for EVERY existing and future
            employee at once

      @classmethod
      def from_string(cls, csv_line):
          - csv_line looks like "Alice,90000"
          - split it, build and RETURN a new
            Employee instance using cls(...)
          - this is an ALTERNATE constructor.

4. STATIC method:
      @staticmethod
      def is_valid_salary(amount):
          - return True if amount is an int or
            float AND amount > 0, else False.

5. In the driver code:
      - create two employees using __init__
      - create one employee using
        Employee.from_string("Carol,75000")
      - call apply_raise() on every employee
      - change the global raise via
        Employee.set_raise_percentage(10)
      - call apply_raise() again
      - call Employee.is_valid_salary(...)
        with several values
      - print each employee's name and salary
6. Do NOT use:
   - any external library
   - global keyword

-------------------------------------------------
Input Example:
e1 = Employee("Alice", 100000)
e2 = Employee("Bob",   80000)
e3 = Employee.from_string("Carol,75000")

e1.apply_raise()                  # 5% raise
Employee.set_raise_percentage(10) # change class attr
e2.apply_raise()                  # 10% raise
e3.apply_raise()                  # 10% raise

Output Example:
Alice -> 105000.0
Bob   -> 88000.0
Carol -> 82500.0
is_valid_salary(50000)  -> True
is_valid_salary(-100)   -> False
is_valid_salary("abc")  -> False

=================================================

"""
# Employee class
class Employee:

    # Class attributes
    company = "Acme Corp"
    raise_pct = 5

    # Constructor
    def __init__(self, name, sal):
        self.name = name   # Employee name
        self.sal = sal     # Employee salary

    # Instance method
    def apply_raise(self):
        self.sal = self.sal + (self.sal * Employee.raise_pct / 100)

    # Class method
    @classmethod
    def set_raise_percentage(cls, pct):
        cls.raise_pct = pct

    # Alternate constructor
    @classmethod
    def from_string(cls, data):
        name, sal = data.split(",")#divides the string into pieces at each comma
        return cls(name, float(sal))

    # Static method
    @staticmethod
    def is_valid_salary(x):
        return type(x) in (int, float) and x > 0


# Input for employees
n1 = input("Enter first employee name: ")
s1 = float(input("Enter first employee salary: "))

n2 = input("Enter second employee name: ")
s2 = float(input("Enter second employee salary: "))

data = input("Enter third employee (name,salary): ")

# Objects
e1 = Employee(n1, s1)
e2 = Employee(n2, s2)
e3 = Employee.from_string(data)

# First raise (5%)
e1.apply_raise()
e2.apply_raise()
e3.apply_raise()

# Change raise percentage
pct = float(input("Enter new raise percentage: "))
Employee.set_raise_percentage(pct)

# Second raise
e1.apply_raise()
e2.apply_raise()
e3.apply_raise()

# Employee details
print(f"{e1.name} -> {e1.sal}")
print(f"{e2.name} -> {e2.sal}")
print(f"{e3.name} -> {e3.sal}")

# Static method calls
print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(-100))
print(Employee.is_valid_salary("abc"))

# Instance method -> uses self (object data)

# Class method -> uses cls (class data)

# Static method -> uses neither self nor cls