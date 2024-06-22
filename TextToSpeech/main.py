import os
import tkinter as tk
from tkinter import *

from gtts import gTTS
from playsound import playsound
import datetime
import random

#Window Initialisation
window = Tk()
window.resizable(width=False, height=False)
window.geometry('1000x500')
window.configure(bg='Lavender')
window.title("Text To Speech")

# Load the icon from the ICO file
icon = tk.PhotoImage(file="image/texttospeech.png")
# Set the window icon
window.iconphoto(True, icon)

Label(window,text="Welcome to Text-To-Speech Application" , font='arial 20 bold' ,bg='Lavender').pack()
Label(window,text='Made by Brice Roméo',font="arial 15" , bg='Lavender' ,width='20').pack(side='bottom')

msg = StringVar()
Label(window , text="What do you want to translate" , font='bodoni 20 bold' , bg='Lavender').pack()

entry = tk.Entry(
    window,
    textvariable=msg,
    width=50,
    font=("Arial", 12, "bold"),
    bg="white",
    fg="black",
    relief="groove",
    highlightthickness=2,
    highlightcolor="black",
)
entry.place(x=270 , y=100)

#Text to speech
def texttospeech():
    message = entry.get()
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"texttospeech_{timestamp}_{random.randint(1, 1000)}.mp3"
    speech = language(msg.get())
    speech.save(filename)
    playsound(filename)
    # Delete the generated MP3 file
    if os.path.exists(filename):
        os.remove(filename)

def destroy():
    window.destroy()

def reset():
    msg.set("")

#Choose the language french , english , spanish
def language(msg):
    if lang == 'fr-FR':
        return gTTS(text=msg, lang='fr-FR')
    elif lang == 'en-US':
        return gTTS(text=msg, lang='en-US')
    elif lang == 'es':
        return gTTS(text=msg, lang='es')
    else:
        return gTTS(text=msg, lang='en-US')

def choose_lang(lang):
    Button(window, text="French", font='arial 10 bold',  command=lambda: on_language_clicked('fr-FR'), bg='blue', width='7', fg='white', relief="flat").place(x=350, y=175)
    Button(window, text="English", font='arial 10 bold', command=lambda: on_language_clicked('en-US'), bg='indigo', width='7', fg='white', relief="flat").place(x=450, y=175)
    Button(window, text="Spanish", font='arial 10 bold', command=lambda: on_language_clicked('es'), bg='orange', width='7', fg='white', relief="flat").place(x=550, y=175)

def on_language_clicked(language):
    global lang
    lang = language
    choose_lang(lang)
#Command displaying in the window
choose_lang('en-US')

Button(window , text="Play" , font='arial 10 bold' , command=texttospeech , bg='green' , width='7' , fg='white' , relief="flat").place(x=350 , y=250)
Button(window , text='Reset' , font='arial 10 bold' , command=reset , width='7' , bg='Tomato').place(x=450 , y=250)
Button(window , text='Exit' , font='arial 10 bold' , command=destroy , width='7' , bg='Red').place(x=550 , y=250)

window.mainloop()
