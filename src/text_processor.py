import re
from collections import Counter


class TextProcessor:

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def word_count(self, text):
        cleaned_text = self.clean_text(text)

        if not cleaned_text:
            return 0

        return len(cleaned_text.split())

    def character_count(self, text):
        return len(text)

    def most_common_words(self, text, limit=5):
        cleaned_text = self.clean_text(text)

        words = cleaned_text.split()

        word_frequency = Counter(words)

        return word_frequency.most_common(limit)