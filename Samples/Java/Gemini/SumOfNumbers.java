// This program calculates the sum of all numbers from 1 to a given input number.

public class SumOfNumbers {

    public static void main(String[] args) {
        int n = 10; // Change this to any number
        int sum = 0;

        // Bug: Incorrect loop condition
        for (int i = 1; i <= n; i += 2) { // Fix: Change += 2 to += 1
            sum += i;
        }

        System.out.println("Sum of numbers from 1 to " + n + " is: " + sum);
    }
}
