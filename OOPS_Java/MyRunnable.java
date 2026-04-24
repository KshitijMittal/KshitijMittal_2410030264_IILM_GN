// Write a program to demonstrate the use of Runnable interface to create a thread in Java.

class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Thread running using Runnable interface");
    }

    public static void main(String[] args) {
        MyRunnable myRunnable = new MyRunnable();
        Thread t1 = new Thread(myRunnable); // pass runnable to Thread
        t1.start(); // start the thread
        System.out.println("Main thread");
    }
}

/*
Output:
Thread running using Runnable interface
Main thread
*/