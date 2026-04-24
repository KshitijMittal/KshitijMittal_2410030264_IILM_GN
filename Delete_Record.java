// Write a java program to connect to a database using JDBC and delete values from table .

import java.sql.*;
public class Delete_Record {
    public static void main(String[] args) {
        try {
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/yourDB", "root", "password");
            PreparedStatement ps = con.prepareStatement(
                "DELETE FROM your_table WHERE id = ?");
            ps.setInt(1, 101);
            ps.executeUpdate();
            System.out.println("Record deleted");
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