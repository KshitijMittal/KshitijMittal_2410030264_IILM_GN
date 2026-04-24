// 4th Program
public class Data_Types_Info {
    public static void main(String[] args) {

        System.out.println("===== PRIMITIVE DATA TYPES =====");
        System.out.println("byte:");
        System.out.println("Size: " + Byte.BYTES + " bytes");
        System.out.println("Range: " + Byte.MIN_VALUE + " to " + Byte.MAX_VALUE);
        System.out.println();

        System.out.println("short:");
        System.out.println("Size: " + Short.BYTES + " bytes");
        System.out.println("Range: " + Short.MIN_VALUE + " to " + Short.MAX_VALUE);
        System.out.println();

        System.out.println("int:");
        System.out.println("Size: " + Integer.BYTES + " bytes");
        System.out.println("Range: " + Integer.MIN_VALUE + " to " + Integer.MAX_VALUE);
        System.out.println();

        System.out.println("long:");
        System.out.println("Size: " + Long.BYTES + " bytes");
        System.out.println("Range: " + Long.MIN_VALUE + " to " + Long.MAX_VALUE);
        System.out.println();

        System.out.println("float:");
        System.out.println("Size: " + Float.BYTES + " bytes");
        System.out.println("Range: " + Float.MIN_VALUE + " to " + Float.MAX_VALUE);
        System.out.println();

        System.out.println("double:");
        System.out.println("Size: " + Double.BYTES + " bytes");
        System.out.println("Range: " + Double.MIN_VALUE + " to " + Double.MAX_VALUE);
        System.out.println();

        System.out.println("char:");
        System.out.println("Size: " + Character.BYTES + " bytes");
        System.out.println("Range: " + (int) Character.MIN_VALUE + " to " + (int) Character.MAX_VALUE);
        System.out.println();

        System.out.println("boolean:");
        System.out.println("Size: Not precisely defined (typically 1 bit or 1 byte)");
        System.out.println("Range: true or false");
        System.out.println();

        System.out.println("===== NON-PRIMITIVE DATA TYPES =====");
        System.out.println("String: Represents a sequence of characters. Size varies based on content.");
        System.out.println("Array: Container object that holds fixed number of values of a single type.");
        System.out.println("Class: Blueprint for creating objects.");
        System.out.println("Object: Root class of all Java classes.");
    }
}

/*
Output:
===== PRIMITIVE DATA TYPES =====
byte:
Size: 1 bytes
Range: -128 to 127

short:
Size: 2 bytes
Range: -32768 to 32767

int:
Size: 4 bytes
Range: -2147483648 to 2147483647

long:
Size: 8 bytes
Range: -9223372036854775808 to 9223372036854775807

float:
Size: 4 bytes
Range: 1.4E-45 to 3.4028235E38

double:
Size: 8 bytes
Range: 4.9E-324 to 1.7976931348623157E308

char:
Size: 2 bytes
Range: 0 to 65535

boolean:
Size: Not precisely defined (typically 1 bit or 1 byte)
Range: true or false

===== NON-PRIMITIVE DATA TYPES =====
String: Represents a sequence of characters. Size varies based on content.
Array: Container object that holds fixed number of values of a single type.
Class: Blueprint for creating objects.
Object: Root class of all Java classes.
*/