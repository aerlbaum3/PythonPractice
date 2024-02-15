def replace_numbers_with_text(input_string):
    # Create a mapping to map each digit to its text representation
    numbers_allocation = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    # Create a mapping to handle numbers between 10 and 19
    teens_allocation = {
        '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
        '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'
    }

    # Create a mapping for the tens place
    tens_allocation = {
        '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
        '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'
    }

    # Split the input string into words
    words = input_string.split()

    # Iterate through the words and replace any numbers with their text representation
    for i in range(len(words)):
        if words[i].isdigit():
            # If the word is a number, replace it with the text representation
            if len(words[i]) == 1:
                words[i] = numbers_allocation[words[i]]
            elif len(words[i]) == 2:
                if words[i][0] == '1':
                    words[i] = teens_allocation[words[i]]
                else:
                    if words[i][1] != '0':
                        words[i] = tens_allocation[words[i][0]] + ' ' + numbers_allocation[words[i][1]]
                    else:
                        words[i] = tens_allocation[words[i][0]]

    # Join the words back into a string
    output_string = ' '.join(words)
    return output_string

# Get user input
user_input = input("Enter a string: ")

# Replace numbers with text and print the result
output_result = replace_numbers_with_text(user_input)
print("Output:", output_result)
