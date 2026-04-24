// Write a program to read a number metre and convert it into feet and display the result.

import java.util.* ;
public class Meter_to_Feet {
    public static void main(String[] args) {

        Scanner sc = new Scanner (System.in);
        System.out.print("Enter the value in meters: ");
        float a = sc.nextFloat();
        sc.close();

        System.out.print("Your value in feet is "+ (a * 3.2808399));

    }
}

/*
Output:
Enter the value in meters: 10
Your value in feet is 32.808399
*/