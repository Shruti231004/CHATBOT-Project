import json
from collections import defaultdict

# Load the data from the provided file
file_path = 'scraped_website_data (1).jsonl'

# Read the JSONL file
data = []
with open(file_path, 'r') as file:
    for line in file:
        data.append(json.loads(line))

# Organize data for quick access
data_dict = defaultdict(list)
for entry in data:
    url = entry.get('url')
    content_type = entry.get('type')
    text = entry.get('text')
    data_dict[url].append({'type': content_type, 'text': text})

def search_data(query, data_dict):
    """
    Search for the query in the data dictionary and return relevant entries.
    """
    results = []
    query_lower = query.lower()
    
    for url, entries in data_dict.items():
        for entry in entries:
            if query_lower in entry['text'].lower():
                results.append({'url': url, 'type': entry['type'], 'text': entry['text']})
    
    return results

def chatbot():
    print("Hello! I am your assistant. How can I help you today?")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Search the data for the user's query
        results = search_data(user_input, data_dict)
        
        if results:
            print("\nChatbot: I found the following information for you:")
            for result in results:
                print(f"- {result['type'].capitalize()}: {result['text']} (URL: {result['url']})")
        else:
            print("\nChatbot: Sorry, I couldn't find any information related to your query.")
            
# Run the chatbot
chatbot()
