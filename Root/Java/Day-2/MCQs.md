# Java Core Concepts - MCQ Question Bank

## Control Flow (if/else, switch)

### 1. Which statement is used to execute a block of code only when a condition is true?

A. switch  
B. if  
C. for  
D. break

**Answer:** B

---

### 2. What is the output?

```java
int x = 10;

if(x > 5)
    System.out.println("A");
else
    System.out.println("B");
```

A. B  
B. A  
C. Compilation Error  
D. Runtime Error

**Answer:** B

---

### 3. Which keyword is optional in a switch statement?

A. case  
B. switch  
C. default  
D. break

**Answer:** C

---

### 4. Which data types are allowed in switch expressions? (Java 8+)

A. byte
B. short
C. int
D. String
E. All of the above

**Answer:** E

---

### 5. What happens if break is omitted in a switch case?

A. Compilation error  
B. Runtime exception  
C. Fall-through occurs  
D. Program terminates

**Answer:** C

---

# Loops

### 6. How many times will the loop execute?

```java
for(int i=0;i<5;i++)
```

A. 4  
B. 5  
C. 6  
D. Infinite

**Answer:** B

---

### 7. Which loop executes at least once?

A. for  
B. while  
C. do-while  
D. foreach

**Answer:** C

---

### 8. What is the output?

```java
int i=1;

while(i<=3){
    System.out.print(i);
    i++;
}
```

A. 123  
B. 0123  
C. 1234  
D. Infinite Loop

**Answer:** A

---

### 9. Which loop is best when the number of iterations is known?

A. while  
B. do-while  
C. for  
D. switch

**Answer:** C

---

### 10. Which keyword skips the current iteration?

A. break  
B. continue  
C. return  
D. exit

**Answer:** B

---

# Arrays

### 11. What is the index of the first element in an array?

A. 1  
B. 0  
C. -1  
D. Depends on JVM

**Answer:** B

---

### 12. What is the output?

```java
int[] arr={10,20,30};

System.out.println(arr.length);
```

A. 2  
B. 3  
C. 4  
D. Error

**Answer:** B

---

### 13. Which exception occurs when accessing an invalid index?

A. NullPointerException  
B. ArithmeticException  
C. ArrayIndexOutOfBoundsException  
D. IllegalArgumentException

**Answer:** C

---

### 14. Arrays in Java are:

A. Dynamic  
B. Fixed-size  
C. Immutable  
D. Linked

**Answer:** B

---

### 15. Which statement correctly declares an array?

A. int arr[];  
B. int[] arr;  
C. Both A and B  
D. None

**Answer:** C

---

# Strings

### 16. Strings are:

A. Mutable  
B. Immutable  
C. Dynamic  
D. Primitive

**Answer:** B

---

### 17. Which method compares string contents?

A. ==  
B. compare  
C. equals()  
D. match()

**Answer:** C

---

### 18. What is the output?

```java
String s="Java";
System.out.println(s.length());
```

A. 3  
B. 4  
C. 5  
D. Error

**Answer:** B

---

### 19. Which class is mutable?

A. String  
B. StringBuffer  
C. Both StringBuilder and StringBuffer  
D. None

**Answer:** C

---

### 20. What does substring(1,4) return for "Java"?

A. Jav  
B. ava  
C. ava  
D. va

**Answer:** C

---

# Packages

### 21. Which keyword defines a package?

A. import  
B. package  
C. class  
D. include

**Answer:** B

---

### 22. Which package is imported automatically?

A. java.util  
B. java.lang  
C. java.io  
D. java.net

**Answer:** B

---

### 23. Which keyword imports classes?

A. package  
B. class  
C. import  
D. include

**Answer:** C

---

# Wrapper Classes

### 24. Wrapper class for int?

A. Int  
B. Integer  
C. Number  
D. Long

**Answer:** B

---

### 25. Wrapper class for double?

A. Double  
B. Decimal  
C. Float  
D. Number

**Answer:** A

---

### 26. What is Autoboxing?

A. Object to primitive conversion  
B. Primitive to Wrapper conversion  
C. Wrapper creation by JVM  
D. None

**Answer:** B

---

### 27. What is Unboxing?

A. Primitive to Object  
B. Wrapper to Primitive  
C. Object destruction  
D. None

**Answer:** B

---

# Static vs Instance Members

### 28. Static members belong to:

A. Object  
B. Class  
C. Method  
D. Constructor

**Answer:** B

---

### 29. Which can be accessed without creating an object?

A. Instance variable  
B. Static variable  
C. Non-static method  
D. Constructor

**Answer:** B

---

### 30. How many copies of a static variable exist?

A. One per object  
B. One per class  
C. One per method  
D. Unlimited

**Answer:** B

---

# Varargs

### 31. What does varargs allow?

A. Variable return types  
B. Variable number of arguments  
C. Variable class names  
D. Variable constructors

**Answer:** B

---

### 32. Which syntax is correct?

A. int... nums  
B. int nums...  
C. ...int nums  
D. int[]...

**Answer:** A

---

### 33. Where must varargs appear?

A. First parameter  
B. Middle parameter  
C. Last parameter  
D. Anywhere

**Answer:** C

---

# Inner Classes

### 34. A class inside another class is called:

A. Nested Class  
B. Child Class  
C. Wrapper Class  
D. Package Class

**Answer:** A

---

### 35. Which inner class does not require an outer object?

A. Member Inner Class  
B. Anonymous Class  
C. Static Nested Class  
D. Local Class

**Answer:** C

---

### 36. Anonymous classes are primarily used for:

A. Packages  
B. One-time implementations  
C. Constructors  
D. Arrays

**Answer:** B

---

# Collections Framework

### 37. Which interface is at the root of Collection hierarchy?

A. Map  
B. Iterator  
C. Iterable  
D. Set

**Answer:** C

---

### 38. Which interface stores duplicate elements?

A. Set  
B. List  
C. Map  
D. Queue

**Answer:** B

---

### 39. Which interface stores unique elements?

A. List  
B. Queue  
C. Set  
D. Stack

**Answer:** C

---

# ArrayList

### 40. ArrayList internally uses:

A. Linked List  
B. Dynamic Array  
C. Tree  
D. Hash Table

**Answer:** B

---

### 41. Which operation is fastest in ArrayList?

A. Middle insertion  
B. Random access  
C. Deletion at beginning  
D. Deletion in middle

**Answer:** B

---

### 42. Does ArrayList allow duplicates?

A. Yes  
B. No

**Answer:** A

---

# LinkedList

### 43. LinkedList implements:

A. List only  
B. Queue only  
C. List and Deque  
D. Set

**Answer:** C

---

### 44. Which is faster for insertion?

A. ArrayList  
B. LinkedList  
C. Same  
D. Depends

**Answer:** B

---

# Set

### 45. Which Set maintains insertion order?

A. HashSet  
B. TreeSet  
C. LinkedHashSet  
D. EnumSet

**Answer:** C

---

### 46. Which Set stores sorted elements?

A. HashSet  
B. TreeSet  
C. LinkedHashSet  
D. HashMap

**Answer:** B

---

# Map

### 47. Which Map stores key-value pairs?

A. Set  
B. List  
C. Map  
D. Queue

**Answer:** C

---

### 48. Are duplicate keys allowed in HashMap?

A. Yes  
B. No

**Answer:** B

---

### 49. Does HashMap allow null keys?

A. Yes (one)  
B. No

**Answer:** A

---

### 50. Which Map maintains sorted keys?

A. HashMap  
B. LinkedHashMap  
C. TreeMap  
D. Hashtable

**Answer:** C

---

# Iterator

### 51. Which method checks availability of next element?

A. next()  
B. hasNext()  
C. hasPrevious()  
D. remove()

**Answer:** B

---

### 52. Which method returns next element?

A. get()  
B. hasNext()  
C. next()  
D. fetch()

**Answer:** C

---

### 53. Iterator supports:

A. Forward traversal only  
B. Backward traversal only  
C. Both directions  
D. Random access

**Answer:** A

---

# ListIterator

### 54. ListIterator supports:

A. Forward only  
B. Backward only  
C. Both directions  
D. Random traversal

**Answer:** C

---

### 55. Which method moves backward?

A. previous()  
B. back()  
C. moveBack()  
D. last()

**Answer:** A

---

# Generics

### 56. Main benefit of Generics?

A. Faster execution  
B. Type safety  
C. Smaller memory  
D. JVM optimization

**Answer:** B

---

### 57. Which declaration is correct?

```java
List<String> list = new ArrayList<>();
```

A. Correct  
B. Incorrect

**Answer:** A

---

### 58. Generics help avoid:

A. Compilation  
B. Casting  
C. Objects  
D. Loops

**Answer:** B

---

# Collections Utility Class

### 59. Which method sorts a collection?

A. Collections.sort()  
B. Arrays.sort()  
C. sort()  
D. Utility.sort()

**Answer:** A

---

### 60. Which method reverses a list?

A. reverse()  
B. Collections.reverse()  
C. flip()  
D. invert()

**Answer:** B

---

### 61. Which method randomizes list elements?

A. reverse()  
B. rotate()  
C. shuffle()  
D. random()

**Answer:** C

---

# Serialization

### 62. Which interface enables serialization?

A. Serializable  
B. Cloneable  
C. Iterable  
D. Comparable

**Answer:** A

---

### 63. Serialization converts:

A. Object to Byte Stream  
B. Byte Stream to Object  
C. String to Object  
D. File to Memory

**Answer:** A

---

### 64. Deserialization converts:

A. Object to Stream  
B. Stream to Object  
C. Array to Object  
D. File to String

**Answer:** B

---

# serialVersionUID

### 65. serialVersionUID is:

A. Method  
B. Constructor  
C. Version identifier  
D. Interface

**Answer:** C

---

### 66. Missing serialVersionUID may lead to:

A. Runtime Optimization  
B. InvalidClassException  
C. NullPointerException  
D. ArithmeticException

**Answer:** B

---

# transient Keyword

### 67. transient fields are:

A. Serialized  
B. Ignored during serialization  
C. Immutable  
D. Static

**Answer:** B

---

### 68. Which field should typically be transient?

A. Password  
B. Name  
C. Age  
D. Salary

**Answer:** A

---

# Deep Copy vs Shallow Copy

### 69. Shallow copy copies:

A. Objects only  
B. References  
C. Files  
D. Methods

**Answer:** B

---

### 70. Deep copy creates:

A. Same object  
B. New independent object  
C. Shared reference  
D. Null object

**Answer:** B

---

### 71. Which copy consumes more memory?

A. Shallow Copy  
B. Deep Copy

**Answer:** B

---

### 72. Which copy avoids side effects?

A. Shallow Copy  
B. Deep Copy

**Answer:** B

---

# Frequently Asked Certification-Level Questions

### 73. Can HashSet contain null?

A. Yes  
B. No

**Answer:** A

---

### 74. Can TreeSet contain null?

A. Yes  
B. No

**Answer:** B

---

### 75. Can ArrayList contain null values?

A. Yes  
B. No

**Answer:** A

---

### 76. Which collection is synchronized?

A. ArrayList  
B. Vector  
C. HashSet  
D. HashMap

**Answer:** B

---

### 77. Which class is thread-safe?

A. StringBuilder  
B. StringBuffer  
C. Both  
D. None

**Answer:** B

---

### 78. Which collection allows duplicate elements and preserves insertion order?

A. HashSet  
B. TreeSet  
C. ArrayList  
D. HashMap

**Answer:** C

---

### 79. Which collection provides O(1) average lookup?

A. HashMap  
B. TreeMap  
C. LinkedList  
D. TreeSet

**Answer:** A

---

### 80. Which collection is best for frequent insertions and deletions?

A. ArrayList  
B. LinkedList  
C. TreeSet  
D. HashMap

**Answer:** B

---
**Total MCQs: 80**
(Covers Java fundamentals, collections, generics, serialization, and interview/certification-level concepts.)
