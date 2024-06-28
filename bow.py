import json

# Load intents from intents.json
with open('intents.json') as file:
    intents = json.load(file)

# Example function to extract patterns and update BoW
def extract_patterns(intents):
    patterns = []
    for intent in intents['intents']:
        patterns.extend(intent['patterns'])
    return patterns

# Extract patterns from intents
patterns = extract_patterns(intents)

# Create BoW model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

# Get the updated vocabulary
vocab = vectorizer.get_feature_names_out()
print("Updated vocabulary:", vocab)
