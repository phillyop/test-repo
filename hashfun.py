def simple_hash(input_string):
    """
    A simple hash function that calculates the hash value of a string.
    """
    hash_value = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Convert the character to its Unicode code point and add it to the hash_value
        hash_value += ord(char)
    
    return hash_value

# Example usage:
input_str = input("Enter the string: ")
hash_result = simple_hash(input_str.lower())
print(f"The hash value of '{input_str}' is: {hash_result}")
