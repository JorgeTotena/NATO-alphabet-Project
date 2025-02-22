"""# Dictionary containing student names and their scores
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through the dictionary to access keys and values
for (key, value) in student_dict.items():
    # Access key and value (currently just a placeholder with 'pass')
    pass

# Import the pandas library for data manipulation
import pandas

# Convert the dictionary into a pandas DataFrame
student_data_frame = pandas.DataFrame(student_dict)

# Loop through each row of the DataFrame
for (index, row) in student_data_frame.iterrows():
    # Access the index and row data
    # You can access specific columns like row.student or row.score
    pass

# Keyword Method with iterrows():
# This is a dictionary comprehension that creates a new dictionary by iterating over rows of a DataFrame
# {new_key:new_value for (index, row) in df.iterrows()} """

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

# Import the pandas library, which is used for data manipulation and analysis
import pandas

# Read the NATO phonetic alphabet data from a CSV file into a pandas DataFrame
# The CSV file should have two columns: 'letter' and 'code'
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Convert the data into a pandas DataFrame
# A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types
nato_dataframe = pandas.DataFrame(data)

# Create a dictionary where the key is the letter and the value is the corresponding NATO code
# This is done using a dictionary comprehension, which is a concise way to create dictionaries
# The 'iterrows()' function is used to iterate over the rows of the DataFrame
codes = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Initialize a boolean variable to control the while loop
# This loop will keep asking the user for input until a valid word is entered
pass_criteria = False

# Start a while loop that will continue until 'pass_criteria' is True
while pass_criteria == False:
    # Prompt the user to input a word and convert it to uppercase
    # This ensures that the input matches the keys in the 'codes' dictionary, which are uppercase
    word = input("Type a word: ").upper()

    # Create a list of characters from the input word (all in uppercase)
    # This list comprehension iterates over each character in the word and converts it to uppercase
    characters = [character.upper() for character in word]

    # Use the 'codes' dictionary to map each character to its corresponding NATO phonetic code
    # This is done using a try-except block to handle any potential errors
    try:
        # List comprehension to create a list of phonetic words corresponding to each character
        phonetic_words = [codes[character] for character in characters]
    except KeyError:
        # If a character is not found in the 'codes' dictionary (e.g., a number or symbol),
        # a KeyError will be raised, and this block will execute
        print("Sorry, only letters in the alphabet please")
        # Set 'pass_criteria' to False to continue the loop
        pass_criteria = False
    else:
        # If no KeyError is raised, set 'pass_criteria' to True to exit the loop
        pass_criteria = True
        # Print the list of phonetic code words
        print(phonetic_words)

# Additional note: This code compares every character in the input word against the 'codes' dictionary
# to generate the corresponding NATO phonetic alphabet representation.