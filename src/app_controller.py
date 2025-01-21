from src.main_window import MainWindow
from src.text_processor import TextProcessor
from src.text_validator import TextValidator


class AppController:
    """
    Controller class for managing interactions between the UI and business logic.
    """

    def __init__(self, text_processor: TextProcessor, main_window: MainWindow):
        """
        Initialize the AppController.

        :param text_processor: An instance of TextProcessor for handling text translation
        :param main_window: An instance of MainWindow for handling UI interactions
        """
        self.text_processor = text_processor
        self.main_window = main_window

        # Connect UI events to controller methods
        self.main_window.set_translate_callback(self.translate_text)
        self.main_window.set_clear_callback(self.clear_text)

    def translate_text(self):
        """
        Handle the translation process when triggered by the UI.
        """
        input_text = self.main_window.get_input_text()

        # Validate input text
        if TextValidator.is_empty(input_text):
            self.main_window.show_warning("Input text cannot be empty.")
            return

        max_length = 500  # Example maximum length
        if TextValidator.exceeds_length(input_text, max_length):
            self.main_window.show_warning(f"Input text exceeds the maximum length of {max_length} characters.")
            return

        prohibited_chars = {"@", "#", "$"}
        if TextValidator.contains_prohibited_characters(input_text, prohibited_chars):
            self.main_window.show_warning(f"Input text contains prohibited characters: {prohibited_chars}")
            return

        # Process valid input text
        try:
            translated_text = self.text_processor.process_text(input_text)
            self.main_window.set_output_text(translated_text)
        except Exception as e:
            self.main_window.show_error(f"Failed to translate text: {e}")

    def clear_text(self):
        """
        Clear the input and output text fields in the UI.
        """
        self.main_window.clear_input_text()
        self.main_window.clear_output_text()
