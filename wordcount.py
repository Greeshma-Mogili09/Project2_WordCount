# Word Counter Program with Enhanced Error Handling

# Function to count words in the user input
def count_words(text):
    # Remove extra spaces and split the text into words
    words = text.strip().split()
    return len(words)

# Main program execution
def main():
    print("Welcome to the Word Counter Program!")
    
    while True:
        # Prompt the user for input
        user_input = input("Please enter a sentence or paragraph: ")

        # Check if input is empty or contains only whitespace
        if not user_input.strip():
            print("Error: No text entered. Please try again.\n")
        else:
            # Count the words and display the result
            word_count = count_words(user_input)
            print(f"\nThe number of words in your text is: {word_count}")
            break  # Exit the loop after successful input

# Call the main function to run the program
if __name__ == "__main__":
    main()

