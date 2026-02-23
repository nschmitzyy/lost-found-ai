import re

STOPWORDS = ["the", "a", "an", "and", "is", "in", "at", "on"]

def clean_text(text):
    words = re.findall(r'\w+', text.lower())
    return [w for w in words if w not in STOPWORDS]

def keyword_similarity(text1, text2):
    words1 = set(clean_text(text1))
    words2 = set(clean_text(text2))

    if not words1 or not words2:
        return 0

    overlap = len(words1.intersection(words2))
    return overlap / max(len(words1), len(words2))

def calculate_match(ai_confidence, desc1, desc2):
    keyword_score = keyword_similarity(desc1, desc2)
    return (0.6 * ai_confidence) + (0.4 * keyword_score)
