// Super Method in Java

class Superclass{
    public Superclass(){
        System.out.println("First Constructor of Superclass");
    }
    public Superclass(int n){
        System.out.println("Second Constructor of Superclass with value: " + n);
    }
}

class Subclass extends Superclass{
    public Subclass(){
        System.out.println("First Constructor of Subclass");
    }
    public Subclass(int n){
        System.out.println("Second Constructor of Subclass with value: " + n);
    }
}

public class Super_Method {
    public static void main(String[] args) {
        Subclass obj1 = new Subclass();
        System.out.println(obj1);
    }
}
