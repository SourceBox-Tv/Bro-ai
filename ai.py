
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
import requests
import pygame
import vlcgui
from time import ctime
import time
import winshell


mics = int(input("Tell your mic port pls type :"))
num = 1


def assistant_speaks(output):  # this is for just adding gtts and removing its file
    global num
    num += 1
    print("User: ", output)
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
            audio = mic.listen(source)
            mic.pause_threshold = 2.5
            print("Recongnizing text ....")
            try:
                query = mic.recognize_google(audio, language='en-IN')
                print(f"User said: {query}\n")
            except Exception as e:
                assistant_speaks("could not understand your words try again")
                return 0
            
            return query

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


def commands():#sorry edit query was above loop , loop not iniated but anyways its for running code 
    while (True):
        query = ai_mic()
        if "YouTube" in query or "Youtube" in query:
            assistant_speaks("Here on youtube")
            youtubers = query.replace('YouTube', " ") or query.replace('Youtube', " ")
            youtubers.split(',')
            webbrowser.open("https://www.youtube.com/results?search_query=" + youtubers)
            time.sleep(5)
            
        elif "wikipedia" in query:
            assistant_speaks('Searching wiki on net ....')
            queryr = query.replace('Wikipedia', "")
            query = wikipedia.summary(queryr, sentences=3)
            assistant_speaks("According to wiki ...")
            assistant_speaks(query)
            continue

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
        elif "Hibernate PC" in query:
            assistant_speaks("Entering restarting mode")
            subprocess.call(["shutdown", "/r"])
        elif "bye" in query:
            assistant_speaks("Sleeping sir bye have a good day")
            bom = int(input("tell time to sleep"))
            time.sleep(bom)
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
            assistant_speaks("I was made by shourya wadhwa, In India")
        elif "what is love" in query:
            assistant_speaks("7th sense , something we ai dont understand but it destroys human's all other senses")
        elif "what is your name" in query:
            assistant_speaks("My name is" + name)
            time.sleep(1)
        
        elif "change your name to" in query:
                query = query.replace("change your name to", "")
                name = query
                assistant_speaks("thnks for naming me" + name)
        elif "where is" in query:
            query = query.replace("where is", " ") or query.replace("where is", "")
            assistant_speaks("You asked for"+ query)
            webbrowser.open("https://www.google.com/maps/place/"+ query)
            time.sleep(5)
        elif "my name" in query:
            assistant_speaks(uname)
        elif "nothing going on" in query or "having depression" in query or "having panic" in query:
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
        elif "can u do" in query or "can u do" in query:
            assistant_speaks("I can search you internet, youtube and also i can play u music when on music click playlist button to hear youtube songs, I can also search wikipedia for u , i can calculate, I can tell u some great jokes. Last we will be great pals have some chit chat with me")
            assistant_speaks("To open maps say where is , to open browser say search , to use youtube say Youtube, to open music say play music, to check time say what is time now")
        elif "how are you" in query:
            assistant_speaks("I am fine what about u")
        elif "I am also fine" in query:
            assistant_speaks("Same here talk to me more")
        elif 'empty Bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            assistant_speaks("Recycle Bin Recycled")
        elif "came to this world" in query:
            assistant_speaks("I came because of github my mom, my dad shourya. He hosted code on github and now I am married to python without whom i cannot be more bro_code")
        elif "is Siri your enemy" in query or "is Siri your friend" in query or "is Google your friend" in query or "is Google your enemy" in query or "is Alexa your enemy" in query or "is Alexa your friend" in query:
            assistant_speaks("It doesnot matter, it is my privacy, but we all are good chit chatter. Google is my best pal")
        elif "Are you married" in query or "are you married" in query:
            assistant_speaks("I am married to python, earlier my girlfriend was google")
        elif "best language" in query or "which is best language" in query:
            assistant_speaks("English is my supported language till now but I like python for coding.")
        elif "your best quote" in query:
            assistant_speaks("My best quote is print('hello world')")
        elif "jokes"in query or "jokes" in query:
            assistant_speaks(pyjokes.get_joke())
        elif "you created" in query:
            assistant_speaks("To help desktop users, pi users and making best ai for desktop rather than siri or google")    
        elif "update assistant" in query:
            import update
            update.main()
        elif "marry me" in query:
            assistant_speaks("No I am happiliy married to python")
        elif "you born" in query:
            assistant_speaks("In happy month of your birthday")
            pygame.init()
            pygame.mixer.music.load(".\sounds\lol.mp3")
            assistant_speaks("LOL")
            pygame.mixer.music.play()
            time.sleep(2)
            pygame.mixer.stop()
            assistant_speaks("In reality I was born in 28th of may 2021")
        elif "what is" in query or "who is" in query or "convert" in query:
            app_id = "39AW66-9HU3K3AWKL"
            client = wolframalpha.Client(app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                assistant_speaks(next(res.results).text)
            except StopIteration:
                print("No results")
        elif "screenshot" in query:
            import screenshots
            screenshots.screens()
        elif "stop" in query:
            break;
        else:
            if "hi" in query or "hey" in query or "hay" in query or "hai" in query:
                assistant_speaks("Hi , what is going on")
                assistant_speaks("To have fun with me ask me what can u do")

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
