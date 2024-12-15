from tkinter import *
import pyttsx3

myframe = Tk()
myframe.geometry("400x300")
myframe.title("Task")

mylabel = Label(myframe, text="Speech to Text", font="Tahoma 30 bold")
mylabel.pack(pady=30)

mylabe2 = Label(myframe, text="Enter your link", font="Courier 30 bold")
mylabe2.pack(pady=10)

mytext = Entry(myframe, width=50)
mytext.pack(pady=10)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)

def voice():
    text = mytext.get()
    engine.say(text)     
    engine.runAndWait()

def delete():
    mytext.delete(0, END)
button1 = Button(myframe,padx=10 ,text="Play", command=voice)
button1.place( rely=0.8,x=100)
button2 = Button(myframe,padx=10,bg="red", text="Exit", command=myframe.destroy)
button2.place( rely=0.8,x=170)
button3 = Button(myframe, padx=10,text="Set", command= delete)
button3.place( rely=0.8,x=240)
myframe.mainloop()