import java.util.ArrayList;
import java.util.List;

public class ArrayListExample {

    public static void main(String[] args) {

        // Create an ArrayList
        List<String> names = new ArrayList<>();

        // Add elements
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        // Display the original list
        System.out.println("Original List:");
        System.out.println(names);

        // Fast index access - O(1)
        String first = names.get(0);
        System.out.println("\nFirst Element: " + first);

        // Append a new element
        names.add("Diana");
        System.out.println("\nAfter Adding Diana:");
        System.out.println(names);

        // Remove the element at index 1 ("Bob")
        names.remove(1);

        System.out.println("\nAfter Removing Bob:");
        System.out.println(names);

        // Display elements using a for-each loop
        System.out.println("\nIterating through the list:");

        for (String name : names) {
            System.out.println(name);
        }

        // Size of the list
        System.out.println("\nList Size: " + names.size());

        // Check if an element exists
        System.out.println("Contains Alice? " + names.contains("Alice"));

        // Replace an element
        names.set(1, "Chris");

        System.out.println("\nAfter Replacing Charlie with Chris:");
        System.out.println(names);

        // Remove all elements
        names.clear();

        System.out.println("\nAfter clear():");
        System.out.println(names);
        System.out.println("Is Empty? " + names.isEmpty());
    }
}
