import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary mapping topics to advice or dynamic response logic
TOPICS = {
    "Advice on not knowing what to do": (
        "1. Pause and step back: Overthinking breeds paralysis.\n"
        "2. Pick the smallest possible action: Break tasks down until the next step takes under 2 minutes.\n"
        "3. Focus on process, not outcome: Curiosity over perfection."
    ),
    "Advice on removing superstition": (
        "1. Examine the logic: Trace the cause-and-effect chain critically.\n"
        "2. Track actual occurrences: Keep a log to see if the outcome correlates with the action.\n"
        "3. Test small exposures: Intentionally break a minor superstition and observe that no negative outcome occurs."
    ),
    # Add new topics here as key-value pairs in the future
}


def show_advice(event=None):
    selected_topic = topic_combo.get()
    advice = TOPICS.get(selected_topic, "Please select a valid topic.")

    # Display in text window
    text_display.config(state=tk.NORMAL)
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, advice)
    text_display.config(state=tk.DISABLED)


# Initialize GUI Window
root = tk.Tk()
root.title("Startup Assistant")
root.geometry("500x350")
root.attributes('-topmost', True)  # Keeps window on top at startup

# UI Elements
label = tk.Label(root, text="Select a topic to get guidance:", font=("Arial", 11, "bold"))
label.pack(pady=10)

topic_combo = ttk.Combobox(root, values=list(TOPICS.keys()), state="readonly", width=40)
topic_combo.pack(pady=5)
topic_combo.bind("<<ComboboxSelected>>", show_advice)

text_display = tk.Text(root, wrap=tk.WORD, height=10, width=55, font=("Arial", 10))
text_display.pack(pady=10)
text_display.config(state=tk.DISABLED)

root.mainloop()