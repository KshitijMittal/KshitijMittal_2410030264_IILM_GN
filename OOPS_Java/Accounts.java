// WAP to design accounts class and two functions withdraw() and deposit()

class Account_Holder {
    private double balance;

    // Constructor
    public Account_Holder(double initialBalance) {
        balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount + " | New Balance: " + balance);
        }
    }

    public void withdraw(double amount) {
      if (amount <= balance) {
        balance -= amount;
        System.out.println("Withdrew: " + amount + " | New Balance: " + balance);
      } else {
           System.out.println("Insufficient Balance! Current: " + balance);
      }
    }

}
public class Accounts {
    public static void main(String[] args) {
        Account_Holder acc1 = new Account_Holder(1000);
        acc1.deposit(500);
        acc1.withdraw(200);
        acc1.withdraw(2000);
    }
}

/*
Output:
Deposited: 500.0 | New Balance: 1500.0
Withdrew: 200.0 | New Balance: 1300.0
Insufficient Balance! Current: 1300.0
*/