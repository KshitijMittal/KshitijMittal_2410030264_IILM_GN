// Write a program in Java to show the inheritance in java and use of super keyword.

class Person {
    String name = "John";

    public void display() {
        System.out.println("Person Name: " + name);
    }
}

class Student extends Person {
    String name = "Alice";

    public void display() {
        super.display();  // calls parent method
        System.out.println("Student Name: " + name);
    }
}

public class Inheritance_Demo_Super_Keyword {
    public static void main(String[] args) {
        Student s = new Student();
        s.display();
    }
}

/*
Output:
Person Name: John
Student Name: Alice
*/