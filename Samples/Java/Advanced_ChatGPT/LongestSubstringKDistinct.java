package Samples.Java.Advanced_ChatGPT;

/*
Program: Longest Substring with At Most K Distinct Characters
Aim: Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
*/
import java.util.HashMap;

public class LongestSubstringKDistinct {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        HashMap<Character, Integer> map = new HashMap<>();
        int maxLen = 0, left = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            map.put(c, map.getOrDefault(c, 0) + 

