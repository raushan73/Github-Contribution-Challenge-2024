// This program generates the Fibonacci sequence up to a given number.

public class FibonacciSequence {

    public static void main(String[] args) {
        int n = 10;

        // Bug: Incorrect base case initialization
        int a = 0, b = 1; // Fix: Initialize b to 1
        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");
            int temp = a; // Bug: Missing variable to store previous a
            a = b;
            b = temp + a;
        }
    }
}
