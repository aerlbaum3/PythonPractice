def replace_numbers_with_text(input_string):
    # create a allocation to map each digit to its text representation
    numbers_allocation = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    # Split the string into words
    words = input_string.split()

    # Iterate through the words and replace any numbers with their text representation
    for i in range(len(words)):
        if words[i].isdigit():
            # If the word is a number, replace it with the text representation
            words[i] = number_dict[words[i][0]]

    # Join the words back into a string
    output_string = ' '.join(words)

    return output_string

# Get user input
#This is the main
user_input = input("Enter a string: ")

# Replace numbers with text and print the result
output_result = replace_numbers_with_text(user_input)
print("Output:", output_result)
