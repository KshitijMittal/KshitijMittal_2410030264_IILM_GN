// Write a program to calculate the length of a number entered by the user.

import java.util.*;
public class Length_of_a_number {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in) ;
        System.out.print("Enter the number: ");
        int n = sc.nextInt();
        sc.close();

        int length = 0;
        int temp = n;

        if (n == 0) {
            length = 1; // Special case for 0
        } else {
            while (temp != 0) {
                temp /= 10;
                length++;
            }
        }

        System.out.println("The length of the number " + n + " is: " + length);
    }
}

/*
Output:
Enter the number: 12345
The length of the number 12345 is: 5
*/