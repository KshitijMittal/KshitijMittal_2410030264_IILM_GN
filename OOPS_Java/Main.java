// Write a program to get the current thread and change its name.

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
        Thread t = Thread.currentThread();
        System.out.println(t);
        t.setName("Surabhi Thread");
	System.out.println(t);
    }
}

/*
Output:
Hello World
Thread[#3,main,5,main]
Thread[#3,Surabhi Thread,5,main]
*/