package Samples.Java.Advanced_ChatGPT;
/*
Program: Two Sum
Aim: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
*/
import java.util.HashMap;

public class TwoSum2 {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                indices[0] = i;
                indices[1] = map.get(complement);
                return indices;
            }
            map.put(nums[i], i);
        }
        return indices;
    }
}

