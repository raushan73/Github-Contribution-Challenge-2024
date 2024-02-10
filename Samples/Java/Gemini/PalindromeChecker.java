// This program checks if a given string is a palindrome.

public class PalindromeChecker {

    public static void main(String[] args) {
        String text = "racecar";

        // Bug: Incorrect character comparison (ignoring case)
        boolean isPalindrome = true;
        for (int i = 0; i < text.length() / 2; i++) {
            if (text.charAt(i) != text.charAt(text.length() - 1 - i)) { // Fix: Compare lowercase characters
                isPalindrome = false;
                break;
            }
        }

        System.out.println(text + " is a palindrome: " + isPalindrome);
    }
}
