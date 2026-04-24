// Write a program in Java to handle the Exception using try and multiple catch block.

public class Exception_Demo {
    public static void main(String[] args) {
        try {
            int[] numbers = {1, 2, 3};
            System.out.println(numbers[5]); // This will throw ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index is out of bounds: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            System.out.println("Execution completed.");
        }
    }
}

/*
Output:
Array index is out of bounds: Index 5 out of bounds for length 3
 */