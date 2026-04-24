// Write a program to print all odd numbers from 1 to n, where n is a number entered by the user.

import java.util.* ;
public class Print_Odd_number {
    public static void main(String[] args) {

        Scanner sc = new Scanner (System.in) ;
        System.out.print("Enter the value of n: ");
        int n = sc.nextInt();
        sc.close();

        System.out.println();

        System.out.print("The odd numbers from 1 to " + n + " are: ");

        System.out.println();

        for (int i = 1; i <= n; i++) {
            if (i % 2 != 0) {
                System.out.print(i + " ");
            }
        }

    }
}

/*
Output:
Enter the value of n: 10
The odd numbers from 1 to 10 are:
1 3 5 7 9
*/