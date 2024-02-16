import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style, ttk

# Morse Code Dictionary
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                   '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                   '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
                   }

# Reverse Morse Code Dictionary
reversed_morse_code_dict = {value: key for (key, value) in morse_code_dict.items()}

# Function to show 'text to morse' translation screen
def show_text_to_morse():
    home_frame.pack_forget()
    translation_frame.pack()
    translation_label.config(text="Input Text:")
    translation_button.config(text="Translate to morse")
    translation_button.config(command=text_to_morse)

def show_morse_to_text():
    home_frame.pack_forget()
    translation_frame.pack()
    translation_label.config(text="Input Text:")
    translation_button.config(text="Translate to text")
    translation_button.config(command=morse_to_text)


# Function to show home screen
def show_home_screen():
    translation_frame.pack_forget()
    home_frame.pack()
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

#Function to translate text to morse code
def text_to_morse():
    text = input_text.get("1.0", "end").strip().upper()
    # Validate if textbox is not empty
    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text.")
        return
    # Validate if user entered text, not morse code.
    for char in text:
        if char in morse_code_dict.values():
            messagebox.showwarning(
                "Invalid Input", "Cannot put morse code in this option.")
            return

    morse_code = ""
    for char in text:
        if char in morse_code_dict:
            morse_code = morse_code + morse_code_dict[char] + " "
        else:
            morse_code = morse_code + char
    output_text.delete("1.0", "end")
    output_text.insert("1.0", morse_code)
    print(morse_code)

# Function to translate Morse Code to Text
def morse_to_text():
    morse_code = input_text.get("1.0", "end").strip().split()
    # Validate if textbox is not empty
    if not morse_code:
        messagebox.showwarning("Invalid Input", "Please enter morse code.")
        return
    # Validate if user input is morse, not text.
    for code in morse_code:
        if code.isalpha() | code.isnumeric(): #reversed_morse_code_dict.values(): #The isalpha() method returns True if all the characters are alphabet letters (a-z).
            messagebox.showwarning("Invalid Input", "Cannot put text or number in this option.")
            return
    text = ""
    for code in morse_code:
        if code in reversed_morse_code_dict:
            text = text + reversed_morse_code_dict[code] + " "
        else:
            text = text + reversed_morse_code_dict[code]
    output_text.delete("1.0", "end")
    output_text.insert("1.0", text)
    print(text)

def clear_text():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    show_home_screen()

# Create the main window
window = tk.Tk()
window.title("Morse code translator")
window.geometry("500x500")
style = Style(theme="flatly")

home_label = ttk.Label(window, text="Select Translation Type:",
                       font=('tk.DefaultFont', 20))
home_label.pack(pady=10)

# Create home screen
home_frame = ttk.Frame(window, padding="20")
home_frame.pack()


# Text to Morse Code button
text_to_morse_button = ttk.Button(home_frame, text="Text to Morse Code",
                                       command=show_text_to_morse)
text_to_morse_button.pack(pady=5)

# Morse to Text button
morse_to_text_button = ttk.Button(home_frame, text="Morse to Text",
                                  command=show_morse_to_text)
morse_to_text_button.pack(pady=5)

# Create translation screen
translation_frame = ttk.Frame(window, padding="20")

# Create label for input text
translation_label = ttk.Label(translation_frame, text="Input text:",
                              font=("tk.DefaultFont", 20))
translation_label.pack(pady=10)

# Create input text field
input_text = tk.Text(translation_frame, height=5)
input_text.pack()

# Create label for output text
output_text_label = tk.Label(translation_frame, text="Output text:",
                            font=("tk.DefaultFont", 20))
output_text_label.pack(pady=5)

# Crate output text field
output_text = tk.Text(translation_frame, height=5)
output_text.pack()

# Create translation button
translation_button = ttk.Button(translation_frame, text="Translate",command=None)
translation_button.pack(pady=15)

# Create back button to home screen
back_button = ttk.Button(translation_frame, text="Back", command=show_home_screen)
back_button.pack(pady=5)

# Hide translation screen initially
translation_frame.pack_forget()

window.mainloop()