import speech_recognition as sr
from gtts import gTTS
import playsound
import os  # to save/open files
import datetime
import subprocess
from twilio.rest.api.v2010.account import message
import wolframalpha
import shutil
import tkinter
import json
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import ctypes
import requests
import cv2
import vlcgui
from time import ctime
import time

mics = int(input("Tell your mic port pls type :"))
num = 1


def assistant_speaks(output):  # this is for just adding gtts and removing its file
    global num
    num += 1
    print("User: ", output)
    toSpeak = gTTS(text=output, lang='en-UK', slow=False)
    file = str(num)+".mp3 "
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)


def ai_mic():  # using mic to recognize and declaring text
    mic = sr.Recognizer()
    audio = ''
    with sr.Microphone(device_index=mics) as source:
        print("Listeningt text .....")
        mic.adjust_for_ambient_noise(source)
        audio = mic.listen(source, phrase_time_limit=5)
        print("Recongnizing text ....")
        try:
            lang = mic.recognize_google(audio, language='en-UK')
            print("your text:", lang)
            return lang
        except:
            assistant_speaks("could not understand your words try again")
            return 0


def wishMe():#this is for wishing user
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        assistant_speaks("Hello,Good Morning")
    elif hour >= 12 and hour < 16:
        assistant_speaks("Hello,Good Afternoon")
    elif hour >= 16 and hour < 20:
        assistant_speaks("Hello,Good Evening")
    else:
        assistant_speaks("Hello, Good night")
    global name
    name = ("Bro 1.0")
    assistant_speaks("I am your virtualized Assistant")
    assistant_speaks(name)


def usrname():#this is for naming users
    assistant_speaks("What should i call you sir")
    print("pls type this one last")
    uname = input("")
    assistant_speaks("Welcome Mister/Mistress")
    assistant_speaks(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    assistant_speaks("How can i Help you, Sir")


def times():#this is for declaring time
    strTime = ctime()
    assistant_speaks(f"Sir time right now is {strTime}.")


"""def sendEmails(to,content):
    server = SMTP('smtp.gmail.com',465)
    email = input("Enter email id of yours")
    passd = input("Enter password")
    server.login(email,passd)
    server.sendmail(email,to,content)
    server.close()
"""


def commands():#sorry edit query was above loop , loop not iniated but anyways its for running code 
    while (True):
        query = ai_mic()
        if "wikipedia" in query:
            assistant_speaks('Searching wiki on net ....')
            queryr = query.replace('Wikipedia', "")
            query = wikipedia.summary(queryr, sentences=3)
            assistant_speaks("According to wiki ...")
            assistant_speaks(query)
            continue

        elif "YouTube" in query or "Youtube" in query:
            assistant_speaks("Here on youtube")
            youtubers = query.replace('YouTube', " ") or query.replace('Youtube', " ")
            youtubers.split(',')
            webbrowser.open("https://www.youtube.com/results?search_query=" + youtubers)
            time.sleep(5)

        elif "search" in query or 'find' in query:
            assistant_speaks("Searching globaly")
            searches = query.replace('search', "") or query.replace('find', "")
            webbrowser.open("https://www.google.com/search?q=" + searches)
            time.sleep(5)
        elif "play music" in query or "play song" in query:
            vlcgui.main()
        elif "time now" in query:
            times()
        elif "bro code" in query:
            global name
            name = ("Bro 1.0")
            wishMe()
            assistant_speaks("Sir Bro 1.0 in your service")
        elif "shutdown PC" in query:
            assistant_speaks("3")
            assistant_speaks("2")
            assistant_speaks("1")
            assistant_speaks("Shutdowning pc do u still want to continue")
            time.sleep(1)
            if 'no' in query:
                exit()
            else:
                subprocess.call(["shutdown", "/s"])
        elif "Hibernate PC" in query:
            assistant_speaks("Entering loggin off mode")
            subprocess.call(["shutdown", "/l"])
        elif "bye" in query:
            assistant_speaks("Sleeping sir bye have a good day")
            print("press ctrl +c to activate again")
            time.sleep(10000)
            continue
        elif "calculate" in query:
            app_id = "39AW66-9HU3K3AWKL"
            client = wolframalpha.Client(app_id)
            indexr = query.lower().split().index('calculate')
            res = client.query(''.join(query))
            awnser = next(res.results).text
            assistant_speaks("The query are:\n" + awnser)
        elif "who I am" in query:
            assistant_speaks("If you talk then definately your human.")
        elif "who are you" in query:
            assistant_speaks("what are YOU, I dont know and what I know is  I was made in India  I like Hindi but my creator doesn't like that but we all are the same so does shourya or source box helping me to make this artificial intelligence called bro code; lalalala we all dance  together ")
        elif "who made you" in query:
            assistant_speaks("I was made by supreme command of sourceboxtv aka shourya wadhwa")
        elif "what is love" in query:
            assistant_speaks("7th sense , something we ai dont understand but it destroys human's all other senses")
        elif "what is your name" in query:
            name = "brocode"
            assistant_speaks("My name is" + name)
            time.sleep(1)
        elif "change your name" in query:
                query = query.replace("change your name", "")
                name = query
                assistant_speaks("thnks for naming me" + name)
        elif "where is" in query:
            query = query.replace("Where is", " ") or query.replace("where is", "")
            assistant_speaks("You asked for"+ query)
            webbrowser.open("https://www.google.com/maps/place/"+ query)
        elif "what is" in query or "who is" in query or "convert" in query:
            app_id = "39AW66-9HU3K3AWKL"
            client = wolframalpha.Client(app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                assistant_speaks(next(res.results).text)
            except StopIteration:
                print("No results")
        elif "hi" in query or "hey" in query or "hay" in query or "hai" in query:
            assistant_speaks("Hi , what is going on")
        elif "nothing going on" in query or "having depression" in query or "having panic" in query:
            import pygame
            pygame.mixer.init()
            assistant_speaks("Take a deep breath, look closely inside you and drink a glass of water and just relax and chill.")
            assistant_speaks("Life is not ending its just every day new beginning, so stop overthink")
            assistant_speaks("So last advice as AI ; You are master of senses and control of imagination think beyond what others think  and  solve the life's equation , to win it")
            pygame.mixer.music.load("sound\moonlight.mp3")
            pygame.mixer.music.play()
            if KeyboardInterrupt:
                pygame.mixer.music.stop()
        elif "update assistant" in query:
            assistant_speaks("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)


"""def mailer():    
    if"send a mail" in query:
            try:
                assistant_speaks("What should I say?")
                content = input()
                assistant_speaks("whoome should i send")
                to = input()   
                sendEmails(to, content)
                assistant_speaks("Email has been sent !")
            except Exception as e:
                print(e)
                assistant_speaks("I am not able to send this email")
"""
if __name__ == '__main__':
    def clear(): return os.system('cls')
    clear()
    wishMe()
    usrname()
    commands()
