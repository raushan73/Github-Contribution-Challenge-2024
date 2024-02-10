# Program: Given a string s, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    hashmap = {}
    max_length = start = 0
    for i, char in enumerate(s):
        if char in hashmap and start <= hashmap[char]:
            start = hashmap[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        hashmap[char] = i
    return max_length

# Test case
string = "abcabcbb"
print(lengthOfLongestSubstring(string))  # Expected output: 3
