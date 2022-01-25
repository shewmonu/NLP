from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3
import speech_recognition as s
import threading
import spacy

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voices', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")



convo=[
       'hello',
       'hi there !',
       'what is your name ?',
       'My name is Bot , I am created by Shew , Anik , Manoj and Tushar and Souvik',
       'how are you ?',
       'I am doing great these days',
       'thankyou',
       'In which city you live ?',
       'I live in Kolkata',
       'In which language you talk',
       ' I mostly talk in English ',
       'How can I see the academic structure of tpi ?'
       'Sure, if you enter our main website then you show a red square with red straight line besides our college name, you just click or touch the box and then you see that a option of academic, you just click and finally you see academic structure of our college.'
       ]
trainer=ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

#answer = bot.get_response("what is your name?")
#print(answer)

#print("Talk to bot ")
#while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ",answer)
     
main = Tk()

main.geometry("450x650")

main.title("TPI Chat bot")
img = PhotoImage(file="tpi.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)

#takey query : takes audio as input from user and converts it to string.

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)



frame=Frame(main)

sc = Scrollbar(frame)
msgs=Listbox(frame,width=80,height=15, yscrollcommand = sc.set)

sc.pack(side=RIGHT, fill = Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()
sc.config(command=msgs.yview)

# creating text field

textF=Entry(main,font=("Time New Roman", 20))
textF.pack(fill=X,pady=15)

btn=Button(main,text="Ask from bot", font=("Time New Roman", 20),command=ask_from_bot)
btn.pack()

# creating a function
def enter_function(event):
    btn.invoke()
    
#going to binid main window with enter key....

main.bind('<Return>', enter_function)



def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)

t.start()

main.mainloop()
