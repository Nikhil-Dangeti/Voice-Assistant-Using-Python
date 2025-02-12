import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib,ssl
import openai_request as ai
import image_generation
import mtranslate
import weather_module
import os
import psutil  # To check running processes
import YouTube_Control
import time

engine=pyttsx3.init()

voices = engine.getProperty('voices')  #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male and 1 for female
engine.setProperty("rate",170)


def speak(audio):
    #translating english to telugu
    #audio=mtranslate.translate(audio,to_language="te",from_language="en-in")
    engine.say(audio)
    engine.runAndWait()
def command():
    content=" "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content=r.recognize_google(audio,language='en-in')
            #for translating telugu language(which we speaks) to english
            content=mtranslate.translate(content,to_language="en-in")
            print("You Said.."+ content)
        except Exception as e:
            print("Please try again..")

    return content

def main_process():
    jarvis_chat=[]
    while True:
        request=command().lower()
        if "hello" in request:
            speak("Welcome, How can i help you.")
        elif "play music" in request:
            speak("Playing music")
            song=random.randint(1,4)
            if song==1:
                webbrowser.open("https://youtu.be/o_u1uo_71-Q?si=xjJNoG4DbP6MCxVU")
            elif song==2:
                webbrowser.open("https://youtu.be/PBQHQ9c-f2k?si=bSju-DrLVyQvP8gs")
            elif song==3:
                webbrowser.open("https://youtu.be/GhXU_FTKNbE?si=UMX5zdKALXAy8D2r")
            elif song==4:
                webbrowser.open("https://youtu.be/91EzD9VgwGk?si=hHCYZeYVXqmzAzOF")
        elif "time" in request:
            now_time=datetime.datetime.now().strftime("%H:%M")
            speak("current time is "+str(now_time))
        elif "date" in request:
            now_date=datetime.datetime.now().strftime("%d:%m")
            speak("current date is "+str(now_date))
        
        elif "exit" in request or "bye" in request:
            speak("Nice to meet you, We will meet again")
            exit()

        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task != "":
                speak("Adding task: " + task)
                with open("D:/python_codeclause/AIBased_VoiceAssisstance/todo.txt", "a") as file:
                    file.write(task + "\n")
                print("Task successfully added to file.")  # Debugging line
        elif "todo list" in request or "to do list" in request or "to do list" in request or "what is my work today" in request:
            try:
                with open("D:/python_codeclause/AIBased_VoiceAssisstance/todo.txt", "r") as file:
                    tasks = file.read().strip()
                    if tasks:
                        speak("Work you have to do today is: " + tasks)
                    else:
                        speak("No tasks found in your to-do list.")
            except FileNotFoundError:
                speak("Task list is empty. You haven't added any tasks yet.")

        elif "my work" in request:
            try:
                with open("D:/python_codeclause/AIBased_VoiceAssisstance/todo.txt", "r") as file:
                    tasks = file.read().strip()
                    if tasks:
                        notification.notify(
                            title="Today's work",
                            message=tasks,
                            timeout=10  # Notification stays for 10 seconds
                        )
                    else:
                        speak("No tasks found in your to-do list.")
            except FileNotFoundError:
                speak("Task list is empty. You haven't added any tasks yet.")

        elif "open" in request:
            query=request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")



        elif "close" in request:
            query = request.replace("close", "").strip()
            process_names = {
                "chrome": "chrome.exe",
                "notepad": "notepad.exe",
                "word": "winword.exe",
                "excel": "excel.exe",
                "powerpoint": "powerpnt.exe",
                "vlc": "vlc.exe"
            }

            if query in process_names:
                process_name = process_names[query]
                
                # Check if the process is running
                if any(proc.name().lower() == process_name.lower() for proc in psutil.process_iter()):
                    os.system(f"taskkill /f /im {process_name}")
                    speak(f"Closing {query}")
                else:
                    speak(f"{query} is not currently running.")
            else:
                speak("Application not recognized. Please try again.")


        elif "wikipedia" in request:
            #request=request.replace("judo","")
            request=request.replace("search wikipedia ","")
            result=wikipedia.summary(request,sentences=2)
            print(result)
            speak(result)

        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
            
        
        elif "search google" in request:
            #request=request.replace("judo","")
            request=request.replace("search google ","")
            webbrowser.open("https://www.google.com/search?q="+request)

        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+910123456789","hi",13,30,30)

        #elif "send email" in request:
         #   pwk.send_mail("nani123@gmail.com",user_config.gmail_password,"Hello","How are you","nani72@gmail.com")
          #  speak("Email Sent")
            
        elif "send email" in request:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("nani@gmail.com",user_config.gmail_password)
            message="How are you"
            s.sendmail("nani123@gmail.com","nani72@gmail.com",message)
            s.quit()
            speak("Email Sent")



        elif "weather" in request:
            speak("Which city's weather do you want?")
            city = command().lower()
            weather_module.speak_weather(city)

    


        elif "play" in request and "video on youtube" in request:
            video_name = request.replace("play", "").replace("video on youtube", "").strip()
            search_url = f"https://www.youtube.com/results?search_query={video_name.replace(' ', '+')}"
            
            webbrowser.open(search_url)  # Open YouTube search results page
            time.sleep(5)  # Wait for the page to load

            # Move cursor to click on the first video
            pyautogui.press("tab", presses=10)  # Navigate to the first video
            pyautogui.press("enter")  # Play the first video
            print(f"Playing {video_name} on YouTube.")

        elif "stop" in request:
            pyautogui.press("space")  # Toggles play/pause on YouTube
            print("Paused/Resumed the YouTube video.")

        elif "close tab" in request:
            pyautogui.hotkey("ctrl", "w")  # Closes the current browser tab
            print("Closed the YouTube tab.")

"""
        elif "weather" in request:
            speak("Which city's weather do you want to know?")
            with sr.Microphone() as source:
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source, duration=1.2)
                print("Listening for city name...")
                audio = r.listen(source)
                city = r.recognize_google(audio)
            weather_info = weather.get_weather(city)
            print(weather_info)
            speak(weather_info)
"""
"""
        elif "ask ai" in request:
            jarvis_chat=[]
            request=request.replace("ask ai","")            
            response=ai.send_request(request)
            print(response)
            speak(response)
        
        elif "clear chat" in request:
            jarvis_chat=[]
            speak("Chat Cleared")

        elif "image" in request:
            request=request.replace("ask ai","")
            image_generation.generate_image(request)
        else:
            
            request=request.replace("jarvis","")            
            jarvis_chat.append({"role": "user","content": request})
            #print(jarvis_chat)
            response=ai.send_request(request)
            jarvis_chat.append({"role": "assistant","content":response})
            #print(jarvis_chat)            
            speak(response)
"""

if __name__ == "__main__":
    main_process()
