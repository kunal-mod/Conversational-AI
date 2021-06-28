from tkinter import *
from tkinter.font import BOLD
import requests
from gtts import gTTS
import playsound
import random


root = Tk()
root.geometry("400x780")
root.configure(bg='skyblue')
root.resizable(False, False)
root.title("Mental health Bot")

img = PhotoImage(file="health.png")
lblPhoto = Label(root,image=img,bg="skyblue",bd=3)
lblPhoto.pack(pady=2)

frame = Frame(root)
sc = Scrollbar(frame)

sender = "xyz"

def speak(text):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    randfile = "sounds\\"+str(r2)+"randomtext"+str(r1) +".mp3"
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(randfile)
    playsound.playsound(randfile)

bot_message=""
def ask(text_msg):
    bot_message=""
    message=text_msg
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})
    for i in r.json():
        bot_message = i['text']
        chatbox.insert(END,"Bot Says : "+bot_message)
        speak(bot_message)
        
query=""
def ask_bot():
    query = user_input.get()
    chatbox.insert(END,"You Said : " + query)
    user_input.delete(0,END)
    ask(query)    

chatbox = Listbox(frame,width=60,height=18,bg="#f0f8ff")
chatbox.config(yscrollcommand = sc.set)
sc.config(command = chatbox.yview)
sc.pack(side=RIGHT,fill=BOTH)

chatbox.pack(side = LEFT ,fill=BOTH ,pady=8)
frame.pack()

labelText=StringVar()
labelText.set("Your Message : ")
labelDir=Label(root, textvariable=labelText, height=2,font = ("Arial", 15, BOLD),bg ="skyblue")
labelDir.pack(side="top",pady=5)

scrollbar = Scrollbar(root,orient="horizontal")
txt = StringVar()
user_input =Entry(root,xscrollcommand=scrollbar.set,textvariable=txt,font = ("Arial", 15),bg ="#f0f8ff")
user_input.focus()
user_input.pack(side = "top",fill="x")
scrollbar.pack(fill="x")
scrollbar.config(command=user_input.xview)
user_input.config()

imgs = PhotoImage(file=r"play-button.png")
btn = Button(root,image=imgs,bg="skyblue",borderwidth = 0,command = ask_bot,text="Bottom")
btn.pack(pady=10)
root.mainloop()
