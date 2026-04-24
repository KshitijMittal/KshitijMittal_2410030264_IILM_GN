// Write a program to connect to a database using JDBC and insert values in to it .

import java.sql.*;

public class Insert_Record {
    public static void main(String[] args) {
        try {
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/yourDB", "root", "password");
            PreparedStatement ps = con.prepareStatement(
                "INSERT INTO your_table (id, name) VALUES (?, ?)");
            ps.setInt(1, 101);
            ps.setString(2, "Alice");
            ps.executeUpdate();
            System.out.println("Record inserted");
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