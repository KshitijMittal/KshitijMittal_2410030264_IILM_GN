// Write a program that works as a simple calculator. Use a Grid Layout to arrange Buttons for digits and for the + - * % operations. Add a text field to display the result.

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Grid_Calculator extends JFrame implements ActionListener {
    private JTextField display;
    private JPanel panel;
    private String[] buttons = {
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", "C", "=", "+"
    };
    private String operator;
    private double num1, num2, result;

    public Grid_Calculator() {
        display = new JTextField();
        display.setEditable(false);
        display.setHorizontalAlignment(JTextField.RIGHT);

        panel = new JPanel();
        panel.setLayout(new GridLayout(4, 4));

        for (String text : buttons) {
            JButton button = new JButton(text);
            button.addActionListener(this);
            panel.add(button);
        }

        this.setLayout(new BorderLayout());
        this.add(display, BorderLayout.NORTH);
        this.add(panel, BorderLayout.CENTER);
        this.setTitle("Grid Calculator");
        this.setSize(300, 400);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        if ("0123456789".contains(command)) {
            display.setText(display.getText() + command);
        } else if (command.equals("C")) {
            display.setText("");
            operator = null;
            num1 = num2 = result = 0;
        } else if (command.equals("=")) {
            if (operator != null) {
                num2 = Double.parseDouble(display.getText());
                switch (operator) {
                    case "+":
                        result = num1 + num2;
                        break;
                    case "-":
                        result = num1 - num2;
                        break;
                    case "*":
                        result = num1 * num2;
                        break;
                    case "/":
                        if (num2 != 0) {
                            result = num1 / num2;
                        } else {
                            display.setText("Error: Div by 0");
                            return;
                        }
                        break;
                }
                display.setText(String.valueOf(result));
                operator = null;
            }
        } else {
            if (!display.getText().isEmpty()) {
                num1 = Double.parseDouble(display.getText());
                operator = command;
                display.setText("");
            }
        }
    }
    public static void main(String[] args) {
        new Grid_Calculator();
    }
}

/*
Output:
A GUI window opens with a calculator layout. Users can click buttons to perform calculations. The display shows the input and results.
*/