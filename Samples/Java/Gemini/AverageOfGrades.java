// This program calculates the average grade of students in a class.

public class AverageOfGrades {

    public static void main(String[] args) {
        int[] grades = {85, 92, 78, 95, 80};

        // Bug: Missing element in total calculation
        int total = 0;
        for (int grade : grades) {
            total += grade;
        }

        // Bug: Division by zero (check input array length)
        double average = total / grades.length; // Fix: Divide by actual number of grades

        System.out.println("Average grade: " + average);
    }
}
