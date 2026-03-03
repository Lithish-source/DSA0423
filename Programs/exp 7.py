import numpy as np

student_scores = np.array([
    [85, 78, 90, 88],
    [92, 81, 76, 95],
    [75, 85, 89, 80],
    [88, 79, 84, 91]
])

subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

print("Average score for each subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", average_scores[i])

highest_avg_index = np.argmax(average_scores)

print("\nSubject with highest average score:")
print(subjects[highest_avg_index])