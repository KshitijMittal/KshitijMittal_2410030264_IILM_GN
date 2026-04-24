// Write a program in Java to create a thread that Implement the Runnable interface

class MyRunnable implements Runnable {
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Thread " + Thread.currentThread().getName() + " - Count: " + i);
            try {
                Thread.sleep(500); // Sleep for 500 milliseconds
            } catch (InterruptedException e) {
                System.out.println("Thread interrupted: " + e.getMessage());
            }
        }
    }
}

public class Runnable_Demo {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new MyRunnable());
        Thread thread2 = new Thread(new MyRunnable());

        thread1.start();
        thread2.start();
    }
}

/*
Output:
Thread Thread-0 - Count: 1
Thread Thread-1 - Count: 1

Thread Thread-0 - Count: 2
Thread Thread-1 - Count: 2

Thread Thread-0 - Count: 3
Thread Thread-1 - Count: 3

Thread Thread-0 - Count: 4
Thread Thread-1 - Count: 4

Thread Thread-0 - Count: 5
Thread Thread-1 - Count: 5
*/