// Write a program to implement following collections
//  a) array List
//  b) Vector

import java.util.ArrayList;
import java.util.Vector;
public class Collection_Demo {
    public static void main(String[] args) {
        // a) ArrayList
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("Apple");
        arrayList.add("Banana");
        arrayList.add("Cherry");

        System.out.println("ArrayList elements:");
        for (String fruit : arrayList) {
            System.out.println(fruit);
        }

        // b) Vector
        Vector<String> vector = new Vector<>();
        vector.add("Dog");
        vector.add("Cat");
        vector.add("Rabbit");

        System.out.println("\nVector elements:");
        for (String animal : vector) {
            System.out.println(animal);
        }
    }
}

/*
Output:
ArrayList elements:
Apple
Banana
Cherry
Vector elements:
Dog
Cat
Rabbit
*/