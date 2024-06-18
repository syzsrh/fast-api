import openai
from constants import API_KEY

openai.api_key = API_KEY

def embed_text(text, model="text-embedding-3-small"):
    """Generate an embedding for a given piece of text using a specified embedding model.

    Args:
        text (str): The text to be embedded. The function removes any extra spaces before processing.
        model (str, optional): The name of the embedding model to use. Defaults to "text-embedding-3-small".

    Returns:
        list: A list representing the embedding of the input text.
    """
    
    text = text.strip()
    print(text)
    return openai.embeddings.create(input = [text], model=model).data[0].embedding
