import tkinter as tk

# Funciones para traducir de texto a código Morse y viceversa
def text_to_morse():
    text = text_entry.get()
    morse_output.config(text=text_to_morse_text(text))

def morse_to_text():
    morse = morse_entry.get()
    text_output.config(text=morse_to_text_text(morse))

def text_to_morse_text(text):
    morse_code = ""
    for char in text:
        if char.lower() in morse_code_dict:
            morse_code += morse_code_dict[char.lower()] + " "
    return morse_code

def morse_to_text_text(morse_code):
    text = ""
    morse_code = morse_code.split(" ")
    for code in morse_code:
        for letter, morse in morse_code_dict.items():
            if code == morse:
                text += letter
                break
    return text

# Definir el diccionario Morse
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}

# Crear la ventana principal
root = tk.Tk()
root.title("Traductor Morse")

# Crear etiquetas y campos de entrada
text_label = tk.Label(root, text="Texto:")
text_label.pack()
text_entry = tk.Entry(root)
text_entry.pack()
text_to_morse_button = tk.Button(root, text="Texto a Morse", command=text_to_morse)
text_to_morse_button.pack()

morse_label = tk.Label(root, text="Código Morse:")
morse_label.pack()
morse_entry = tk.Entry(root)
morse_entry.pack()
morse_to_text_button = tk.Button(root, text="Morse a Texto", command=morse_to_text)
morse_to_text_button.pack()

# Crear etiquetas para mostrar los resultados
morse_output = tk.Label(root, text="", wraplength=300)
morse_output.pack()
text_output = tk.Label(root, text="", wraplength=300)
text_output.pack()

# Ejecutar la ventana
root.mainloop()
