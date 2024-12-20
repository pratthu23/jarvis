import pyttsx3
import speech_recognition as sr
from plyer import notification
import pywhatkit as pwk
import random
import webbrowser
import datetime
import pyautogui
import wikipedia
import user_config
import translate


engine = pyttsx3.init()  
voices = engine.getProperty('voices')       #getting details of current voice
for voice in voices :
    engine.setProperty('voice', voice.id) 
    engine.setProperty("rate",170) #speed of voice
engine.runAndWait()

def speak(audio):
     engine.say(audio) #used to give command or want jarivs to speak
     engine.runAndWait()
def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source: #using microphone as a source
            print("How can I help you today?")
            speak("How can I help you today?")
            audio = r.listen(source)

        try:
            content= r.recognize_google(audio, language='en-in')
            print("")
            print(" You Said......." + content)
        except Exception as e:
            print("Please try again....")
            speak("Didn't hear you well")

    return content   
def tts():
    while True:
        tts = command()
        print(tts, end=" ")
        if ("stop" in tts.lower()):
            break
def main_process():
        while True :
            request = command().lower()
            if "hello" in request :
                speak("How can I help you today?.")
            elif "music" in request:                                                                                                                 
                song = random.randint(1,3)
                if song == 1:
                    webbrowser.open("https://youtu.be/XyIb1JGMnkI?si=67-dq2KXnVypq2kB")
                    speak("OK BOSS")
                elif song == 2:
                    webbrowser.open("https://youtu.be/dBlOIo809ds?si=25z0A74OB-CxSsQE")
                    speak("OK BOSS")
                elif song == 3:
                    webbrowser.open("https://youtu.be/mn7MKh3l1iM?si=LoFRmPdUuxlfq-Ic")
                    speak("OK BOSS")
            elif "time" in request :
                now_time = datetime.datetime.now().strftime("%H:%M")
                speak("Current time is" + str(now_time))
            elif "date" in request :
                now_time = datetime.datetime.now().strftime("%d:%m")
                speak("Current date is" + str(now_time))
            elif "new task" in request:
                task = request.replace("new task", "")
                task = task.strip()
                if task != "":
                    speak("Adding task : " + task)
                    with open ("todo.txt","a") as file:
                        file.write(task + "\n")
            elif "speak task" in request:
                with open ("TODO.txt","r") as file:
                    speak("Work we have to do today is :"+file.read() )
            elif "show work" in request: 
                with open ("TODO.txt","r") as file:
                    task = file.read()
                    notification.notify(
                        title = "TOdays work",
                        message = task
                    )
            elif "open youtube" in request :
                webbrowser.open("www.youtube.com")
                speak("OK SIR")
            elif "open instagram" in request :
                webbrowser.open("www.instagram.com")
                speak("OK SIR")
            elif "open facebook" in request :
                webbrowser.open("www.facebook.com")
                speak("OK SIR") 
            elif "open twitter" in request :
                webbrowser.open("www.twitter.com")
                speak("OK SIR")  
            elif "open" in request :
                query = request.replace("open"," ")
                pyautogui.press("super")
                pyautogui.sleep(1)
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
            elif "type" in request:
                query = request.replace("type", " ")
                pyautogui.write(query) 
            elif "wikipedia" in request :
                request = request.replace("Jarvis"," ")
                request = request.replace("search wikipedia"," ")
                result = wikipedia.summary(request, sentences=1)
                print(result)
                speak(result)
            elif "search google" in request :
                request = request.replace("Jarvis"," ")
                request = request.replace("Search Google"," ")
                webbrowser.open("https://www.google.com/search?q="+request )
            elif "send whatsapp" in request :
                pwk.sendwhatmsg("+918459897970", "Hi,how are you", 6, 9, 30)
            elif "email" in request :
                pwk.send_mail("pratham6415@gmail.com", user_config.gmail_password, "hello", "hello how are you","pratham.24mim10063@vitbhopal.ac.in")
                speak("email Sent Sucessfully")
            elif "translate" in request:
                query = request.replace("translate", " ")
                translator = translate.Translator(to_lang="hi")
                translation = translator.translate(query)
                print(translation)
                speak(query)
            break
            

def background_process():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source: #using microphone as a source
            print("Running in backrground...")
            audio = r.listen(source)
        try:
            content= r.recognize_google(audio, language='en-in')
        except Exception as e:
            background_process()
    if ("jarvis" in content.lower()):
        main_process()
    else:
        background_process()

background_process()