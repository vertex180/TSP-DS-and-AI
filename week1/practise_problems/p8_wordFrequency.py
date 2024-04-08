def alphabet_frequency(string):
    # Initialize an empty dictionary to store frequencies
    frequency_dict = {}

    # Iterate through each character in the string
    for char in string:
        # Check if the character is an English alphabet (uppercase or lowercase)
        if char.isalpha():
            # Convert the character to lowercase for uniformity
            char = char.lower()
            # Increment the frequency count for the character
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    return frequency_dict

#alphabet_frequency('tomato')
print(alphabet_frequency('tomato')) 
