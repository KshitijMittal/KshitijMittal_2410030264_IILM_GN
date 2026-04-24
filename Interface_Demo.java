// Write a program in java which implement interface Student which has two methods Display_Grade and Attendance for PG_Students and UG_Students (PG_Students and UG_Students are two different classes for Post Graduate and Under Graduate Students respectively).

interface Student {
    void Display_Grade();
    void Attendance();
}
class PG_Students
implements Student {
    @Override
    public void Display_Grade() {
        System.out.println("PG Student Grade: A");
    }

    @Override
    public void Attendance() {
        System.out.println("PG Student Attendance: 90%");
    }
}
class UG_Students
implements Student {
    @Override
    public void Display_Grade() {
        System.out.println("UG Student Grade: B");
    }

    @Override
    public void Attendance() {
        System.out.println("UG Student Attendance: 85%");
    }
}

public class Interface_Demo {
    public static void main(String[] args) {
        Student pgStudent = new PG_Students();
        Student ugStudent = new UG_Students();

        System.out.println("Post Graduate Student Details:");
        pgStudent.Display_Grade();
        pgStudent.Attendance();

        System.out.println("\nUnder Graduate Student Details:");
        ugStudent.Display_Grade();
        ugStudent.Attendance();
    }
}

/*
Output:
Post Graduate Student Details:
PG Student Grade: A
PG Student Attendance: 90%
Under Graduate Student Details:
UG Student Grade: B
UG Student Attendance: 85%
*/