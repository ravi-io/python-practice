from collections import Counter

# sentence = "Hello, my name is Ravi Karmakar. I am a software engineer and I love coding."

# words = sentence.split()

# count = Counter(words)
# print(count)

marks = [85, 90, 78, 92, 88, 95, 85, 75, 89, 91]
count = Counter(marks)
print(count.most_common(1))  # Get the three most common marks