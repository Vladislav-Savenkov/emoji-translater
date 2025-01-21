class TextValidator:
    """
    Utility class for validating input text for the Emoji Translator.
    """

    @staticmethod
    def is_empty(text: str) -> bool:
        """
        Check if the given text is empty or contains only whitespace.

        :param text: The text to validate
        :return: True if the text is empty or whitespace, False otherwise
        """
        return not text.strip()

    @staticmethod
    def exceeds_length(text: str, max_length: int) -> bool:
        """
        Check if the text exceeds the specified maximum length.

        :param text: The text to validate
        :param max_length: The maximum allowable length
        :return: True if the text exceeds the maximum length, False otherwise
        """
        return len(text) > max_length

    @staticmethod
    def contains_prohibited_characters(text: str, prohibited_chars: set) -> bool:
        """
        Check if the text contains any prohibited characters.

        :param text: The text to validate
        :param prohibited_chars: A set of prohibited characters
        :return: True if the text contains any prohibited characters, False otherwise
        """
        return any(char in prohibited_chars for char in text)
