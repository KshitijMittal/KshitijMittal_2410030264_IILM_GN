// SUper Keyword in Java

class Superclass{
    int a, b;

    public void get(int x, int y) {
        a = x;
        b = y;
    }
}

class Subclass extends Superclass{
    int a, b;

    public void set(){
        this.a = super.a;
        this.b = super.b;
    }
    public void put(){
        System.out.println("a: " + a);
        System.out.println("b: " + b);
    }
}

public class Super_Keyword {
    public static void main(String[] args) {
        Subclass obj = new Subclass();
        obj.get(10,20);
        obj.set();
        obj.put();
    }
}
