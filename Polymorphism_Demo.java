// WAP in java to the concept of polymorphism by designing functions to sum different types of numbers

class Calculator {

    // Add two integers
    public int add(int a, int b) {
        return a + b;
    }

    // Add two double numbers
    public double add(double a, double b) {
        return a + b;
    }

    // Add three integers
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Add one integer and one double
    public double add(int a, double b) {
        return a + b;
    }

    // Add one double and one integer
    public double add(double a, int b) {
        return a + b;
    }
}

public class Polymorphism_Demo {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        System.out.println("Sum of two integers: " + calc.add(10, 45));
        System.out.println("Sum of two doubles: " + calc.add(12.5, 67.3));
        System.out.println("Sum of three integers: " + calc.add(5, 10, 15));
        System.out.println("Sum of int and double: " + calc.add(10, 12.5));
        System.out.println("Sum of double and int: " + calc.add(7.5, 5));
    }
}

/*
Output:
Sum of two integers: 55
Sum of two doubles: 79.8
Sum of three integers: 30
Sum of int and double: 22.5
Sum of double and int: 12.5
*/