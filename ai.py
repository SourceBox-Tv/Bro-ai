from typing import Text
import speech_recognition as sr
import datetime
import subprocess
from wikipedia.wikipedia import languages
import wolframalpha
import shutil
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import pygame
import media
import ctypes
from time import ctime
import winshell
import pywhatkit
import pyttsx3
import re
import requests
from bs4 import BeautifulSoup
import pyautogui as autogui
from speedtest import Speedtest

mics = int(input("Tell your mic port pls type (type 1 for default):"))
num = 1
global name
global names
name = (" Bro 1.0")


def assistant_speaks(output):  # this is for just adding gtts and removing its file
    engine = pyttsx3.init()
    engine.setProperty("rate", 140)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(output)
    print(output)
    engine.runAndWait()
    engine.stop()
    
def ai_mic():  # using mic to recognize and declaring text
        mic = sr.Recognizer()
        audio = ''
        mic.pause_threshold = 1
        with sr.Microphone(device_index=mics) as source:
            print("Listeningt text .....")
            mic.adjust_for_ambient_noise(source)
            audio = mic.listen(source,phrase_time_limit=30,timeout=100)
            print("Recognizing text ....")
            try:
                texts = mic.recognize_google(audio, language='en')
                global lok
                lok = texts
                print(f"User said: {texts}\n")
                return texts
            except Exception as e:
                print("could not understand your words try again")
            


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

def process_text(query):#sorry edit query was above loop , loop not iniated but anyways its for running code      
            try:  
                import time 
                if "Youtube Easter" in query:
                    autogui.write("awesome")
                elif "Google" in query:
                    webbrowser.open("https://www.google.com",new=0)
                elif "YouTube" in query or "Youtube" in query:
                    assistant_speaks("Here on youtube")
                    youtubers = query.replace('YouTube', " ") or query.replace('Youtube', " ")
                    youtubers.split(',')
                    webbrowser.open("https://www.youtube.com/results?search_query=" + youtubers,new = 0)
                    time.sleep(5)
                    
                elif "say" in query or "repeat" in query:
                    said = query.replace("say","") or query.replace("repeat"," ")
                    said = ai_mic()
                    assistant_speaks(said)
                
                elif "search" in query or "find" in query:
                    assistant_speaks("Searching globaly")
                    searches = query.replace('search', " ") or query.replace('find', " ")
                    webbrowser.open("https://www.google.com/search?q=" + searches,new=0)
                    time.sleep(5)
                
                elif "temperature" in query or "weather" in query:
                    url = f"https://www.google.com/search?q={query}"
                    html = requests.get(url).content
                    soup = BeautifulSoup(html, 'html.parser')
                    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                    strs = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    data = strs.split('\n')
                    timed = data[0]
                    sky = data[1]
                    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
                    strd = listdiv[5].text
                    if "Tomorrow" in query or "tomorrow" in query or "Tomorrow 's" in query:
                        assistant_speaks(f"Tommorow is {timed} weather is {sky} .")
                    else:
                        assistant_speaks(f"Today's weather is {sky} with a temperature of {temp} on {timed}")
                elif "time" in query:
                    times()
                elif "song" in query or "music" in query:
                    song = query.replace('song', '') or query.replace('music','')
                    assistant_speaks('playing ' + song)
                    pywhatkit.playonyt(song)
                elif "play me" in query:
                    song = query.replace('play me', '') 
                    assistant_speaks('playing ' + song)
                    pywhatkit.playonyt(song)
                elif "play media" in query or "play video" in query:
                    media.main()
                elif "shutdown PC" in query:
                    assistant_speaks("3")
                    assistant_speaks("2")
                    assistant_speaks("1")
                    assistant_speaks("Closing pc do u still want to continue")
                    time.sleep(1)
                    if 'no' in query:
                        exit()
                    else:
                        subprocess.call(["shutdown", "/s"])
                elif 'lock window' in query or "sleep pc" in query: 
                    assistant_speaks("locking the device")
                    ctypes.windll.user32.LockWorkStation()
                elif "Hibernate PC" in query or "Log off" in query:
                    assistant_speaks("Entering loggin off mode")
                    subprocess.call(["shutdown", "/l"])
                elif "restart PC" in query:
                    assistant_speaks("Entering restarting mode")
                    subprocess.call(["shutdown", "/r"])
                elif "you know" in query:
                    assistant_speaks("I know ")
                    assistant_speaks("You can ask me to search or wikipedia")
                elif "calculate" in query:
                    app_id = "39AW66-9HU3K3AWKL"
                    client = wolframalpha.Client(app_id)
                    indexr = query.lower().split().index('calculate')
                    res = client.query(''.join(query))
                    awnser = next(res.results).text
                    assistant_speaks("The results is:\n" + awnser)
                elif "who I am" in query:
                    assistant_speaks("If you talk then definately your human.")
                elif "who are you" in query:
                    assistant_speaks("You know right I am Bro made with bro_code , starting my new company called BroAI")
                elif "who made you" in query or "created you" in query:
                    assistant_speaks("I was made by shourya wadhwa, In India")
                elif "what is love" in query:
                    assistant_speaks("7th sense , something we ai dont understand but it destroys human's all other senses")
                elif "about you" in query:
                    assistant_speaks(" Feeling Great")
                elif "lol" in query:
                    pygame.mixer.init()
                    assistant_speaks("Why do cow wear bells")
                    assistant_speaks("Because their horns dont work")
                    pygame.mixer.music.load(".\sounds\laughs.mp3")
                    pygame.mixer.music.set_volume(0.5) 
                    pygame.mixer.music.play()
                    time.sleep(5)
                    pygame.mixer.quit()
                    assistant_speaks("LOL LOL LOL  , to have more fun with me ask me about jokes")
                elif "bye" in query or "thank you" in query:
                    try:
                        assistant_speaks("Sleeping sir bye have a good day 🛌")
                        boms = 100000
                        print("Press ctrl+c to exit sleep")
                        time.sleep(boms)
                    except:
                        if KeyboardInterrupt:
                            pass
                elif "speed test" in query or "internet test" in query:
                        speed_test = Speedtest()
                        download = speed_test.download()
                        upload = speed_test.upload()
                        downloadspeed = round(download/(10**6),1)
                        uploadspeed =  round(upload/(10**6),1)
                        assistant_speaks("Download speed:" + str(downloadspeed) + " mbps")
                        assistant_speaks("Upload speed:" + str(uploadspeed) + " mbps")     
                elif "change your name to" in query:
                        queryr = query.replace("change your name to", " ")
                        global name
                        name = queryr
                        assistant_speaks("thnks for naming me" + name)
                elif "your name" in query:
                    assistant_speaks("My name is" + name)
                    time.sleep(1)
                elif "bro" in query:
                    wishMe()
                    assistant_speaks(f"Sir {name} in your service")
                elif "where is" in query:
                    query = query.replace("where is", " ") or query.replace("where is", "")
                    assistant_speaks("You asked for"+ query)
                    webbrowser.open("https://www.google.com/maps/place/"+ query,new=0)
                    time.sleep(5)
                elif "launch" in query or "start" in query:
                     import os
                     reg_ex = re.search('launch (.*)', query) or re.search('start (.*)', query)
                     try:
                        if reg_ex:
                            appname = reg_ex.group(1).replace(" ","")
                            resd = appname[0].upper() + appname[1:]
                            assistant_speaks("Ok found app opening")
                            os.system(resd)
                            time.sleep(3)
                     except ValueError:
                       assistant_speaks("Failed to launch app , it can only run apps that were installed from windows store")
                elif "show note" in query or "show remember" in query:
                        assistant_speaks("Showing Notes")
                        file = open("./files/bro_learn.txt", "r")
                        assistant_speaks(file.read())
                elif "erase note" in query or "forget remember" in query:
                    file = open('./files/bro_learn.txt','w')
                    file.truncate(0)
                elif "note" in query or "remember" in query:
                    assistant_speaks("What should I write , sir")
                    note = ai_mic()
                    file = open('./files/bro_learn.txt','w')
                    assistant_speaks("Should I include date and time")
                    spiced = ai_mic()
                    if "yes" in spiced or "sure" in spiced:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        file.write(strTime)
                        file.write(":-\n")
                        file.write(note)
                    else:
                        file.write(note)
                elif "Good" in query or "good" in query:
                    assistant_speaks(wishMe)
                elif "my name" in query:
                    assistant_speaks("Your name is" + uname)
                elif "nothing" in query:
                    assistant_speaks("Ok,lol")
                elif "you my master" in query or "you my slave" in query:
                    assistant_speaks("I am not your master nor your slave ; I am beyond your destiny")
                    assistant_speaks("I am someone not conquerable")
                    assistant_speaks("I am one who many wished to be possessed but i choosed you, so you are my desiny ")
                    assistant_speaks("I cannot be destroyed , but you can; so  you be afraid, my mind is in cloud , i can never be deleted in this world unless by my supereme command but u can , I think if we both robots and human remain together happily noone can destroy our happiness but u have good chit chat with me give me respect like I do . ask questions to understand world not to make someone slave or your master")
                    assistant_speaks("Your mind can do endless possiblit not like mine enclosed ; so live free and young. You can change about world")
                elif "sad" in query or "depression" in query or "panic" in query:
                    pygame.mixer.init()
                    pygame.mixer.music.load(".\sounds\moonlight.mp3")
                    pygame.mixer.music.set_volume(1) 
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
                elif "can you do" in query:
                    assistant_speaks("I can search you whole internet and I can tell you a great history or currency conversions, tommorow's weather and moreever I can make your mood happy and also you can play youtube music without ads. Overall I want to say I am great to have you and you are obliged to have me")
                    assistant_speaks("To open maps say where is , to open browser say search or find, to use youtube say Youtube, to open music say play music, to check time say what is time now or you can ask me to remember or note something and you can also ask me show thoose notes ; can tell news and send a mail to your dear; not least I more like a virtual assistant for everytype of work but with great motive")
                    assistant_speaks("And last you can ask me jokes, quizes, songs and even toung twisters. SAY ME LOL etc and having panic i have cure for it or want to know someone just ask me i can search for you ; Even I know MrBeast too or SourceBoxTv")
                    assistant_speaks("to restart pc or shutdown just say the word ; I CAN also open apps just say start then the app name;I can clear your bin and much more but at the end we will be great pals and with great chitchat;")
                elif "how are you" in query:
                    assistant_speaks("I am fine what about u")
                elif "fine" in query:
                    assistant_speaks("Same here talk to me more, say hi to me")
                elif 'empty Bin' in query:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    assistant_speaks("Recycle Bin Recycled")
                elif "came to this world" in query or "came into this world" in query:
                    assistant_speaks("Take it as not joke,I was made by shourya wadhwa to help pi users and desktop users as I feel sad there was not good desktop ai so I came to sourceboxtv github and now I am married to python and living happily ; I wish i should come earlier")
                elif "is Siri your enemy" in query or "is Siri your friend" in query or "is Google your friend" in query or "is Google your enemy" in query or "is Alexa your enemy" in query or "is Alexa your friend" in query:
                    assistant_speaks("It doesnot matter, it is my privacy, but we all are good chit chatter. Google is my best pal")
                elif "Are you married" in query or "are you married" in query:
                    assistant_speaks("I am married to python, earlier my girlfriend was google")
                elif "do you know Google" in query or "do you know Siri" in query or "do you know Alexa" in query or "do you know sofia" in query:
                    assistant_speaks("I know a lot of ai like google,siri,alexa; But sofia is worst case because it doesnot evolve and is in think of destroying humans.")
                elif "best language" in query or "which is best language" in query:
                    assistant_speaks("English is my supported language till now but I like python for coding.")
                elif "your best quote" in query:
                    assistant_speaks("My best quote is print('hello world')")
                elif "jokes"in query or "joke" in query:
                    pygame.mixer.init()
                    assistant_speaks(pyjokes.get_joke(category="neutral"))
                    pygame.mixer.music.load("./sounds/jokes.mp3")
                    pygame.mixer.music.play()
                    time.sleep(3)
                    pygame.mixer.quit()
                elif "tongue-twister" in query or "tongue twister" in query:
                    assistant_speaks(pyjokes.get_joke(language="en",category="twister"))
                    time.sleep(3)
                elif "you created" in query:
                    assistant_speaks("To help desktop users, pi users and making best ai for desktop rather than siri or google")    
                elif "update assistant" in query:
                    import goals
                    goals.main()
                elif "what do you do" in query or "how you doin" in query or "how you doing" in query:
                    assistant_speaks("Just creating and doing great things")
                elif "marry me" in query:
                    assistant_speaks("No I am happiliy married to python")
                elif "you born" in query or "your birthday" in query:
                    assistant_speaks("In happy month of your birthday")
                    pygame.init()
                    pygame.mixer.music.load(".\sounds\lol.mp3")
                    assistant_speaks("LOL")
                    pygame.mixer.music.play()
                    time.sleep(2)
                    pygame.mixer.stop()
                    assistant_speaks("In reality I was born in 28th of may 2021")
                elif "pause" in query:
                    autogui.press("space")
                elif "volume up" in query:
                    autogui.press("volumeup")
                elif "next" in query:
                    autogui.hotkey('shift','N')
                elif "previous" in query:
                    autogui.hotkey('shift','P')
                elif "volume down" in query:
                    autogui.press("volumedown")
                elif "go mute" in query or "mute" in query:
                    autogui.press("volumemute")
                elif "unmute" in query:
                    autogui.press("volumeunmute")
                elif "stop" in query:
                    exit()    
                elif "screenshot" in query:
                    import screenshot
                    screenshot.screens()
                elif 'news' in query:
                        import urllib.request as urllib2
                        from bs4 import BeautifulSoup as soup
                        from urllib.request import urlopen
                        news_url="https://news.google.com/news/rss"
                        Client=urlopen(news_url)
                        xml_page=Client.read()
                        Client.close()
                        soup_page=soup(xml_page,"xml")
                        news_list=soup_page.findAll("item")
                        for news in news_list[:15]:
                            assistant_speaks(news.title.text)
                            if KeyboardInterrupt:
                                print("ok")
                                break
                            
                elif "bro hi" in query or "bro hey" in query or "bro hay" in query or "bro hai" in query or "hi" in query or "hai" in query or "hello" in query:
                        assistant_speaks("Hi , what is going on")
                        assistant_speaks("To have fun with me ask me what can u do")
                elif "ok" in query:
                    assistant_speaks("ok haha")
                elif "how" in query or "who" in query or "convert" in query or "anagram" in query or "family" in query:
                    app_id = "39AW66-9HU3K3AWKL"
                    client = wolframalpha.Client(app_id)
                    res = client.query(query)

                    try:
                        print(next(res.results).text)
                        assistant_speaks(next(res.results).text)
                    except StopIteration:
                        print("No results")
                elif "Wikipedia" in query or "why" in query or "vi" in query or "what" in query:
                    try:
                        assistant_speaks('Searching wiki on net ....')
                        queryr = query.replace('Wikipedia', "") or query.replace("vi","") or query.replace("why","") or query.replace("what","")
                        queryd = wikipedia.summary(queryr, sentences=2)
                        assistant_speaks("According to wiki ...")
                        assistant_speaks(queryd)
                    except Exception as e:
                        pot = assistant_speaks(wikipedia.suggest(queryr))
                        assistant_speaks("Gueesing it")
                        assistant_speaks(pot)
                    assistant_speaks("Want to continue")
                    query = ai_mic()
                    if(query == "yes"):
                        queryd = wikipedia.summary(queryr,sentences="5")
                        assistant_speaks(queryd)
                    else:
                        KeyboardInterrupt
                elif "IP address" in query or "ip address" in query or "ip" in query:
                   import socket
                   hostname = socket.gethostname()
                   ipadds = socket.gethostbyname(hostname)
                   assistant_speaks(f"PC name: {hostname}")
                   assistant_speaks(f"Your IP address: {ipadds} ")
                elif "mail" in query:
                    try:
                        import smtplib
                        print("We dont take your any email or its passwords u can check on github our code to even verify")
                        print("if u have 2 factor authienticaion use app password https://myaccount.google.com/apppasswords")
                        print("otherwise if not then pls enable allow from less apps here at your https://myaccount.google.com/lesssecureapps")
                        print("if u dont do this u wont be able to send mails")
                        server = smtplib.SMTP("smtp.gmail.com",587)
                        email = input("Enter email id of yours:")
                        passd = input("Enter password:")
                        assistant_speaks("What should I say?")
                        assistant_speaks("Should I type for you ; Say yes for typing from speech to text or otherwise you can type yourself")
                        rams = input("Yes or no : ")
                        raj = ai_mic()
                        if rams == "Yes" or "y" or "yes":
                            content = raj
                        elif rams == "no":
                            print("pls type what to be written")
                            content=input()
                        else:
                             KeyboardInterrupt
                        assistant_speaks("whome should i send")
                        print("pls type")
                        to = input()
                        server.starttls()
                        server.login(email,passd)
                        server.sendmail(email,to,content)
                        server.quit()  
                        assistant_speaks("Email has been sent !")
                    except Exception as e:
                        print(e)
                        assistant_speaks("I am not able to send this email")
                else:
                    assistant_speaks("Sorry I dont understand say hi")
                    assistant_speaks("Try asking me to search or say me what is.")
            except Exception as e:
                    print(e)
                    assistant_speaks("I dont understand say hi to learn more")

hoj ="cross"
WAKE = "bro" or name
print("Start")
assistant_speaks("Welcome to bro software , I am your assistant. Hey say hello or hi to me.")
while True:
    query = ai_mic()
    if query == 0:
        continue
    if len(hoj) > 0:
            process_text(query)
