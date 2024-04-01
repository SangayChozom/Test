def find_first_repeating_character(s):
    char_count = {}
    for char in s:
        # If character is encountered for the second time
        if char in char_count:
            print(f"First repeating character: {char}, Memory address: {id(char)}")
            return char, id(char)
        else:
            # Store the count of each character encountered
            char_count[char] = 1
    # If no repeating character is found
    print("No repeating character found.")
    return None

# Example:
s = "abcdefgah"
result = find_first_repeating_character(s)
if result is None:
    print("No repeating character found.")