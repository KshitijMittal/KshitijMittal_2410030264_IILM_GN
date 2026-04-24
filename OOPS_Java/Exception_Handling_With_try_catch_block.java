// Java program to demonstrate exception handling with try-catch block

import java.util.*;
public class Exception_Handling_With_try_catch_block {
    public static void main (String args[]) {

        Scanner sc = new Scanner (System.in);
        int a, b, c;

        System.out.print ("Enter first number: ");
        a = sc.nextInt();
        System.out.print ("Enter second number: ");
        b = sc.nextInt();

        try {
            c = a / b;
            System.out.println ("Result: " + c);
        }

        catch (Exception e) {
            System.out.println ("Problem in divide");
        }

        System.out.print ("Sorry other work.");
        sc.close();
    }
}

/*
Output:
Enter first number: 10
Enter second number: 0
Problem in divide
Sorry other work.
*/