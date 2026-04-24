// Fibonacci Series using non recursive function

import java.util.*;
public class Fibonacci_Series {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of terms in the Fibonacci series: ");
        int n = sc.nextInt();
        sc.close();

        int first = 0, second = 1;

        System.out.print("Fibonacci Series: " + first + ", " + second);

        for (int i = 2; i < n; i++) {
            int next = first + second;
            System.out.print(", " + next);
            first = second;
            second = next;
        }
    }
}

/*
Output:
Enter the number of terms in the Fibonacci series: 7
Fibonacci Series: 0, 1, 1, 2, 3, 5, 8
*/