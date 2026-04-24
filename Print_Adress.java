// Write a program to print your address

public class Print_Adress {
    public static void main(String[] args) {

        //using single println statement
        System.out.println("---- Using single println statement ----");
        System.out.println("Address: 123 Main Street, City, Country, Zip Code");

        //using multiple println statements
        System.out.println("---- Using multiple println statements ----");
        System.out.println("Address:");
        System.out.println("123 Main Street");
        System.out.println("City, Country");
        System.out.println("Zip Code: 123456");
    }
}

/*
Output:
---- Using single println statement ----
Address: 123 Main Street, City, Country, Zip Code
---- Using multiple println statements ----
Address:
123 Main Street
City, Country
Zip Code: 123456
*/