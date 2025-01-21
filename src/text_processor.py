class TextProcessor:
    """
    Handles the logic for processing and validating text for emoji translation.
    """

    def __init__(self, llm_client):
        """
        Initialize the TextProcessor with an LLMClient instance.

        :param llm_client: An instance of LLMClient for handling API interactions
        """
        self.llm_client = llm_client

    def process_text(self, input_text: str) -> str:
        """
        Process the input text by sending it to the LLM for translation.

        :param input_text: The text to be translated into emojis
        :return: Translated text containing emojis
        """
        if not input_text.strip():
            raise ValueError("Input text cannot be empty or whitespace.")

        try:
            return self.llm_client.query(input_text)
        except Exception as e:
            raise RuntimeError(f"Error during text processing: {e}")
