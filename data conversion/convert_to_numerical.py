import pandas as pd

# Load the CSV file
file_path = 'data conversion/depression survey(Responses) - Form responses 1 (1).csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Define mappings for converting options to numerical values
mappings = {
    "How often do you feel sad?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How do you feel about the future?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How do you perceive your accomplishments?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Do you enjoy activities as much as you used to?":{
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Do you feel guilty?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Do you feel like you're being punished?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How do you feel about yourself": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Do you blame yourself for problems?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Do you have thoughts of self-harm?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How often do you cry?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Do you feel irritated?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Have you lost interest in others?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "HHow well do you make decisions?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How do you feel about your appearance?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How well do you work?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How well do you sleep?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How often do you feel tired?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How is your appetite?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Have you lost weight?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "Are you worried about your health?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
    },
    "How is your interest in sex?": {
        "Option 0": 0,
        "Option 1": 1,
        "Option 2": 2,
        "Option 3": 3,
        "Option 4": 0,
        "Option 5": 2,
    },

    
    # Repeat for all questions in your dataset
}

# Apply the mappings to convert text to numerical values
for question, mapping in mappings.items():
    if question in data.columns:
        data[question] = data[question].map(mapping)

# Save the converted data to a new CSV file
output_path = 'data conversion/depression survey(numerical_Responses).csv'  # Replace with desired output file path
data.to_csv(output_path, index=False)

print(f"Numerical data saved successfully to {output_path}")
