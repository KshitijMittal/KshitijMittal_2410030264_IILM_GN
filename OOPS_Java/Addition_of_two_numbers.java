// Write a program to add two numbers and display the result (using scanner).

import java.util.*;
public class Addition_of_two_numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();

        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();

        int sum = num1 + num2;

        System.out.println("The sum of " + num1 + " and " + num2 + " is: " + sum);
        sc.close();
    }
}

/*
Output:
Enter first number: 10
Enter second number: 20
The sum of 10 and 20 is: 30
*/