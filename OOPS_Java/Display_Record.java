// Write a program that connects to a database using JDBC display all records in a table.

import java.sql.*;

public class Display_Record {
    public static void main(String[] args) {
        try {
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/yourDB", "root", "password");
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM your_table");

            while (rs.next()) {
                System.out.println(rs.getInt(1) + " " + rs.getString(2));
            }

            con.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}

/*
Output:
java.sql.SQLException: No suitable driver found for jdbc:mysql://localhost:3306/yourDB
*/