// Write a program to print all real solutions for quadratic equation ax2 + bx + c = 0. Read the values of a,b,c and use the quadratic formula. If the discriminant is negative display a message stating there are no real solutions.

import java.util.* ;
public class Roots_of_Quadratic_Equation {
    public static void main(String[] args) {

        Scanner sc = new Scanner (System.in) ;
        System.out.print("Enter the value of a: ");
        int a = sc.nextInt();
        System.out.print("Enter the value of b: ");
        int b = sc.nextInt();
        System.out.print("Enter the value of c: ");
        int c = sc.nextInt();
        sc.close();

        System.out.println();

        System.out.print("Your quadratic equation is: "+ a + "x^2 + " + b + "x + " + c + " = 0");

        System.out.println();
        System.out.println();

        double D = ((b*b) - (4*a*c));
        System.out.print("The Discriminent of the equation is: "+ D);

        System.out.println();
        System.out.println();

        if (D > 0) {
            System.out.println("The two real roots are:");
            double root1 = (-b + Math.sqrt(D)) / (2*a);
            double root2 = (-b - Math.sqrt(D)) / (2*a);
            System.out.println("Root 1: " + root1);
            System.out.println("Root 2: " + root2);
        } else if (D == 0) {
            System.out.println("The single real root is:");
            double root1 = -b / (2*a);
            System.out.println("Root: " + root1);
        } else {
            System.out.println("There are no real solution for this quadratic equation.");
        }

    }
}

/*
Output:
Enter the value of a: 1
Enter the value of b: -3
Enter the value of c: 2
Your quadratic equation is: 1x^2 + -3x + 2 = 0
The Discriminent of the equation is: 1.0
The two real roots are:
Root 1: 2.0
Root 2: 1.0
*/