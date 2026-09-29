import re
from collections import Counter


class TextProcessor:

    STOP_WORDS = {
        "a", "an", "the", "is", "are", "was", "were",
        "and", "or", "but", "in", "on", "at", "to",
        "of", "for", "with", "this", "that", "it",
        "as", "be", "by", "from", "has", "have"
    }

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

    def remove_stop_words(self, text):
        cleaned_text = self.clean_text(text)

        words = cleaned_text.split()

        meaningful_words = [
            word for word in words
            if word not in self.STOP_WORDS
        ]

        return meaningful_words

    def most_common_words(self, text, limit=5):
        meaningful_words = self.remove_stop_words(text)

        word_frequency = Counter(meaningful_words)

        return word_frequency.most_common(limit)