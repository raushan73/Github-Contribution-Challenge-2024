/**

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

**/

//Given code has used type conversion for solution come up with a code that not uses type conversion
//You need to correct complete function body.
//Do not change class name and method name.

class Solution {
    public String addBinary(String a, String b) {
        if (a == null || a.isEmpty()) return b;
        if (b == null || b.isEmpty()) return a;
        
        int num1 = Integer.parseInt(a, 2);
        int num2 = Integer.parseInt(b, 2);
        
        int sum = num1 + num2;
        return Integer.toBinaryString(sum);
    }
}