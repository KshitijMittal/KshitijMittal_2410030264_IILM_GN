// Write a program to design simple calculator for (+,-,*, and /) using switch case.

import java.util.*;
public class Simple_Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        float num1 = sc.nextFloat();
        System.out.print("Enter second number: ");
        float num2 = sc.nextFloat();

        System.out.println("Choose an operation: ");
        System.out.println("1. Addition (+)");
        System.out.println("2. Subtraction (-)");
        System.out.println("3. Multiplication (*)");
        System.out.println("4. Division (/)");

        int choice = sc.nextInt();

        switch (choice) {
            case 1:
                System.out.println("Result: " + (num1 + num2));
                break;
            case 2:
                System.out.println("Result: " + (num1 - num2));
                break;
            case 3:
                System.out.println("Result: " + (num1 * num2));
                break;
            case 4:
                if (num2 != 0) {
                    System.out.println("Result: " + (num1 / num2));
                } else {
                    System.out.println("Error: Division by zero is not allowed.");
                }
                break;
            default:
                System.out.println("Invalid choice.");
        }

        sc.close();
    }
}

/*
Output:
Enter first number: 10
Enter second number: 5
Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
1
Result: 15.0
*/