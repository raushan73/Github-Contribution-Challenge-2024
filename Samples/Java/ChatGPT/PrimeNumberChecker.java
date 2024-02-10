// Program Description: This program seeks to check if a given number is prime or not.

package Samples.Java.ChatGPT;
import java.util.Scanner;

public class PrimeNumberChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        int num = scanner.nextInt();
        
        boolean isPrime = true;
        if (num <= 1) {
            isPrime = false;
        } else {
            for (int i = 2; i <= Math.sqrt(num); i++) {
                if (num % i == 0) { // Intentional bug: incorrect condition for prime checking
                    isPrime = false;
                    break;
                }
            }
        }
        
        if (isPrime)
            System.out.println(num + " is a prime number.");
        else
            System.out.println(num + " is not a prime number.");
        
        scanner.close();
    }
}

