from src.llm_client import LLMClient
from src.text_processor import TextProcessor
from src.main_window import MainWindow
from src.app_controller import AppController
import tkinter as tk

def main():
    # Step 1: Initialize LLM client
    llm_client = LLMClient()

    # Step 2: Create the business logic layer
    text_processor = TextProcessor(llm_client)

    # Step 3: Set up the UI
    root = tk.Tk()
    main_window = MainWindow(root)

    # Step 4: Connect the UI and logic with the controller
    app_controller = AppController(text_processor, main_window)

    # Step 5: Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
