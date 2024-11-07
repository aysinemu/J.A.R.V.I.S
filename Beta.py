#Cre:Tấn Cường UTE
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
from datetime import date
import instaloader
import time 
from time import sleep as wait
import pyautogui
import PyPDF2
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
import cv2
import urllib.request
import numpy as np
import urllib3 as urllib
engine = pyttsx3.init('sapi5')
#getProperty get the voice from the library
voices = engine.getProperty('voices')
#voices[x].id to next you know which voice you are using right now
#print(voices[1].id)
#setProperty set the voice that you get to standard and use that voice to speak
i = 0
engine.setProperty('voices',voices[i].id)
#set the speed of the voice
engine.setProperty('rate',180)
#read the news
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=    '
    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        #print(f"Today 's {day[i]} News 's: ",head[i])
        speak(f"Today {day[i]} News Is: {head[i]}")
#Send email to someone
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('    ','    ')
    server.sendmail('    ',to , content)
    server.close()
#Change text to voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#convert what you say into text so its can do anything you want
def command():
    read = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        read.pause_threshold = 1
        audio = read.listen(source, timeout = 1, phrase_time_limit = 5)
    try:
        print("Recognizing...")
        query = read.recognize_google(audio, language = 'en-vn')
        print(f"User Said: {query}")
    except Exception as Ex:
        speak("Can You Repeat It Please")    
        return "none"
    return query
#import the time so its know what time is it and what to say
def time():
    hour = int(datetime.datetime.now().hour)
    today = date.today()
    time = datetime.datetime.now()
    current_time = time.strftime("%H:%M:%S")
    s1 = 'Good Morning, '
    s2 = 'Good Afternoon, '
    s3 = 'Good Evening, '
    s4 = 'Today Date Is '
    s5 = s4 + str(today) + ' ' + str(current_time)
    if hour >= 0  and hour <= 12:
        s6 = s1 + s5
        speak(s6)
    if hour > 12 and hour < 18:
        s7 = s2 + s5
        speak(s7)
    if hour >= 18 and hour < 24:
        s8 = s3 + s5
        speak(s8)
    speak("I Am Jarvis Sir, How Can I Help You Today")
#do task
def task():
    time()
    while True:
        #building some simple task so its can do when jarvis heard what you said and the word you say
        #is similar with the word in the simple task
        query = command().lower()
        #print(f"User Said: {query}")
        if "open notepad" in query:
            notepadpath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2112.32.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(notepadpath)
        elif "close notepad" in query: 
            speak("Ok Sir, Closing Notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "open command prompt" in query:
            os.system("Start CMD")
        elif "play sad music" in query:
            music = "E:\\Samsung\\J.A.R.V.I.S\\JARVIS\Music\\y2mate.com - MRSIRO VERSION Đừng Lo Anh Đợi Mà_1080p.mp4"
            os.startfile(music)
        elif "play music" in query:
            musics = "E:\\Samsung\\J.A.R.V.I.S\\JARVIS\\Music"
            songs = os.listdir(musics)
            rd = random.choice(songs)
            os.startfile(os.path.join(musics, rd))
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is: {ip}")
        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            #print(query)
            result = wikipedia.summary(query, sentences = 2)
            speak("According To Wikipedia")
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open google" in query:
            speak("What do you want me to search on Google sir?")        
            cmd = command().lower()
            webbrowser.open(f"{cmd}") 
        elif "email to me" in query:
            speak("What Should I Do Sir")
            query = command().lower()
            if "send a file" in query:
                try:
                    email = ''
                    password = ''
                    send_to = ''
                    speak("Okay Sir, What 's The Subject For This Email")
                    query = command().lower()
                    subject = query
                    speak("And Sir, What 's The Message For This Email")
                    query1 = command().lower()
                    message = query1
                    speak("Sir Please Enter The Correct Path To The File Location")
                    file_location = input("Please Enter The Path Here: ")
                    speak("Please Wait, I 'm Sending The Email Now")
                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))
                    #Set up the file
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename = %s" % filename)
                    #Attach the attachment to the MIMEMultipart object
                    msg.attach(part)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('    ','     ')
                    text = msg.as_string()
                    server.sendmail(email, send_to, text)
                    server.quit()
                    speak("The Email Have Been Send")
                except Exception as Ex:
                    print(Ex)
                    speak("Sorry sir, unfortunately i can not send the email because of some technical problem")
                    pass   
            else:    
                try:
                    speak("What should i write sir?")
                    content = command().lower()
                    to = "    "
                    sendEmail(to, content)
                    speak("Email have been send successfully")
                except Exception as Ex:
                    print(Ex)
                    speak("Sorry sir, unfortunately i can not send the email because of some technical problem")
                    pass
        elif "tell me about the news today" in query:
            speak("Please Wait Sir,Looking For The Newest News")
            news()
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("Sir Please Enter The User Name Correctly")
            name = input("Enter User Name Here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir Here Is The Profile Of The User {name}")
            wait(5)
            speak("Sir Would You Like To Dowload The Profile Picture Of This Account")
            condition = command().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I Am Done Sir, Profile Picture Is Save In Our Jarvis Folder")
            else:
                pass
        elif "take a screenshot" in query or "take screenshot" in query:
            speak("Please Tell Me The Name Of This Screenshot File")
            name = command().lower()
            speak("Please Hold The Screen For A Second Please, I Am Taking The Screenshot Right Now")
            wait(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I Am Done Sir, It Is Save In Our Jarvis Folder")
        elif "where i am" in query or "where we are" in query:
            speak("Wait Sir, I Will Check Right Now")
            try:
                ipAdd = get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir I 'm Not Sure, But I Think We Are In {city} City Of {country}")
            except Exception as Ex:
                speak("Sorry Sir, Due To The Network Connection I Do Not Know Where We Are, I Am Apologize For The Inconvenient")
                pass
        elif "tell me the temperature" in query:
            speak("Where Do You Want To Know")
            place = command().upper()
            s1 = place
            s2 = 'Temperature In ' + place
            url = f"https://www.google.com/search?q={s2}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {s2} Is {temp}")
        elif "no thanks" in query:
            speak("Thank You For Using Me Sir")
            sys.exit()
        elif "sleep" in query:
            speak("Sleeping, Wake Me Up When You Need Help")    
            break
        elif "want to make" in query:
            speak("What Do You Want To Make")
            something = command()
            max_results = 1
            how_to = search_wikihow(something, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        elif "power" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Right Now It Has {percentage} Percentage")
        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir We Have {dl} Bit Per Second Downloading Speed And {up} Bit Per Second Uploading Speed")
            # try:
            #     os.system('cmd /k "speedtest')
            #     speak("Done Please Look At The Data")
            # except:
            #     speak("There Is No Internet Connection")
        elif "open my laptop camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows
        elif "i want to chat" in query:
            speak("Ok Let Talk What Do You Want To Talk About")
            chat = command().lower()
            if "quit" in chat:
                speak("Ok I Will Stop This Conversation And Go Back To Work")
                break
            speak(gpt(chat))
        speak("Sir, Can I Help You With Anything Else")
#main
if __name__ == "__main__":
    while True:
        permission = command().lower()
        if "jarvis" in permission or "javit" in permission or "trarvis" in permission or "tarvis" in permission or "charvis" in permission or "travis" in permission:
            s1 = permission
            s2 = 'Call Me Jarvis Not ' + s1
            speak(s2)
            task()
        elif "shut down" in permission:
            speak("Thank You For Using Me Sir")
            sys.exit()
    #command()
    #speak("Hello i am Jarvis, how can i help you?")
