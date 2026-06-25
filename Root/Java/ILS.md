LAB 1: Primitive Data Types, Ranges, Casting, and Overflow 📌 Objective
Declare all 8 primitives, observe guaranteed ranges via wrapper
constants, demonstrate numeric literals (L, F), perform casts, and
reproduce overflow/underflow.

🔹 Step 1 --- Declare All Primitives File: PrimitiveBasics.java

public class PrimitiveBasics { public static void main(String\[\] args)
{ byte b = 30; short s = 32000; int i = 1_420_000_000; long dist =
9_460_730_472_580_800L;

        float rate = 4.5F;
        double temp = 36.625;

        char grade = 'A';
        boolean active = true;

        System.out.println(b + " " + s + " " + i + " " + dist);
        System.out.println(rate + " " + temp);
        System.out.println(grade + " " + active);
    }

} 🔹 Step 2 --- Print Fixed Ranges Add to main:

System.out.println("byte:" + Byte.MIN_VALUE + " to " + Byte.MAX_VALUE);
System.out.println("short:" + Short.MIN_VALUE + " to " +
Short.MAX_VALUE); System.out.println("int:" + Integer.MIN_VALUE + " to
" + Integer.MAX_VALUE); System.out.println("long:" + Long.MIN_VALUE + "
to " + Long.MAX_VALUE); System.out.println("float:" + Float.MIN_VALUE +
" to " + Float.MAX_VALUE); System.out.println("double:" +
Double.MIN_VALUE + " to " + Double.MAX_VALUE);
System.out.println("char:" + (int)Character.MIN_VALUE + " to " +
(int)Character.MAX_VALUE); 🔹 Step 3 --- Narrowing and Widening Casts
int big = 130; byte narrowed = (byte) big; System.out.println("130 cast
to byte =" + narrowed);

double d = 42.9; int truncated = (int) d; System.out.println("42.9 cast
to int =" + truncated);

long widened = i; System.out.println("int -\> long =" + widened); 🔹
Step 4 --- Overflow/Underflow Demo int max = Integer.MAX_VALUE;
System.out.println("MAX_INT + 1 =" + (max + 1));

int min = Integer.MIN_VALUE; System.out.println("MIN_INT - 1 =" + (min -
1)); 🔹 Step 5 --- Compile & Run javac PrimitiveBasics.java java
PrimitiveBasics ✅ Conclusion: Learned all primitives, type ranges,
casting, and overflow behavior.

LAB 2: Floating-Point Behavior --- Precision, Rounding, and Comparisons
📌 Objective Explore float vs double precision, rounding artifacts,
formatting, and safe comparison patterns.

🔹 Step 1 --- Create Demo File: FloatDoubleDemo.java

public class FloatDoubleDemo { public static void main(String\[\] args)
{ float f1 = 0.1F + 0.2F; double d1 = 0.1 + 0.2;

        System.out.println("float  0.1F + 0.2F = " + f1);
        System.out.println("double 0.1  + 0.2  = " + d1);

        double x = 1.0 - 0.9;
        double y = 0.2 - 0.1;

        System.out.println("x = " + x + ", y = " + y);
    }

} 🔹 Step 2 --- Format Output System.out.printf("x = %.20f, y =
%.20f%n", x, y); 🔹 Step 3 --- Safe Comparison with Epsilon double eps =
1e-9; System.out.println("x ≈ y ?" + (Math.abs(x - y) \< eps)); 🔹 Step
4 --- Compile & Run javac FloatDoubleDemo.java java FloatDoubleDemo ✅
Conclusion: Observed floating-point precision and safe comparison using
epsilon.

LAB 3: Reference Types --- Aliasing, null, and Value vs Reference
Semantics 📌 Objective Demonstrate that reference variables hold
addresses, not objects, and show aliasing, null, and method parameter
semantics.

🔹 Step 1 --- Define Simple Class File: Person.java

public class Person { String name; } 🔹 Step 2 --- Aliasing in Action
File: RefDemo.java

public class RefDemo { public static void main(String\[\] args) { Person
p1 = new Person(); p1.name = "Alice";

        Person p2 = p1;
        p2.name = "Bob";

        System.out.println(p1.name);

        int a = 10;
        int b = a;
        b = 20;
        System.out.println("a = " + a + ", b = " + b);
    }

} 🔹 Step 3 --- null and NPE Person p3 = null; try { p3.name = "X"; }
catch (NullPointerException e) { System.out.println("Caught NPE:" +
e.getMessage()); } 🔹 Step 4 --- Method Parameter Semantics static void
rename(Person x) { x.name = "Updated"; } static void reassign(Person x)
{ x = new Person(); x.name = "New"; }

public static void main(String\[\] args) { Person p = new Person();
p.name = "Init";

    rename(p);
    System.out.println(p.name);

    reassign(p);
    System.out.println(p.name);

} 🔹 Step 5 --- Compile & Run javac Person.java RefDemo.java java
RefDemo ✅ Conclusion: Understood aliasing, null, and Java's
pass-by-value behavior with references.

LAB 4: Access Modifiers --- public, private, protected, default 📌
Objective Enforce visibility rules across packages and inheritance using
all four access modifiers.

🔹 Step 1 --- Create Package Structure src/ com/example/a/ Base.java
SamePackage.java com/example/b/ Sub.java Other.java 🔹 Step 2 --- Base
Class with All Modifiers src/com/example/a/Base.java

package com.example.a;

public class Base { public int pub = 1; protected int prot = 2; int pack
= 3; private int priv = 4;

    public void show() {
        System.out.println(pub + " " + prot + " " + pack + " " + priv);
    }

} 🔹 Step 3 --- Same Package Access src/com/example/a/SamePackage.java

package com.example.a;

public class SamePackage { public static void main(String\[\] args) {
Base b = new Base(); System.out.println(b.pub);
System.out.println(b.prot); System.out.println(b.pack); //
System.out.println(b.priv); // error } } 🔹 Step 4 --- Subclass in
Another Package src/com/example/b/Sub.java

package com.example.b;

import com.example.a.Base;

public class Sub extends Base { public static void main(String\[\] args)
{ Sub s = new Sub(); System.out.println(s.pub);
System.out.println(s.prot); // System.out.println(s.pack); // error //
System.out.println(s.priv); // error } } 🔹 Step 5 --- Non-subclass in
Another Package src/com/example/b/Other.java

package com.example.b;

import com.example.a.Base;

public class Other { public static void main(String\[\] args) { Base b =
new Base(); System.out.println(b.pub); // System.out.println(b.prot); //
error // System.out.println(b.pack); // error //
System.out.println(b.priv); // error } } 🔹 Step 6 --- Compile & Run
javac -d out \$(find src -name "\*.java") java -cp out
com.example.a.SamePackage java -cp out com.example.b.Sub java -cp out
com.example.b.Other ✅ Conclusion: Learned public is universal, private
is class-only, protected is for subclass (even across packages), and
default is package-only.

LAB 4: Access Modifiers --- public, private, protected, default 📌
Objective Enforce visibility rules across packages and inheritance using
all four access modifiers.

🔹 Step 1 --- Create Package Structure src/ com/example/a/ Base.java
SamePackage.java com/example/b/ Sub.java Other.java 🔹 Step 2 --- Base
Class with All Modifiers src/com/example/a/Base.java

package com.example.a;

public class Base { public int pub = 1; protected int prot = 2; int pack
= 3; private int priv = 4;

    public void show() {
        System.out.println(pub + " " + prot + " " + pack + " " + priv);
    }

} 🔹 Step 3 --- Same Package Access src/com/example/a/SamePackage.java

package com.example.a;

public class SamePackage { public static void main(String\[\] args) {
Base b = new Base(); System.out.println(b.pub);
System.out.println(b.prot); System.out.println(b.pack); //
System.out.println(b.priv); // error } } 🔹 Step 4 --- Subclass in
Another Package src/com/example/b/Sub.java

package com.example.b;

import com.example.a.Base;

public class Sub extends Base { public static void main(String\[\] args)
{ Sub s = new Sub(); System.out.println(s.pub);
System.out.println(s.prot); // System.out.println(s.pack); // error //
System.out.println(s.priv); // error } } 🔹 Step 5 --- Non-subclass in
Another Package src/com/example/b/Other.java

package com.example.b;

import com.example.a.Base;

public class Other { public static void main(String\[\] args) { Base b =
new Base(); System.out.println(b.pub); // System.out.println(b.prot); //
error // System.out.println(b.pack); // error //
System.out.println(b.priv); // error } } 🔹 Step 6 --- Compile & Run
javac -d out \$(find src -name "\*.java") java -cp out
com.example.a.SamePackage java -cp out com.example.b.Sub java -cp out
com.example.b.Other ✅ Conclusion: Learned public is universal, private
is class-only, protected is for subclass (even across packages), and
default is package-only.

LAB 6: final --- Variables, Methods, and Classes 📌 Objective Enforce
immutability by preventing reassignment, overriding, and inheritance.

🔹 Step 1 --- Final Variables File: FinalVars.java

public class FinalVars { public static void main(String\[\] args) {
final int MAX = 500;

        final StringBuilder sb = new StringBuilder("A");
        sb.append("B");

        System.out.println(sb.toString());
    }

} 🔹 Step 2 --- Final Method File: BankAccount.java

class BankAccount { public final void calculateInterest() {
System.out.println("Base formula"); } }

class Savings extends BankAccount { // Cannot override
calculateInterest() } 🔹 Step 3 --- Final Class File: MathUtil.java

public final class MathUtil { public static int add(int a, int b) {
return a + b; } } 🔹 Step 4 --- Compile & Run javac FinalVars.java
BankAccount.java MathUtil.java java FinalVars ✅ Conclusion: final
provides safety by freezing variables, methods, and classes.

LAB 6: final --- Variables, Methods, and Classes 📌 Objective Enforce
immutability by preventing reassignment, overriding, and inheritance.

🔹 Step 1 --- Final Variables File: FinalVars.java

public class FinalVars { public static void main(String\[\] args) {
final int MAX = 500;

        final StringBuilder sb = new StringBuilder("A");
        sb.append("B");

        System.out.println(sb.toString());
    }

} 🔹 Step 2 --- Final Method File: BankAccount.java

class BankAccount { public final void calculateInterest() {
System.out.println("Base formula"); } }

class Savings extends BankAccount { // Cannot override
calculateInterest() } 🔹 Step 3 --- Final Class File: MathUtil.java

public final class MathUtil { public static int add(int a, int b) {
return a + b; } } 🔹 Step 4 --- Compile & Run javac FinalVars.java
BankAccount.java MathUtil.java java FinalVars ✅ Conclusion: final
provides safety by freezing variables, methods, and classes.
