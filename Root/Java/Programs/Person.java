public class Person {
 String name;
}
public class Demo {
 public static void main(String[] args) {
 Person p1 = new Person();
 p1.name = "Alice";
 Person p2 = p1; // both refer to the same object
 p2.name = "Bob";
 System.out.println(p1.name); // prints "Bob"
 }
}
