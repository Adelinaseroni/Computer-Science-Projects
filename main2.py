# Imports
import json

# Initialize an empty dictionary to hold clinic data
data = {}

# Load clinic information from text file
file_path = "clinic_info.json"

# Try to open and read the contents of the file
try:
    with open(file_path, 'r', encoding='utf8') as fin:
        data = json.loads(fin.read())
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please make sure it is in the same directory as this script.")
    exit()

# Display welcome message once
print("MEDICAL CHATBOT:", data.get("greeting", "Welcome!"))

# Print the options only once
print("\nPlease enter a number corresponding to the question you would like answered, or type 'exit' to exit:")
for i in range(len(data.get("questions", []))):
    print(f"{i+1}. {data['questions'][i]['question']}")

# User input loop
while True:
    user_input = input("> ").strip()
    if user_input.lower() == 'exit':
        print(f"\nMEDICAL CHATBOT: {data.get('goodbye', 'Goodbye!')}")
        break
    else:
        try:
            print(f"\nMEDICAL CHATBOT: {data['questions'][int(user_input)-1]['answer']}")
        except:
            print("\nMEDICAL CHATBOT: Invalid choice. Please enter a number within the range, or type 'exit' to quit.")
        print("MEDICAL CHATBOT: Any other questions?")
