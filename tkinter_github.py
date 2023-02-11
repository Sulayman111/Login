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
window.title('Login')
window.geometry('411x508')
window.resizable(False, False)
window['bg'] = '#1F1F1F'

frame = tkinter.Frame(window, width=360, height=460, bg="White")
frame.place(x=25, y=23)
frame['bg'] = '#3B3B3B'

show_code = '😀'
hide_code = '😄'

def show_hide_code():
    if ent2['show'] == '●':
        ent2.configure(show='')
        but2.configure(text=show_code, bg='green')
    else:
        ent2.configure(show='●')
        but2.configure(text=hide_code)

img = tkinter.PhotoImage(file = "./Tkinter/image/github.png")
imgbx = tkinter.Label(image = img)
imgbx.place(x=165, y=45)
imgbx['bg'] = '#3B3B3B'

label1 = tkinter.Label(frame,text = "Username / email: ")
label1.place(x = 20, y = 160)
label1.config(background='#3B3B3B', foreground='white')
label1['font'] = 'NORMAL 12'
ent1 = ttk.Entry(frame, font='Roboto 12')
ent1.place(x=40, y=185, width=280)
ent1.focus()

label2 = tkinter.Label(frame, text = "Password: ")
label2.place(x = 20, y = 245)
label2.config(background='#3B3B3B', foreground='white')
label2['font'] = 'NORMAL 12'
ent2 = ttk.Entry(frame, show="●", font='Roboto 12')
ent2.place(x=40, y=270, width=280)

but1 = tkinter.Button(frame, text='Login', command=name)
but1.place(x=120, y=330, width=120)
but1.config(background='green', foreground='white')

but2 = tkinter.Button(frame, text=hide_code, command=show_hide_code)
but2.place(x=325, y=270, width=20, height=23)
but2['bg'] = 'red'

window.mainloop()
