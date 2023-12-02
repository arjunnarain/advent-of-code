import re

def parse_text_file(file_path):
    final_sum = 0
    """
    Reads a text file line by line and processes each line to find the last number.

    Args:
    file_path (str): Path to the text file.
    """
    try:
        with open('day_1/input.txt', 'r') as file:
            for line in file:
                final_sum += process_line(line)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print(f"The final sum is {final_sum}.")

def process_line(line):
    """
    Processes a single line to find individual digits and spelled-out digits and sum them.

    Args:
    line (str): A line of text.

    Returns:
    int: The calculated number, or None if no number is found.
    """
    # Mapping of spelled-out numbers to their numerical equivalents
    word_to_num = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Find all numerical digits and words that represent digits
    matches = re.findall(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine)\b|\d', line.lower())
    
    if matches:
        # Convert each found word to its corresponding digit
        digit_str = ''.join([word_to_num[match] if match in word_to_num else match for match in matches])
        return int(digit_str)
    else:
        return None

def main():
    file_path = 'example.txt'  # Replace with your file path
    parse_text_file(file_path)

if __name__ == "__main__":
    main()
