import tkinter as tk
from tkinter import messagebox

class EmojiTranslatorApp:
    """
    Простое приложение для перевода текста в эмодзи.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Emoji Translator")
        self.root.geometry("400x300")

        # Поле ввода текста
        self.input_label = tk.Label(root, text="Введите текст:")
        self.input_label.pack(pady=5)

        self.input_text = tk.Text(root, height=5, width=40)
        self.input_text.pack(pady=5)

        # Кнопка перевода
        self.translate_button = tk.Button(root, text="Перевести", command=self.translate_text)
        self.translate_button.pack(pady=10)

        # Поле вывода текста
        self.output_label = tk.Label(root, text="Переведенный текст:")
        self.output_label.pack(pady=5)

        self.output_text = tk.Text(root, height=5, width=40, state="disabled")
        self.output_text.pack(pady=5)

        # Кнопка очистки
        self.clear_button = tk.Button(root, text="Очистить", command=self.clear_text)
        self.clear_button.pack(pady=10)

    def translate_text(self):
        """
        Перевод текста в эмодзи (упрощенная заглушка).
        """
        input_text = self.input_text.get("1.0", tk.END).strip()

        if not input_text:
            messagebox.showwarning("Предупреждение", "Введите текст для перевода.")
            return

        emoji_dict = {
    # Английский
    "love": "❤️",
    "pizza": "🍕",
    "cat": "🐱",
    "happy": "😊",
    "dog": "🐶",

    # Русский
    "любовь": "❤️",
    "пицца": "🍕",
    "кот": "🐱",
    "кошка": "🐱",
    "собака": "🐶",
    "радость": "😊",
    "улыбка": "😊",
    "смех": "😂",
    "грусть": "😢",
    "злость": "😡",
    "удивление": "😲",
    "поцелуй": "😘",
    "сердце": "❤️",
    "звезда": "⭐",
    "огонь": "🔥",
    "вода": "💧",
    "дерево": "🌳",
    "цветок": "🌸",
    "солнце": "☀️",
    "луна": "🌙",
    "еда": "🍴",
    "яблоко": "🍎",
    "банан": "🍌",
    "виноград": "🍇",
    "машина": "🚗",
    "самолет": "✈️",
    "поезд": "🚆",
    "дом": "🏠",
    "работа": "💼",
    "школа": "🏫",
    "спорт": "⚽",
    "музыка": "🎵",
    "танец": "💃",
    "книга": "📖",
    "компьютер": "💻",
    "игра": "🎮",
    "деньги": "💰",
    "подарок": "🎁",
    "часы": "⌚",
    "друзья": "👫",
    "семья": "👪"
}


        translated_text = " ".join(emoji_dict.get(word, word) for word in input_text.split())

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, translated_text)
        self.output_text.config(state="disabled")

    def clear_text(self):
        """
        Очищает поля ввода и вывода текста.
        """
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmojiTranslatorApp(root)
    root.mainloop()
