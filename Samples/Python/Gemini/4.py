# Reverses a string inefficiently (with errors)

def reverse_string(text):
    """Reverses the characters in a given string.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.
    """

    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):  # Incorrect loop condition (off-by-one error)
        reversed_text += text[i]  # Inefficient character-by-character concatenation
    return reversed_text

# Example usage
string = "Hello, world!"
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")
