// // Java program to demonstrate static variable

class demo {
    static int num = 3;

    public void set() {
        num ++;
    }

    public void get() {
        System.out.println("num: " + num);
    }
}

class Static_Variable {
    public static void main(String[] args) {
        demo obj1 = new demo();
        demo obj2 = new demo();
        demo obj3 = new demo();

        obj1.set();
        obj2.set();
        obj3.set();

        obj3.set();
        obj3.set();
        obj3.set();

        obj1.get();
        obj2.get();
        obj3.get();
    }
}

/*
Output:
num: 9
num: 9
num: 9
*/