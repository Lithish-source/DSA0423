import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")

# Take the feedback column
feedback = data["feedback"].dropna()

# Basic stop words list
stop_words = {
    "the","and","is","in","to","of","for","on","at","a","an","this","that",
    "it","be","as","are","was","were","by","with","from"
}

words = []

# Text preprocessing
for text in feedback:
    # convert to lowercase
    text = text.lower()
    
    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # split into words
    word_list = text.split()
    
    # remove stop words
    filtered_words = [w for w in word_list if w not in stop_words]
    
    words.extend(filtered_words)

# Calculate frequency distribution
word_freq = Counter(words)

# User input for N
N = int(input("Enter number of top frequent words to display: "))

# Get top N words
top_words = word_freq.most_common(N)

# Display results
print("\nTop", N, "most frequent words:")
for word, freq in top_words:
    print(word, ":", freq)

# Prepare data for plotting
labels = [word for word, freq in top_words]
values = [freq for word, freq in top_words]

# Plot bar graph
plt.bar(labels, values)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top Frequent Words in Customer Feedback")
plt.xticks(rotation=45)
plt.show()