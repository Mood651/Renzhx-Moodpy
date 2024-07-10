import tkinter as tk
from tkinter import scrolledtext
import subprocess

class PythonEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.run_button = tk.Button(self, text="运行", command=self.run_code)
        self.run_button.pack(side=tk.BOTTOM)

        self.output_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=80, height=10)
        self.output_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def run_code(self):
        code = self.text_area.get("1.0", tk.END)
        try:
            result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
            output = result.stdout
            error = result.stderr
            if error:
                self.output_area.delete("1.0", tk.END)
                self.output_area.insert(tk.END, f"错误: {error}")
            else:
                self.output_area.delete("1.0", tk.END)
                self.output_area.insert(tk.END, output)
        except Exception as e:
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, f"运行时错误: {e}")

root = tk.Tk()
root.title("Renzhx Moodpy V0.0.5")
app = PythonEditor(master=root)
app.pack()
root.mainloop()