// Write a program to print the multiplication table of a given number, where n is the positive number entered by the user.

import java.util.* ;
public class Print_table {
    public static void main(String[] args) {

        Scanner sc = new Scanner (System.in);
        System.out.print("Enter the value of n: ");
        int n = sc.nextInt();
        sc.close();

        System.out.println();

        System.out.println("Multiplication table of " + n + " is: ");

        System.out.println();

        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n * i));
        }
    }
}

/*
Output:
Enter the value of n: 5
Multiplication table of 5 is:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
*/