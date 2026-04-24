// Write a program in Java that import the user define package and access the Member variable of classes that Contained by Package

// File: mypackage/My_Class.java
package mypackage;
public class My_Class {
    public String message = "Hello from My_Class in mypackage!";
}
// File: Package_Demo.java
import mypackage.My_Class;

public class Package_Demo {
    public static void main(String[] args) {
        My_Class myObj = new My_Class();
        System.out.println(myObj.message);
    }
}

/*
Output:
Hello from My_Class in mypackage!
 */