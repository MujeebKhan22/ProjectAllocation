from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example data
students = ["Python, Machine Learning", "Web Development, JavaScript"]
projects = ["AI Project with Python", "Frontend Project with JavaScript"]

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
student_vectors = vectorizer.fit_transform(students)
project_vectors = vectorizer.transform(projects)

# Calculate cosine similarity
similarity_matrix = cosine_similarity(student_vectors, project_vectors)

# Output matches
for i, student in enumerate(students):
    print(f"Matches for student {i}: {similarity_matrix[i]}")