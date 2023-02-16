import tkinter
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import pyjokes
from command_dict import command_dict


machine = pyttsx3.init()
voices = machine.getProperty('voices')
listener = sr.Recognizer()
machine.setProperty('voice', voices[2].id)

def talk(text):
    machine.say(text)
    machine.runAndWait()

def clear_command():
    commander.delete(0, len(commander.get()))

def command_receiver():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'roboman' in command:
                command = command.replace('roboman', '')
                print(command)
        return command
    except:
        return "Nothing"


def run_roboman(text_command=None):
    if text_command == None:
        command = command_receiver()
    else:
        command = text_command
    print(command)
    command = command.lower()
##    command_split = command.split()
##    command_split = set(command_split)
    for i in command_dict:
        if i in command:
            talk(command_dict[i])
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('No, i have a lifelong partner and his name is Internet')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please ask something')

def say_command():
##    machine.say(commander.get())
##    machine.runAndWait()
    result = run_roboman(commander.get())
    talk(result)


win = tkinter.Tk()
win.geometry("265x200")
win.title("Roboman_Chatbot")
win.configure(bg="white")
tkinter.Label(win, text="Roboman_Chatbot", bg="white", font=("Terminal", 10)).pack()
tkinter.Label(win, text="Developed by - Akhil Jose C", bg="white", font=("Terminal", 10)).pack()
commander = tkinter.Entry(win, width=20, font=("Terminal", 15))
commander.pack()
submit_button = tkinter.Button(win, width=20, text="Answer Me !!!", bg="#739af5", fg="white", command=say_command, font=("Terminal", 15))
submit_button.pack()
clear_button = tkinter.Button(win, width=20, text="Clear", bg="#739af5", fg="white", command=clear_command, font=("Terminal", 15))
clear_button.pack()
listen = tkinter.Button(win, width=20, text="Ask Roboman", bg="#739af5", fg="white", command=run_roboman, font=("Terminal", 15))
listen.pack()

win.mainloop()
