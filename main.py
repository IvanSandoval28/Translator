from tkinter import *
import translator

with open('languages.txt', 'r') as file:
    content = file.read()
def translate_text():
    language1 = tkvarq.get()
    language2 = tkvarq2.get()
    text = e.get()
    translated_text = translator.translate(language1, language2, text)
    f.delete(0, END)
    f.insert(0, str(translated_text))
languages = content.split('","')
languages[0] = languages[0][1:]
languages[-1] = languages[-1].rstrip('"')
content = None
root = Tk()
tkvarq = StringVar(root)
tkvarq.set(languages[0])
tkvarq2 = StringVar(root)
tkvarq2.set(languages[0])
myLabel1 = Label(root, text="Please select your language:").grid(column=0, row=0)
option_menu = OptionMenu(root, tkvarq, *languages).grid(column=0, row=1)
e = Entry(root, width=50)
e.grid(column=0, row=2)
myLabel2 = Label(root, text="Please select translated language:").grid(column=0, row=3)
option_menu2 = OptionMenu(root, tkvarq2, *languages).grid(column=0, row=4)
f = Entry(root, width=50)
f.grid(column=0, row=5)
myButton1 = Button(root, text="Translate", command=translate_text).grid(column=0, row=6)

root.mainloop()
