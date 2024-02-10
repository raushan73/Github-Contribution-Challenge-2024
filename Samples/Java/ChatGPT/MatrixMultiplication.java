// Program Description: This program seeks to multiply two matrices.

package Samples.Java.ChatGPT;
import java.util.Scanner;

public class MatrixMultiplication {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of rows in first matrix: ");
        int rows1 = scanner.nextInt();
        System.out.print("Enter the number of columns in first matrix: ");
        int cols1 = scanner.nextInt();
        
        int[][] matrix1 = new int[rows1][cols1];
        System.out.println("Enter the elements of the first matrix:");
        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols1; j++) {
                matrix1[i][j] = scanner.nextInt();
            }
        }
        
        System.out.print("Enter the number of rows in second matrix: ");
        int rows2 = scanner.nextInt();
        System.out.print("Enter the number of columns in second matrix: ");
        int cols2 = scanner.nextInt();
        
        int[][] matrix2 = new int[rows2][cols2];
        System.out.println("Enter the elements of the second matrix:");
        for (int i = 0; i < rows2; i++) {
            for (int j = 0; j < cols2; j++) {
                matrix2[i][j] = scanner.nextInt();
            }
        }
        
        if (cols1 != rows2) { // Intentional bug: Incorrect condition for matrix multiplication
            System.out.println("Matrix multiplication is not possible.");
            return;
        }
        
        int[][] result = new int[rows1][cols2];
        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols2; j++) {
                for (int k = 0; k < cols1; k++) {
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }
        
        System.out.println("Resultant matrix:");
        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols2; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
        
        scanner.close();
    }
}

