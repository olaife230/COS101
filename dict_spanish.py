from tkinter import Tk, Entry, Button, Label, StringVar

spanish_dict = {
    "hola": "hello",
    "adios": "goodbye",
    "gracias": "thank you",
    "por favor": "please",
    "si": "yes",
    "no": "no",
    "buenos dias": "good morning",
    "buenas noches": "good night",
    "amigo": "friend",
    "familia": "family",
    "comida": "food",
    "agua": "water",
    "escuela": "school",
    "libro": "book",
    "casa": "house",
    "feliz": "happy",
    "triste": "sad",
    "trabajo": "work",
    "tiempo": "time",
    "musica": "music"
}

window = Tk()
window.geometry('600x250')
window.title("Spanish Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

def search(word):
    if word in spanish_dict:
        result.set(spanish_dict[word])
        print(spanish_dict[word])
    else:
        result.set("Not Found")

search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()

