from collections import Counter

# List of products sold during the year
products = [
    "Laptop", "Phone", "Laptop", "Tablet", "Phone",
    "Laptop", "Headphones", "Phone", "Tablet", "Laptop"
]

# Calculate frequency distribution
frequency = Counter(products)

print("Frequency Distribution of Products:")
for product, count in frequency.items():
    print(product, ":", count)

# Find most popular product
most_popular = frequency.most_common(1)

print("\nMost Popular Product:")
print(most_popular[0][0], "sold", most_popular[0][1], "times")