import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

text = "" # string to bem filled by the file content

with open("text.txt", "r") as opened_file:
    text = opened_file.read()

# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# Convert to lowercase
text = text.lower()

# Tokenize the text
words = text.split()

# Tokenize into sentences
sentences = sent_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('portuguese'))
filtered_words = [word for word in words if word not in stop_words]

# Count the occurrences
word_counts = Counter(filtered_words)

# Sort the words based on frequencies
most_common_words = word_counts.most_common()

# Get the most repeated words (top 5)
top_words = [word for word, count in most_common_words[:5]]

print("Most repeated words:")

for word in top_words:
    print(word)

neighboring_words_counts = Counter()
for word in top_words:
    for sentence in sentences:
        if word in sentence:
            tokens = word_tokenize(sentence)
            index = tokens.index(word)
            for i in range(1, 6):
                if index - i >= 0 and tokens[index - i] not in stop_words:
                    neighboring_words_counts[tokens[index - i]] += 1
                if index + i < len(tokens) and tokens[index + i] not in stop_words:
                    neighboring_words_counts[tokens[index + i]] += 1

# Display the most repeated word and its neighboring words
for word in top_words:
    print(f"Most repeated word: '{word}'")
    print(f"Most frequent neighboring words of '{word}':")
    neighbors = neighboring_words_counts.most_common(6)
    for neighbor, count in neighbors:
        if neighbor != word:
            print(neighbor)
    print()
