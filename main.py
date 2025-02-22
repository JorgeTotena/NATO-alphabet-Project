# Dictionary containing student names and their scores
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
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

# Read the NATO phonetic alphabet data from a CSV file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Convert the data into a pandas DataFrame
nato_dataframe = pandas.DataFrame(data)

# Create a dictionary where the key is the letter and the value is the corresponding NATO code
codes = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Prompt the user to input a word and convert it to uppercase
word = input("Type a word: ").upper()

# Create a list of characters from the input word (all in uppercase)
characters = [character.upper() for character in word]

# Use the 'codes' dictionary to map each character to its corresponding NATO phonetic code
phonetic_words = [codes[character] for character in characters]

# Print the list of phonetic code words
print(phonetic_words)

# Additional note: This code compares every character in the input word against the 'codes' dictionary
# to generate the corresponding NATO phonetic alphabet representation.