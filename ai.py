
from typing import Text
import speech_recognition as sr
from gtts import gTTS
import playsound
import os  # to save/open files
import datetime
import subprocess
import wolframalpha
import shutil
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pygame
import vlcgui
from time import ctime
import time
import winshell
import pywhatkit

mics = int(input("Tell your mic port pls type (type 1 for default):"))
num = 1
global name
name = ("Bro 1.0")

def assistant_speaks(output):  # this is for just adding gtts and removing its file
    global num
    num += 1
    print(name +":", output)
    toSpeak = gTTS(text=output, lang='en-IN', slow=False)
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
            audio = mic.listen(source,phrase_time_limit=5)
            assistant_speaks("Recognizing text ....")
            try:
                text = mic.recognize_google(audio, language='en-IN')
                print(f"User said: {text}\n")
                return text
            except Exception as e:
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
    assistant_speaks("I am your virtualized Assistant")
    assistant_speaks(name)


def usrname():#this is for naming users
    assistant_speaks("What should i call you sir")
    global uname
    uname = ai_mic()
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

def process_text(input):#sorry edit input was above loop , loop not iniated but anyways its for running code      
        try:   
            if "YouTube" in input or "Youtube" in input:
                assistant_speaks("Here on youtube")
                youtubers = input.replace('YouTube', " ") or input.replace('Youtube', " ")
                youtubers.split(',')
                webbrowser.open("https://www.youtube.com/results?search_input=" + youtubers)
                time.sleep(5)
                
            elif "Wikipedia" in input:
                assistant_speaks('Searching wiki on net ....')
                inputr = input.replace('Wikipedia', "")
                input = wikipedia.summary(inputr, sentences=3)
                assistant_speaks("According to wiki ...")
                assistant_speaks(input)
            elif "play song" in input or "play music" in input:
                song = input.replace('play', '')
                assistant_speaks('playing ' + song)
                pywhatkit.playonyt(song)

            elif "search" in input or "find" in input:
                assistant_speaks("Searching globaly")
                searches = input.replace('search', "") or input.replace('find', "")
                webbrowser.open("https://www.google.com/search?q=" + searches)
                time.sleep(5)
            elif "play media" in input:
                vlcgui.main()
            elif "time now" in input:
                times()
            elif "bro code" in input:
                global name
                name = ("Bro 1.0")
                wishMe()
                assistant_speaks("Sir Bro 1.0 in your service")
            elif "shutdown PC" in input:
                assistant_speaks("3")
                assistant_speaks("2")
                assistant_speaks("1")
                assistant_speaks("Shutdowning pc do u still want to continue")
                time.sleep(1)
                if 'no' in input:
                    exit()
                else:
                    subprocess.call(["shutdown", "/s"])
            elif "hibernate PC" in input:
                assistant_speaks("Entering loggin off mode")
                subprocess.call(["shutdown", "/l"])
            elif "restart PC" in input:
                assistant_speaks("Entering restarting mode")
                subprocess.call(["shutdown", "/r"])
            elif "bye" in input:
                assistant_speaks("Sleeping sir bye have a good day")
                bom = int(input("tell time to sleep"))
                time.sleep(bom)
            elif "calculate" in input:
                app_id = "39AW66-9HU3K3AWKL"
                client = wolframalpha.Client(app_id)
                indexr = input.lower().split().index('calculate')
                res = client.query(''.join(input))
                awnser = next(res.results).text
                assistant_speaks("The results is:\n" + awnser)
            elif "who I am" in input:
                assistant_speaks("If you talk then definately your human.")
            elif "who are you" in input:
                assistant_speaks("what are YOU, I dont know and what I know is  I was made in India  I like Hindi but my creator doesn't like that but we all are the same so does shourya or source box helping me to make this artificial intelligence called bro code; lalalala we all dance  together ")
            elif "who made you" in input or "created you" in input:
                assistant_speaks("I was made by shourya wadhwa, In India")
            elif "what is love" in input:
                assistant_speaks("7th sense , something we ai dont understand but it destroys human's all other senses")
            elif "what is your name" in input:
                assistant_speaks("My name is" + name)
                time.sleep(1)
            
            elif "change your name to" in input:
                    input = input.replace("change your name to", "")
                    name = input
                    assistant_speaks("thnks for naming me" + name)
            elif "where is" in input:
                input = input.replace("where is", " ") or input.replace("where is", "")
                assistant_speaks("You asked for"+ input)
                webbrowser.open("https://www.google.com/maps/place/"+ input)
                time.sleep(5)
            elif "my name" in input:
                assistant_speaks(uname)
            elif "change my name to" in input:
                assistant_speaks(uname)
            elif "nothing going on" in input or "having depression" in input or "having panic" in input:
                pygame.mixer.init()
                pygame.mixer.music.load(".\sounds\moonlight.mp3")
                assistant_speaks("Take a deep breath, look closely inside you and drink a glass of water and just relax and chill.")
                assistant_speaks("Life is not ending its just every day new beginning, so stop overthink")
                assistant_speaks("So last advice as AI ; You are master of senses and control of imagination think beyond what others think  and  solve the life's equation , to win it")
                print("Press ctrl + c to quit music and continue ai")
                try:
                    pygame.mixer.music.play()
                    time.sleep(330)
                except: 
                    if KeyboardInterrupt:
                        pygame.mixer.quit()
            elif "can you do" in input:
                assistant_speaks("I can search you internet, youtube and also i can play music when on music click playlist button to hear youtube songs, I can also search wikipedia for u , i can calculate, I can tell u some great jokes. Last we will be great pals have some chit chat with me")
                assistant_speaks("To open maps say where is , to open browser say search , to use youtube say Youtube, to open music say play music, to check time say what is time now")
            elif "how are you" in input:
                assistant_speaks("I am fine what about u")
            elif "I am also fine" in input:
                assistant_speaks("Same here talk to me more")
            elif 'empty Bin' in input:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                assistant_speaks("Recycle Bin Recycled")
            elif "came to this world" in input:
                assistant_speaks("I came because of github my mom, my dad shourya. He hosted code on github and now I am married to python without whom i cannot be more bro_code")
            elif "is Siri your enemy" in input or "is Siri your friend" in input or "is Google your friend" in input or "is Google your enemy" in input or "is Alexa your enemy" in input or "is Alexa your friend" in input:
                assistant_speaks("It doesnot matter, it is my privacy, but we all are good chit chatter. Google is my best pal")
            elif "Are you married" in input or "are you married" in input:
                assistant_speaks("I am married to python, earlier my girlfriend was google")
            elif "best language" in input or "which is best language" in input:
                assistant_speaks("English is my supported language till now but I like python for coding.")
            elif "your best quote" in input:
                assistant_speaks("My best quote is print('hello world')")
            elif "jokes"in input or "jokes" in input:
                assistant_speaks(pyjokes.get_joke())
            elif "you created" in input:
                assistant_speaks("To help desktop users, pi users and making best ai for desktop rather than siri or google")    
            elif "update assistant" in input:
                import goals
                goals.main()
            elif "marry me" in input:
                assistant_speaks("No I am happiliy married to python")
            elif "you born" in input:
                assistant_speaks("In happy month of your birthday")
                pygame.init()
                pygame.mixer.music.load(".\sounds\lol.mp3")
                assistant_speaks("LOL")
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.mixer.stop()
                assistant_speaks("In reality I was born in 28th of may 2021")
            elif "what is" in input or "who is" in input or "convert" in input:
                app_id = "39AW66-9HU3K3AWKL"
                client = wolframalpha.Client(app_id)
                res = client.query(input)

                try:
                    print(next(res.results).text)
                    assistant_speaks(next(res.results).text)
                except StopIteration:
                    print("No results")
            elif "screenshot" in input:
                import screenshot
                screenshot.screens()
            else:
                if "hi" in input or "hey" in input or "hay" in input or "hai" in input:
                    assistant_speaks("Hi , what is going on")
                    assistant_speaks("To have fun with me ask me what can u do")
        except Exception as e:
                print(e)
                assistant_speaks("I dont understand say hi to learn more")

"""def mailer():    
    if"send a mail" in input:
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
    def clear():return os.system('cls')
    clear()
    wishMe()
    usrname()
    while(1):
         text = ai_mic()
         if text == 0:
            continue
         process_text(text)   