// Program to demonstrate 'this' keyword
class Thsdemo {
    int a,b;

    public void get(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public void put() {
        System.out.println("a: " + a );
        System.out.println("b: " + b );
    }
}

class This_Keyword {
    public static void main(String[] args) {
        Thsdemo obj = new Thsdemo();
        obj.get(10,20);
        obj.put();
    }
}
