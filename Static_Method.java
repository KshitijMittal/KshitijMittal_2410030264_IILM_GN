// Java program to demonstrate static method

public class Static_Method {
    // static variable
     static int a = 40;
    // instance variable
    int b = 50;

    void simpleDisplay()
    {
        System.out.println(a);
        System.out.println(b);
    }
    // Declaration of a static method
    static void staticDisplay()
    {
      System.out.println(a);
    }
    // main method
    public static void main(String[] args)
    {
        Static_Method obj = new Static_Method();
        obj.simpleDisplay();

        // Calling static method
        Static_Method.staticDisplay();
        staticDisplay();
    }
}

/*
Output:
40
50
40
40
*/