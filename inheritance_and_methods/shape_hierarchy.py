"""
## 4. Shape Hierarchy with an Abstract Method  *(Medium)*

=================================================
SHAPE HIERARCHY (PARENT + 3 CHILDREN)
=================================================

Problem Statement:
Build a small inheritance hierarchy:

   Shape   (parent / "abstract" base)
   ├── Circle
   ├── Rectangle
   └── Triangle    (uses Heron's formula for
                    area)

The parent class declares the shape's name
and the methods area() and perimeter() — but
these methods just RAISE NotImplementedError
so that any child class is FORCED to override
them.

This problem teaches:
   - one parent, multiple children
   - the "abstract method" pattern using
     NotImplementedError
   - using super().__init__() in each child
   - storing different attributes per child

-------------------------------------------------
Instructions:
1. Parent class:
      class Shape:
          def __init__(self, name):
              self.name = name

          def area(self):
              raise NotImplementedError(
                  "Child classes must override area()"
              )

          def perimeter(self):
              raise NotImplementedError(
                  "Child classes must override perimeter()"
              )

          def describe(self):
              print(f"{self.name}: "
                    f"area={self.area()}, "
                    f"perimeter={self.perimeter()}")

2. Child class Circle:
      __init__(self, radius)
          - super().__init__("Circle")
          - self.radius = radius
      area()       -> 3.14159 * r * r
      perimeter()  -> 2 * 3.14159 * r

3. Child class Rectangle:
      __init__(self, length, width)
          - super().__init__("Rectangle")
          - store length, width
      area()       -> length * width
      perimeter()  -> 2 * (length + width)

4. Child class Triangle:
      __init__(self, a, b, c)
          - super().__init__("Triangle")
          - store sides a, b, c
      perimeter()  -> a + b + c
      area()       -> Heron's formula:
                       s = perimeter / 2
                       area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

5. In the driver code:
      - create one Shape and call describe()
        in a try/except to see the
        NotImplementedError
      - create at least one Circle, one
        Rectangle, one Triangle
      - put them in a LIST and use a for loop
        to call describe() on each shape
6. Do NOT use:
   - the math module (use 3.14159 as PI)
   - any external library

-------------------------------------------------
Input Example:
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5),
]

Output Example:
Circle: area=78.53975, perimeter=31.4159
Rectangle: area=24, perimeter=20
Triangle: area=6.0, perimeter=12
Shape itself raises NotImplementedError when describe() is called.

-------------------------------------------------
Explanation:
- The parent Shape provides the SHARED logic
  (name + describe()) but refuses to compute
  area/perimeter on its own.
- Each child OVERRIDES area() and perimeter()
  with formulas appropriate for that shape.
- describe() works on ALL shapes through
  POLYMORPHISM: the same method call produces
  different results depending on the actual
  object type.
=================================================

"""
# Parent class
class Shape:

    # Constructor
    def __init__(self, name):
        self.name = name
    #An abstract method is a method without a body that must be implemented by child classes.
    # Abstract method for area
    def area(self):
        raise NotImplementedError(
            "Child classes must override area()"
        )

    # Abstract method for perimeter
    def perimeter(self):
        raise NotImplementedError(
            "Child classes must override perimeter()"
            # Forces child classes to define their own area() method
        )

    # Common method for all shapes
    def describe(self):
        print(f"{self.name}: area={self.area()}, perimeter={self.perimeter()}")


# Child class Circle
class Circle(Shape):

    # Constructor (reuse Shape constructor)
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    # Override area method
    def area(self):
        return 3.14159 * self.radius * self.radius

    # Override perimeter method
    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Child class Rectangle
class Rectangle(Shape):

    # Constructor (reuse Shape constructor)
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    # Override area method
    def area(self):
        return self.length * self.width

    # Override perimeter method
    def perimeter(self):
        return 2 * (self.length + self.width)


# Child class Triangle
class Triangle(Shape):

    # Constructor (reuse Shape constructor)
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    # Override perimeter method
    def perimeter(self):
        return self.a + self.b + self.c

    # Override area method using Heron's formula
    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


# Create Shape object and handle NotImplementedError
s = Shape("Shape")

try:
    s.describe()
except NotImplementedError as e:
    print(e)

# Create Circle object
r = float(input("Enter circle radius: "))
c = Circle(r)

# Create Rectangle object
l = float(input("Enter rectangle length: "))
w = float(input("Enter rectangle width: "))
rect = Rectangle(l, w)

# Create Triangle object
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c_side = float(input("Enter side c: "))
tri = Triangle(a, b, c_side)

# Store all shapes in a list
shapes = [c, rect, tri]

# Use a loop to call describe() for each shape
for shape in shapes:
    shape.describe()