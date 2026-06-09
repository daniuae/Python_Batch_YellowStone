# Object-Oriented Programming (OOP) in Python for Kids 🧒🐍

## What is OOP?

Imagine you have many toys:

- 🚗 Toy Cars
- 🐶 Toy Dogs
- 🤖 Robots
- 🎮 Game Characters

Each toy has:

- Things it **has** (color, name, size)
- Things it **does** (run, bark, move)

OOP helps us create things in Python just like real life.

---

# OOP Formula

```text
Class = Blueprint

Object = Real Thing

Attributes = What it Has

Methods = What it Does
```

Example:

```text
Dog
 |
 |-- Name = Bruno
 |-- Color = Brown
 |
 |-- Bark()
 |-- Run()
```

---

# 1. What is a Class?

A class is a blueprint or template.

Think of a cookie cutter.

```text
Cookie Cutter = Class

Cookies Made = Objects
```

Python Example:

```python
class ToyCar:
    pass
```

Here, `ToyCar` is just a blueprint.

---

# 2. What is an Object?

An object is a real thing created from a class.

```python
car1 = ToyCar()
car2 = ToyCar()
```

Now we have two toy cars.

```text
ToyCar (Blueprint)
      |
      |---- car1
      |
      |---- car2
```

---

# 3. Attributes (What an Object Has)

Every toy car can have:

- Color
- Brand

```python
class ToyCar:

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
```

Create Cars:

```python
car1 = ToyCar("Red", "Hot Wheels")
car2 = ToyCar("Blue", "Tesla")
```

Access Attributes:

```python
print(car1.color)
print(car1.brand)
```

Output:

```text
Red
Hot Wheels
```

---

# 4. Methods (What an Object Does)

Cars can do things.

```python
class ToyCar:

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print("Vroom Vroom!")
```

Use It:

```python
car1 = ToyCar("Red", "Hot Wheels")

car1.drive()
```

Output:

```text
Vroom Vroom!
```

---

# What is self?

Imagine you have two toy cars.

```python
car1 = ToyCar("Red", "Hot Wheels")
car2 = ToyCar("Blue", "Tesla")
```

When you write:

```python
car1.drive()
```

Python thinks:

```text
Which car should drive?
```

Answer:

```python
self = car1
```

When:

```python
car2.drive()
```

Then:

```python
self = car2
```

### Simple Meaning

```text
self = Me
self = This Object
```

---

# Example: Dog Class 🐶

Kids love animals!

```python
class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof Woof!")
```

Create Dogs:

```python
dog1 = Dog("Tommy")
dog2 = Dog("Bruno")
```

Use Them:

```python
dog1.bark()
dog2.bark()
```

Output:

```text
Tommy says Woof Woof!
Bruno says Woof Woof!
```

---

# Four Main OOP Concepts

---

# 1. Encapsulation 🔒

Keeping important things safe inside an object.

Example:

```python
class Hero:

    def __init__(self):
        self.health = 100
```

The hero keeps its own health.

Real-Life Example:

```text
Piggy Bank keeps money safe.
```

---

# 2. Inheritance 👨‍👦

Children get qualities from their parents.

```python
class Animal:

    def eat(self):
        print("Eating")
```

Dog inherits from Animal.

```python
class Dog(Animal):
    pass
```

Use It:

```python
dog = Dog()

dog.eat()
```

Output:

```text
Eating
```

Explanation:

```text
Dog is an Animal.
So Dog can do everything Animal can do.
```

---

# 3. Polymorphism 🎭

Same action, different behavior.

Dog:

```python
class Dog:

    def sound(self):
        print("Woof")
```

Cat:

```python
class Cat:

    def sound(self):
        print("Meow")
```

Use Both:

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```text
Woof
Meow
```

Same method:

```python
sound()
```

Different results.

---

# 4. Abstraction 🎮

Using something without knowing how it works inside.

Example:

```text
Press Jump Button
Character Jumps
```

You don't know the game code.

Similarly:

```python
car.start()
```

You don't need to know how the engine works.

You simply use it.

---

# Real-Life Example: Student

Blueprint:

```python
class Student:
    pass
```

Create Students:

```python
rahul = Student()
priya = Student()
```

Students Have:

```text
Name
Age
Grade
```

Students Can:

```text
Study()
Play()
WriteExam()
```

---

# Complete Example

```python
class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print(self.name, "is studying")

    def play(self):
        print(self.name, "is playing")


student1 = Student("Rahul", 5)
student2 = Student("Priya", 5)

student1.study()
student2.play()
```

Output:

```text
Rahul is studying
Priya is playing
```

---

# Quick Revision

| Concept | Meaning | Example |
|----------|----------|----------|
| Class | Blueprint | Dog |
| Object | Real Thing | Bruno |
| Attribute | What it Has | Name, Color |
| Method | What it Does | Bark(), Run() |
| Encapsulation | Keeping data safe | Piggy Bank |
| Inheritance | Child gets parent features | Dog → Animal |
| Polymorphism | Same action, different result | Dog Sound, Cat Sound |
| Abstraction | Use without knowing details | TV Remote |

---

# One-Line Definition

> OOP is a way of creating objects in Python that behave like real-world things. Objects have attributes (what they have) and methods (what they do).

## Remember

```text
Class = Blueprint

Object = Real Thing

Attributes = What it Has

Methods = What it Does
```

🎉 Congratulations! You have learned the basics of OOP in Python.
