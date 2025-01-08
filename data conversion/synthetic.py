import pandas as pd
from imblearn.over_sampling import SMOTE

# Load the dataset
file_path = '/home/najiya/queen_puzzle/mental-health-analysis-using-BERT/data conversion/depression survey(numerical_stResponses).csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Drop the 'Timestamp' column
data = data.drop(columns=['Timestamp'])

# Define the target column (e.g., 'How often do you feel sad?' or another column if it's a classification task)
target_column = 'How often do you feel sad?'  # Replace with the actual target column for SMOTE

# Separate features (X) and target (y)
X = data.drop(columns=[target_column])
y = data[target_column]

# Apply SMOTE
smote = SMOTE(sampling_strategy='auto', n_neighbors=22)  # Adjust n_neighbors
X_resampled, y_resampled = smote.fit_resample(X, y)

# Combine resampled features and target
resampled_data = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), 
                            pd.DataFrame(y_resampled, columns=[target_column])], axis=1)

# Save the synthetic dataset to a new CSV file
resampled_data.to_csv('synthetic_data_smote.csv', index=False)
print("Synthetic dataset created and saved as 'synthetic_data_smote.csv'")
