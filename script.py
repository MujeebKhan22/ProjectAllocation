import pandas as pd
import numpy as np

# Random seed for reproducibility
np.random.seed(42)

# Define number of records
num_students = 5000
num_projects = 500

# Create synthetic student data
student_data = {
    'Student ID': range(1001, 1001 + num_students),
    'Name': [f'Student_{i}' for i in range(1, num_students + 1)],
    'Performance (AI)': np.random.randint(50, 100, num_students),
    'Performance (Web Dev)': np.random.randint(50, 100, num_students),
    'Performance (Networking)': np.random.randint(50, 100, num_students),
    'Interest 1': np.random.choice(['AI', 'Web Dev', 'Networking', 'IoT', 'Data Science'], num_students),
    'Interest 2': np.random.choice(['AI', 'Web Dev', 'Networking', 'IoT', 'Data Science'], num_students),
    'Interest 3': np.random.choice(['AI', 'Web Dev', 'Networking', 'IoT', 'Data Science'], num_students),
    'Overall Rating (0-100)': np.random.randint(60, 100, num_students)
}

students_df = pd.DataFrame(student_data)

# Create synthetic project data
project_data = {
    'Project ID': range(2001, 2001 + num_projects),
    'Project Title': [f'Project_{i}' for i in range(1, num_projects + 1)],
    'Domain': np.random.choice(['AI', 'Web Dev', 'Networking', 'IoT', 'Data Science'], num_projects),
    'Minimum Performance Requirement': np.random.randint(65, 90, num_projects),
    'Project Rating (1-5)': np.random.randint(1, 6, num_projects)
}

projects_df = pd.DataFrame(project_data)

# Save data to CSV files
students_df.to_csv('students_data.csv', index=False)
projects_df.to_csv('projects_data.csv', index=False)

print("Dataset created successfully!")
