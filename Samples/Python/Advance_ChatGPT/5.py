# Program: Given a string s, reverse the string word by word.
def reverseWords(s):
    words = s.split()
    return ' '.join(words[::-1])

# Test case
string = "the sky is blue"
print(reverseWords(string))  # Expected output: "blue is sky the"
