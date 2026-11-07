words = ["mango", "Dog", "apple", "sparrow", "fish", "chilly"]

grouped_words = {}

for word in words:

    first_letter = word[0]

    grouped_words.setdefault(first_letter, []).append(word)

print("Grouped Words:")
print(grouped_words)