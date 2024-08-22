import tkinter as tk
from tkinter import scrolledtext
import nltk
from transformers import pipeline

# 下载nltk数据（如果尚未下载）
nltk.download('punkt')

# 使用transformers库中的预训练模型
chatbot = pipeline("conversational")

class ChatInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI 对话界面")
        self.geometry("600x400")
        
        self.chat_window = scrolledtext.ScrolledText(self, wrap=tk.WORD, state='disabled')
        self.chat_window.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.input_field = tk.Entry(self.input_frame)
        self.input_field.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        self.send_button = tk.Button(self.input_frame, text="发送", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
        
    def send_message(self):
        user_input = self.input_field.get()
        if user_input:
            self.display_message("你: " + user_input)
            response = chatbot(user_input)
            self.display_message("AI: " + response.get('response', '对不起，我不明白你的意思。'))
            self.input_field.delete(0, tk.END)
    
    def display_message(self, message):
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, message + "\n")
        self.chat_window.config(state='disabled')
        self.chat_window.yview(tk.END)

if __name__ == "__main__":
    app = ChatInterface()
    app.mainloop()
