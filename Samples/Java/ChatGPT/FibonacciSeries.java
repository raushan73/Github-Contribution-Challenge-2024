// Program Description: This program seeks to generate the Fibonacci series up to a given number of terms.

package Samples.Java.ChatGPT;
import java.util.Scanner;

public class FibonacciSeries {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of terms: ");
        int n = scanner.nextInt();
        
        int a = 0, b = 1;
        System.out.println("Fibonacci Series:");
        for (int i = 1; i <= n; i++) {
            System.out.print(a + " ");
            int next = a + b; // Intentional bug: Incorrect Fibonacci calculation
            a = b;
            b = next;
        }
        
        scanner.close();
    }
}
