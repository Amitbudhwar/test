def search_text(text, search_query):
    # Convert the text and search query to lowercase for case-insensitive search
    text = text.lower()
    search_query = search_query.lower()

    # Split the text into a list of words
    words = text.split()

    # Search for the search query in the list of words
    results = []
    for i, word in enumerate(words):
        if search_query in word:
            results.append((i, word))

    return results

# Example usage
text = "The quick brown fox jumps over the lazy dog."
search_query = "dog"
print(search_text(text, search_query))