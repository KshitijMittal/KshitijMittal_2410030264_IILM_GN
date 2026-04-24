/* Java program for swapping the value of two positive integer numbers in the following manner :
1. Using 3rd variable
2. Without using 3rd variable */

public class Swapping_the_value_of_two_positive_integer {
    public static void main(String[] args) {
        int a = 5, b = 10;

        // Swapping using a third variable
        System.out.println("Before swapping using third variable: a = " + a + ", b = " + b);
        int temp = a;
        a = b;
        b = temp;
        System.out.println("After swapping using third variable: a = " + a + ", b = " + b);

        // Resetting values
        a = 5;
        b = 10;

        // Swapping without using a third variable
        System.out.println("Before swapping without third variable: a = " + a + ", b = " + b);
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("After swapping without third variable: a = " + a + ", b = " + b);
    }
}