// Java program to demonstrate static block

public class Static_Block {
    // Static Block
    static {
        System.out.println("Static Block Initialized");
    }
    public static void main(String[] args) {
        System.out.println("Main Method");
    }
}

/*
Output:
Static Block Initialized
Main Method
*/