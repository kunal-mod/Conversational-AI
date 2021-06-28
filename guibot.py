from tkinter import *
import speech_recognition as sr 
import requests
import pyttsx3

root = Tk()
root.geometry("400x730")
root.configure(bg='skyblue')
root.resizable(False, False)
root.title("Mental health Bot")

img = PhotoImage(file="health.png")
lblPhoto = Label(root,image=img,bg="skyblue",bd=3)
lblPhoto.pack(pady=2)

frame = Frame(root)
sc = Scrollbar(frame)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
engine.setProperty('rate', 150)


def speak(bot_message):
    engine.say(bot_message)
    engine.runAndWait()

def ask(text_msg):
    bot_message = ""
    while bot_message != "Bye":
        message = text_msg
        print("Sending message now...")
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={ "message": message})
        print("Bot says, ",end=' ')
        for i in r.json():
            bot_message = i['text']
            speak(bot_message)
            print(f"{i['text']}")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak Anything :")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print("You said : {}".format(text))
                except:
                    print("Sorry could not recognize your voice")
            return bot_message


def ask_bot():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Speak Anything :")
        audio = r.listen(source)        
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")
    chatbox.insert(END,"You said : "+text)
    answer = ask(text)
    chatbox.insert(END,"Bot Says : "+answer)



chatbox = Listbox(frame,width=60,height=20,bg="#f0f8ff")
chatbox.config(yscrollcommand = sc.set)
sc.config(command = chatbox.yview)
sc.pack(side=RIGHT,fill=BOTH)

chatbox.pack(side = LEFT ,fill=BOTH ,pady=10)
frame.pack()


imgs = PhotoImage(file=r"buttom-removebg-preview.png")
btn = Button(root,image=imgs,bg="skyblue",command=ask_bot,borderwidth = 0)
btn.pack(pady=10)
root.mainloop()


