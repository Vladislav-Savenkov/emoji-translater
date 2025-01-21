import tkinter as tk
from tkinter import messagebox, font

class MainWindow:
    """
    Main application window for the Emoji Translator.
    """

    def __init__(self, root):
        """
        Initialize the main window.

        :param root: Tkinter root window
        """
        self.root = root
        self.root.title("Emoji Translator")
        self.root.geometry("500x500")
        
        # Initialize the custom font for emojis
        self.emoji_font = font.Font(family="Noto Color Emoji ")

        self.create_widgets()

    def create_widgets(self):
        """
        Create and layout all widgets in the main window.
        """
        # Input label and text box
        self.input_label = tk.Label(self.root, text="Enter text to translate:")
        self.input_label.pack(pady=10)

        self.input_text = tk.Text(self.root, height=5, width=50)
        self.input_text.pack(pady=10)

        # Buttons
        self.translate_button = tk.Button(self.root, text="Translate")
        self.translate_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear")
        self.clear_button.pack(pady=5)

        # Output label and text box
        self.output_label = tk.Label(self.root, text="Translated text (emojis):")
        self.output_label.pack(pady=10)

        # Output text box (using the Apple Color Emoji font)
        self.output_text = tk.Text(self.root, height=5, width=50, font=self.emoji_font, state=tk.DISABLED)
        self.output_text.pack(pady=10)
        
    def set_translate_callback(self, callback):
        """
        Set the callback for the Translate button.

        :param callback: Function to be called when the Translate button is clicked
        """
        self.translate_button.config(command=callback)

    def set_clear_callback(self, callback):
        """
        Set the callback for the Clear button.

        :param callback: Function to be called when the Clear button is clicked
        """
        self.clear_button.config(command=callback)

    def get_input_text(self):
        """
        Retrieve the text from the input field.

        :return: Input text
        """
        return self.input_text.get("1.0", tk.END).strip()

    def set_output_text(self, text):
        """
        Display the translated text in the output field.

        :param text: Translated text to display
        """
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", text)
        self.output_text.configure(state=tk.DISABLED)

    def clear_input_text(self):
        """
        Clear the input text field.
        """
        self.input_text.delete("1.0", tk.END)

    def clear_output_text(self):
        """
        Clear the output text field.
        """
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.configure(state=tk.DISABLED)

    def show_warning(self, message):
        """
        Display a warning message.

        :param message: Warning message to display
        """
        messagebox.showwarning("Warning", message)

    def show_error(self, message):
        """
        Display an error message.

        :param message: Error message to display
        """
        messagebox.showerror("Error", message)
