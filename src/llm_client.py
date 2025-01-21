import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LLMClient:
    """
    A client for interacting with the Mistral LLM API to translate text into emojis.
    """

    def __init__(self, api_url: str = None, api_key: str = None):
        """
        Initialize the client.

        :param api_url: The API endpoint URL (default loaded from environment variables)
        :param api_key: The API key for authentication (default loaded from environment variables)
        """
        self.api_url = api_url or os.getenv("LLM_API_URL")
        self.api_key = api_key or os.getenv("LLM_API_KEY")

        if not self.api_url or not self.api_key:
            raise ValueError("API URL and API Key must be provided.")

    def query(self, text: str) -> str:
        """
        Sends a request to Mistral to translate the text into emojis.

        :param text: The text to be translated
        :return: The text translated into emojis
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty or whitespace.")

        # Prepare request payload
        payload = {
            "model": "open-mistral-nemo",
            "temperature": 0.6,
            "top_p": 1,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "I'll give you a text as input. \n\n"
                        "Imagine that you are a translator from human to emoji.\n\n"
                        "Your task is to translate this text into emoji.\n"
                        "The more words of the input text will be replaced by a separate emoji, the better. \n"
                        "It should be possible to understand the original meaning of the input text only using the specified emoji. \n"
                        "Conclusion: only emoji without any text.\n\n"
                        "Example:\n"
                        "Input: 'I love cats, dogs and pizza'\n"
                        "Output: '🙋‍♂️❤️🐈🐶🍕'"
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            "response_format": {
                "type": "text"
            },
            "n": 1
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()  # Check for HTTP errors
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to Mistral API: {e}")

        # Process the response
        try:
            result = response.json()
            translated_text = result["choices"][0]["message"]["content"]
            if not translated_text:
                raise ValueError("Response from LLM does not contain 'translated_text'.")
            return translated_text
        except (ValueError, KeyError) as e:
            raise ValueError(f"Failed to parse response from LLM: {e}")

# Example usage
if __name__ == "__main__":
    client = LLMClient()
    input_text = "I love pizza and dogs"

    try:
        emoji_translation = client.query(input_text)
        print("Original Text:", input_text)
        print("Emoji Translation:", emoji_translation)
    except Exception as e:
        print(f"Error: {e}")
