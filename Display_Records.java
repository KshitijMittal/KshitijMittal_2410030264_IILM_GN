// Write a program that connects to a database using JDBC display all records in a table.

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Display_Records {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/your_database"; // Replace with your database URL
        String user = "your_username"; // Replace with your database username
        String password = "your_password"; // Replace with your database password
        String query = "SELECT * FROM your_table"; // Replace with your table name
        try {
            // Establishing a connection
            Connection connection = DriverManager.getConnection(url, user, password);
            // Creating a statement
            Statement statement = connection.createStatement();
            // Executing the query
            ResultSet resultSet = statement.executeQuery(query);
            // Displaying the records
            while (resultSet.next()) {
                int id = resultSet.getInt("id"); // Replace with your column name
                String name = resultSet.getString("name"); // Replace with your column name
                System.out.println("ID: " + id + ", Name: " + name);
            }
            // Closing the connection
            resultSet.close();
            statement.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

/*
Output:
java.sql.SQLException: No suitable driver found for jdbc:mysql://localhost:3306/your_database
    at java.sql/java.sql.DriverManager.getConnection(DriverManager.java:638)
    at java.sql/java.sql.DriverManager.getConnection(DriverManager.java:199)
    at Display_Records.main(Display_Records.java:16)
*/