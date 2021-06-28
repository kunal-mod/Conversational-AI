from gtts import gTTS
import os
import playsound
import pyttsx3

mytext = 'Welcome to geeksforgeeks!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("sounds\\welcome.mp3")
playsound.playsound("sounds\\welcome.mp3")

mytext = 'yoyoyoyoy!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("sounds\\elcome.mp3")
playsound.playsound("sounds\\elcome.mp3")

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# # print(voices[1].id)
# engine.setProperty('rate', 120)
# engine.say("Welcome to geeksforgeeks")
# engine.runAndWait()