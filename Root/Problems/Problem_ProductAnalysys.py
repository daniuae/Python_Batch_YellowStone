# ==========================================
# Word Frequency Counter using OOP
# ==========================================
import re


class WordFrequencyCounter:
    """
    A class to analyze word frequencies in a sentence.
    """

    # ------------------------------------------
    # 1. Clean and Tokenize Input
    # ------------------------------------------
    def preprocess_text(self, text: str) -> list:
        """
        Converts text to lowercase,
        removes punctuation,
        and splits into words.
        """

        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)

        # Tokenize words
        words = text.split()

        return words

    # ------------------------------------------
    # 2. Compute Word Frequency
    # ------------------------------------------
    def compute_word_frequency(self, words: list) -> dict:
        """
        Counts occurrences of each word.
        """

        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        return frequency

    # ------------------------------------------
    # 3. Get Most Frequent Word
    # ------------------------------------------
    def get_most_frequent_word(self, freq_dict: dict) -> tuple:
        """
        Returns the most frequent word and count.
        """

        if not freq_dict:
            return None

        return max(freq_dict.items(), key=lambda x: x[1])

    # ------------------------------------------
    # 4. Filter Words by Minimum Frequency
    # ------------------------------------------
    def filter_words_by_frequency(self, freq_dict: dict, n: int) -> dict:
        """
        Returns words appearing at least n times.
        """

        filtered_words = {}

        for word, count in freq_dict.items():
            if count >= n:
                filtered_words[word] = count

        return filtered_words


# ==========================================
# Main Program
# ==========================================

# Create object
counter = WordFrequencyCounter()

# Input sentence
sentence = """
Hello, hello! How are you?
I am fine. Hello Python!
Python is great and Python is powerful.
"""

# Step 1: Preprocess text
words = counter.preprocess_text(sentence)
print("Tokenized Words:")
print(words)

# Step 2: Compute frequency
frequency_dict = counter.compute_word_frequency(words)
print("\nWord Frequencies:")
print(frequency_dict)

# Step 3: Most frequent word
most_frequent = counter.get_most_frequent_word(frequency_dict)
print("\nMost Frequent Word:")
print(most_frequent)

# Step 4: Filter words with frequency >= 2
filtered_words = counter.filter_words_by_frequency(
    frequency_dict,
    2
)

print("\nWords Appearing At Least 2 Times:")
print(filtered_words)
