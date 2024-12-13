spanish_dict = {
    "hola": "hello",
    "adiós": "goodbye",
    "gracias": "thank you",
    "por favor": "please",
    "sí": "yes",
    "no": "no",
    "buenos días": "good morning",
    "buenas noches": "good night",
    "amigo": "friend",
    "familia": "family"}

from tkinter import Tk, Entry, Button, Label, StringVar
window = Tk()
window.geometry('600x250')
window.title(spanish_dict)

entry_text = Entry(window)
entry_text.pack()


result = StringVar()
result_label = Lbel(window, textvarlabel=result)
result_label.pack()


def search(word):
    if word in spanish_dict:
        result.set(spanish_dict[word])
        print(spanish_dict[word])
    else:
        result.set("Not Found")

search_btn = Button(window, text="Search", command=Lambda: search(entry_text.get())
search_btn.pack()
window.mainloop()



