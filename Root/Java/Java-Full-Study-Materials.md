# Java Complete Developer Guide

## Table of Contents

1. Control Flow
2. Loops
3. Arrays
4. Strings
5. Packages
6. Wrapper Classes
7. Static vs Instance Members
8. Varargs
9. Inner Classes
10. Collections Framework
11. List, Set, Map
12. Iterator & ListIterator
13. Generics
14. Collections Utility Class
15. Serialization
16. Classes & Objects
17. Constructors
18. Method Overloading & Overriding
19. Inheritance
20. Abstraction
21. Interfaces vs Abstract Classes
22. Encapsulation
23. Polymorphism
24. final, this, super
25. Composition vs Inheritance
26. Static vs Dynamic Binding
27. SOLID Principles
28. Multithreading
29. Executors & Futures
30. Synchronization & Locks
31. Deadlocks & Race Conditions
32. Exception Handling
33. Custom Exceptions
34. Try-With-Resources
35. Logging
36. File Handling
37. Serialization & Deserialization
38. Directory Traversal
39. Streams API
40. Date & Time API
41. Regular Expressions
42. HTTP Client API
43. JDBC Architecture
44. CRUD Operations
45. Transactions
46. Stored Procedures
47. CompletableFuture
48. Concurrent Collections
49. HikariCP Connection Pooling
50. Recommended GitHub Repositories

---

# 1. Control Flow

## If Else

```java
int age = 20;

if(age >= 18){
    System.out.println("Adult");
}else{
    System.out.println("Minor");
}
```

### Flow Diagram

```text
       age >=18 ?
          |
      +---+---+
      |       |
    Yes      No
      |       |
   Adult    Minor
```

---

## Switch

```java
String day = "MON";

switch(day){
    case "MON":
        System.out.println("Monday");
        break;

    case "TUE":
        System.out.println("Tuesday");
        break;

    default:
        System.out.println("Unknown");
}
```

---

# 2. Loops

## For Loop

```java
for(int i=1;i<=5;i++){
    System.out.println(i);
}
```

## While Loop

```java
int i=1;

while(i<=5){
    System.out.println(i);
    i++;
}
```

## Do While

```java
int i=1;

do{
    System.out.println(i);
    i++;
}
while(i<=5);
```

---

# 3. Arrays

```java
int[] nums = {10,20,30,40};

for(int n : nums){
    System.out.println(n);
}
```

Memory Layout

```text
nums
 |
 v
+----+----+----+----+
|10  |20  |30  |40  |
+----+----+----+----+
```

---

# 4. Strings

```java
String name = "Dani";

System.out.println(name.length());
System.out.println(name.toUpperCase());
System.out.println(name.substring(1));
```

---

# 5. Packages

```java
package com.company.utils;

public class MathUtil {
}
```

Import

```java
import com.company.utils.MathUtil;
```

---

# 6. Wrapper Classes

Primitive → Object

```java
int x = 100;

Integer obj = x;      // Autoboxing
int y = obj;          // Unboxing
```

| Primitive | Wrapper   |
| --------- | --------- |
| int       | Integer   |
| double    | Double    |
| float     | Float     |
| long      | Long      |
| boolean   | Boolean   |
| char      | Character |

---

# 7. Static vs Instance Members

```java
class Employee{

    static String company="ABC";

    String name;
}
```

Memory

```text
Class Area
-----------
company

Heap
-----------
Employee1
Employee2
```

---

# 8. Varargs

```java
public static int sum(int... nums){

    int total = 0;

    for(int n : nums){
        total += n;
    }

    return total;
}
```

Usage

```java
sum(1,2);
sum(1,2,3,4);
```

---

# 9. Inner Classes

```java
class Outer{

    class Inner{

        void display(){
            System.out.println("Inner Class");
        }
    }
}
```

---

# 10. Collections Framework

```text
Collection
│
├── List
│   ├── ArrayList
│   └── LinkedList
│
├── Set
│   └── HashSet
│
└── Map
    └── HashMap
```

---

# 11. List, Set, Map

## ArrayList

```java
List<String> names = new ArrayList<>();

names.add("Java");
names.add("Python");
```

## LinkedList

```java
LinkedList<Integer> list = new LinkedList<>();
list.add(10);
list.add(20);
```

## HashSet

```java
Set<Integer> nums = new HashSet<>();

nums.add(1);
nums.add(1);

System.out.println(nums);
```

Output

```text
[1]
```

## HashMap

```java
Map<Integer,String> map = new HashMap<>();

map.put(1,"Dani");
map.put(2,"John");

System.out.println(map.get(1));
```

---

# 12. Iterator

```java
Iterator<String> itr = names.iterator();

while(itr.hasNext()){
    System.out.println(itr.next());
}
```

---

# 13. Generics

```java
List<String> list = new ArrayList<>();
```

Benefits:

* Type Safety
* Compile-Time Checking
* No Explicit Casting

---

# 14. Collections Utility

```java
Collections.sort(list);
Collections.reverse(list);
Collections.shuffle(list);
```

---

# 15. Serialization

Object → Byte Stream

```text
Object
   |
Serialization
   |
Bytes
   |
File
```

```java
class Employee implements Serializable{

    private static final long serialVersionUID = 1L;

    String name;
}
```

Transient Example

```java
transient String password;
```

---

# 16. Classes & Objects

```java
class Car{

    String brand;

    void start(){
        System.out.println("Started");
    }
}
```

Object

```java
Car car = new Car();
```

---

# 17. Constructors

```java
class Car{

    Car(){
        System.out.println("Created");
    }
}
```

---

# 18. Method Overloading

```java
int add(int a,int b)

int add(int a,int b,int c)
```

Compile-Time Polymorphism

---

# 19. Method Overriding

```java
class Animal{
    void sound(){}
}

class Dog extends Animal{

    @Override
    void sound(){
        System.out.println("Bark");
    }
}
```

Runtime Polymorphism

---

# 20. Inheritance

```java
class Dog extends Animal{
}
```

---

# 21. Abstraction

```java
abstract class Shape{

    abstract double area();
}
```

---

# 22. Interfaces

```java
interface Payment{

    void pay();
}
```

---

# 23. Interface vs Abstract Class

| Feature              | Interface          | Abstract Class |
| -------------------- | ------------------ | -------------- |
| Multiple Inheritance | Yes                | No             |
| Constructors         | No                 | Yes            |
| State                | Limited            | Yes            |
| Methods              | Abstract + Default | Both           |

---

# 24. Encapsulation

```java
class Employee{

    private String name;

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name=name;
    }
}
```

---

# 25. Polymorphism

```java
Animal a = new Dog();
```

---

# 26. this, super, final

```java
this.name = name;
super();
final int MAX = 100;
```

---

# 27. Composition vs Inheritance

Inheritance

```java
Car extends Vehicle
```

Composition

```java
class Car{
    Engine engine;
}
```

Prefer Composition.

---

# 28. SOLID Principles

```text
S - Single Responsibility
O - Open Closed
L - Liskov Substitution
I - Interface Segregation
D - Dependency Inversion
```

---

# 29. Multithreading

```java
class MyThread extends Thread{

    public void run(){
        System.out.println("Running");
    }
}
```

---

# 30. Executor Service

```java
ExecutorService service =
    Executors.newFixedThreadPool(4);

service.submit(() ->
    System.out.println("Task")
);

service.shutdown();
```

---

# 31. Future

```java
Future<Integer> future =
    service.submit(() -> 100);

System.out.println(future.get());
```

---

# 32. Synchronization

```java
synchronized void increment(){
    count++;
}
```

---

# 33. Locks

```java
Lock lock = new ReentrantLock();

lock.lock();

try{
    count++;
}
finally{
    lock.unlock();
}
```

---

# 34. Race Condition

```text
Thread-1 count++
Thread-2 count++

Incorrect Result
```

---

# 35. Deadlock

```text
Thread-1 holds Lock A waits for Lock B

Thread-2 holds Lock B waits for Lock A
```

---

# 36. Exception Hierarchy

```text
Throwable
│
├── Error
│
└── Exception
     │
     └── RuntimeException
```

---

# 37. Try Catch Finally

```java
try{
    int x = 10/0;
}
catch(Exception e){
    e.printStackTrace();
}
finally{
    System.out.println("Done");
}
```

---

# 38. Custom Exception

```java
class AgeException extends Exception{

    public AgeException(String msg){
        super(msg);
    }
}
```

---

# 39. Try With Resources

```java
try(FileReader fr =
    new FileReader("a.txt")){

}
```

---

# 40. Logging

```java
Logger logger =
    Logger.getLogger("App");

logger.info("Started");
```

---

# 41. File Handling

```java
FileInputStream fis =
    new FileInputStream("input.txt");

FileOutputStream fos =
    new FileOutputStream("output.txt");
```

---

# 42. Serialization & Deserialization

```java
ObjectOutputStream out =
    new ObjectOutputStream(
        new FileOutputStream("emp.ser")
    );

out.writeObject(emp);
```

```java
ObjectInputStream in =
    new ObjectInputStream(
        new FileInputStream("emp.ser")
    );

Employee emp =
    (Employee) in.readObject();
```

---

# 43. Directory Traversal

```java
Files.walk(Paths.get("."))
     .forEach(System.out::println);
```

---

# 44. Streams API

## Filter

```java
list.stream()
    .filter(x -> x > 10)
    .forEach(System.out::println);
```

## Map

```java
list.stream()
    .map(String::toUpperCase)
    .forEach(System.out::println);
```

## Reduce

```java
int sum =
    list.stream()
        .reduce(0,Integer::sum);
```

---

# 45. Date & Time API

```java
LocalDate.now();
LocalDateTime.now();
ZonedDateTime.now();
```

---

# 46. Regular Expressions

```java
Pattern p =
    Pattern.compile("\\d+");

Matcher m =
    p.matcher("123");

System.out.println(m.find());
```

---

# 47. HTTP Client API

```java
HttpClient client =
    HttpClient.newHttpClient();
```

---

# 48. JDBC Architecture

```text
Application
    |
 JDBC API
    |
DriverManager
    |
JDBC Driver
    |
Database
```

---

# 49. JDBC CRUD

## Connection

```java
Connection con =
DriverManager.getConnection(
url,user,password);
```

## Insert

```java
PreparedStatement ps =
con.prepareStatement(
"insert into employee values(?)");
```

## Select

```java
ResultSet rs =
stmt.executeQuery(
"select * from employee");
```

---

# 50. Transactions

```java
con.setAutoCommit(false);

con.commit();

con.rollback();
```

---

# 51. Stored Procedure

```java
CallableStatement cs =
con.prepareCall(
"{call getEmployee(?)}");
```

---

# 52. CompletableFuture

```java
CompletableFuture.supplyAsync(
    () -> "Hello"
)
.thenApply(String::toUpperCase)
.thenAccept(System.out::println);
```

---

# 53. ConcurrentHashMap

```java
ConcurrentHashMap<Integer,String> map =
new ConcurrentHashMap<>();
```

---

# 54. CopyOnWriteArrayList

```java
CopyOnWriteArrayList<String> list =
new CopyOnWriteArrayList<>();
```

---

# 55. HikariCP

Maven Dependency

```xml
<dependency>
    <groupId>com.zaxxer</groupId>
    <artifactId>HikariCP</artifactId>
    <version>6.3.0</version>
</dependency>
```

Usage

```java
HikariConfig config =
    new HikariConfig();

config.setJdbcUrl(url);
config.setUsername(user);
config.setPassword(password);

HikariDataSource ds =
    new HikariDataSource(config);

Connection con =
    ds.getConnection();
```

---

# Recommended GitHub Repositories

* OpenJDK
* Java Design Patterns
* Spring PetClinic
* Baeldung Tutorials
* Java Algorithms
* HikariCP

---

# Interview Preparation Order

1. OOP
2. Collections
3. Generics
4. Exception Handling
5. Streams API
6. File I/O
7. Multithreading
8. CompletableFuture
9. JDBC
10. SOLID Principles
11. Concurrent Collections
12. Connection Pooling

---

# End of Guide
