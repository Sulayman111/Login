import tkinter
from tkinter import ttk
from tkinter import PhotoImage
import webbrowser

def name():
    entry1 = ent1.get()
    entry2 = ent2.get()
    url = 'https://github.com/' + entry1 + entry2
    webbrowser.open_new_tab(url)

window = tkinter.Tk()
window.title('Email and password')
window.geometry('480x400')
window.resizable(False, False)
window['bg'] = '#696969'

img = tkinter.PhotoImage(file = "./Tkinter/image/github.png")
imgbx = tkinter.Label(image = img)
imgbx.place(x=195, y=15)
imgbx['bg'] = '#696969'

label1 = tkinter.Label(text = "Email: ")
label1.place(x = 100, y = 170)
label1['bg'] = '#696969'
label1['font'] = 'Roboto 10 bold'
ent1 = ttk.Entry(window)
ent1.place(x=170, y=170)

label2 = tkinter.Label(text = "Password: ")
label2.place(x = 100, y = 240)
label2['bg'] = '#696969'
label2['font'] = 'Roboto 10 bold'
ent2 = ttk.Entry(window)
ent2.place(x=170, y=240)

but1 = ttk.Button(text='Login', command=name)
but1.place(x=190, y=300)
window.mainloop()
