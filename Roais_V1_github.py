import pyttsx3
import os
import pyautogui
from datetime import datetime, timedelta, date, time
import time
import google.generativeai as genai
import shutil
import webbrowser

engine = pyttsx3.init()

engine.setProperty("rate", 200)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  


Main_folder = "D:/Lobby/ROAIS - Main folder"

os.chdir("D:/Lobby")

url = {
    "youtube" : "https://www.youtube.com/",
    "discord" : "https://discord.com/channels/@me",
    "chatgpt" : "https://chatgpt.com/",
    "spotify" : "https://open.spotify.com/?flow_ctx=677341a0-2d0e-4d33-98d8-d5a3f059459d%3A1740164697",
    "video editor" : "https://www.kapwing.com/folder/67cc197053b2a8a51cb73dec",
    "google" : "https://www.google.com"
}

start = ["hi", "hello", "whatsup", "start"]

genai.configure(api_key="")#add your Gemini Api key here

generation_config = {
"temperature": 0,
"top_p": 0.95,
"top_k": 64,
"max_output_tokens": 8192,
"response_mime_type": "text/plain",
}
safety_settings = [
{
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
},
{
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
},
{
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
},
{
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
},
]

model = genai.GenerativeModel(
model_name="gemini-1.5-pro",
safety_settings=safety_settings,
generation_config=generation_config,
system_instruction = "Your name is roais. You  are an helpful ai creted to help the owner. Owner is a 14 year old boy and is interested in learning new things. You are completely created by the owner. Owner name is Suhas. You should also help the owner in esp32, arduino, wiring and programming, Giving information about sensors and help them in creating their own AI assistant. The owner prefers answering in less than 10 lines if they ask any information. When they just ask information, you should not give code. You should only give code, when the owner ask it. If unsure whether to give code or not ask the Owner."
)

chat_session = model.start_chat(
    history=[]
)

def Start():
    print("Roais: Roais V2 activated. Suhas How can I help you today? ")
    engine.say("Roais is activated. Suhas How can I help you today? ")
    engine.runAndWait()

def welcome():
    print("Roais: Hi, Suhas. What will you do today?")
    engine.say("Hi Suhas. What will you do today?")
    engine.runAndWait()

def Exit():
    print("Roais: Exiting")
    engine.say("Exiting")
    engine.runAndWait()
    print("....................")
    time.sleep(0.5)
    print("...........")
    time.sleep(0.5)
    print("....")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    exit()

def Time():
    Time = datetime.now().strftime("%I:%M %p")
    print(f"Roais: Current time: {Time}")
    engine.say(f"Current time is {Time}")
    engine.runAndWait()

def Date():
    Date = datetime.today().strftime("%B %d, %Y")
    print(f"Roais: Today's date: {Date}")
    engine.say(f"Today's date is {Date}")
    engine.runAndWait()

def OpenApp(name):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite(name, 0.05)
    time.sleep(1)
    pyautogui.press('enter')

def FolderCreate(name):
    os.chdir(Main_folder)
    try:
        os.makedirs(name)
        print(f"Roais: Created the folder {name} in main folder")
        engine.say(f"Created the folder {name} in main folder")
        engine.runAndWait()
        print(os.listdir())
    except FileExistsError:
        print(f"Roais: folder {name} already exists")
        engine.say(f"folder {name} already exists")
        engine.runAndWait()

def OpenFile(Filename):
    os.chdir(Main_folder)
    try:
        print(os.listdir())
        print(f"Roais: Opening file {Filename}")
        engine.say(f": Opening file {Filename}")
        engine.runAndWait()
        os.startfile(Filename)
    except FileNotFoundError:
        print(f"Roais: file {Filename} not found")
        engine.say(f"file {Filename} not found")
        engine.runAndWait()

def FolderDelete(name):
    os.chdir(Main_folder)
    print(os.listdir())
    try:
        shutil.rmtree(name)
        print(f"Roais: Deleted the folder {name} in main folder")
        engine.say(f"Deleted the folder {name} in main folder")
        engine.runAndWait()
        print(os.listdir())
    except FileNotFoundError:
        print(f"Roais: folder {name} not found")
        engine.say(f"folder {name} not found")
        engine.runAndWait()
    except NotADirectoryError:
        print("Roais: Invalid format")
        engine.say("Invalid format")
        engine.runAndWait()

def FileCreate(name):
    os.chdir(Main_folder)
    try:
        with open(name, "w") as file:
            file.write("")
            print(f"Roais: Created the file {name} in main folder")
            engine.say(f"Created the file {name} in main folder")
            engine.runAndWait()
            print(os.listdir())
    except FileExistsError:
        print(f"Roais: file {name} alreday exists")
        engine.say(f"file {name} alreday exists")
        engine.runAndWait()

def FileDelete(name):
    os.chdir(Main_folder)
    print(os.listdir())
    try:
        os.remove(name)
        print(f"Roais: Deleted the file {name} in main folder")
        engine.say(f"Deleted the file {name} in main folder")
        engine.runAndWait()
        print(os.listdir())
    except FileNotFoundError:
        print(f"Roais: file {name} not found")
        engine.say(f"file {name} not found")
        engine.runAndWait()
    except NotADirectoryError:
        print("Roais: Invalid format")
        engine.say("Invalid format")
        engine.runAndWait()
    except PermissionError:
        print("Roais: Invalid type")
        engine.say("Invalid type")
        engine.runAndWait()

def Website(web):
    web = web.lower()
    if web in url:
        webbrowser.open(url[web])
    else:
        print(f"Sorry. I dont have access to {web}")
        engine.say(f"Sorry. I dont have access to {web}")
        engine.runAndWait()

def Commands():
    while True:
        commands = input("You: ")
        c = commands.lower().strip().split()

        if not commands:
            continue

        if c[0] in start:
            welcome()

        elif (c[0] == "open" or c[0] == "launch") and len(c) > 1:
            target = " ".join(c[1:2])
            if target in url:
                print(f"Roais: opening {target} website")
                engine.say(f"opening {target} website")
                engine.runAndWait()
                Website(target)
                continue
            elif "file" in c or "folder" in c:
                target = " ".join(c[2:3])
                OpenFile(target)
            else:
                print(f"Roais: Opening {target}")
                engine.say(f"opening {target}")
                engine.runAndWait()
                OpenApp(target)
                continue

        elif c[0] == "create" or c[0] == "new": 
            if len(c) > 2:
                if "folder" in c:
                    folderName = " ".join(c[2:3])
                    FolderCreate(folderName)
                elif "file" in c:
                    file = " ".join(c[2:3])
                    FileCreate(file)
                else:
                    print("Example: *Create Folder abc*")
                    continue
            else:
                    print("Example: *Create Folder abc*")
                    continue
            
        elif c[0] == "delete" or c[0] == "remove":
            if len(c) > 2:
                if "folder" in c:
                    folder = " ".join(c[2:3])
                    FolderDelete(folder)

                elif "file" in c:
                    file = " ".join(c[2:3])
                    FileDelete(file)
                else:
                    print("Example: *Delete folder/file abc*")
                continue
            else:
                print("Example: *Delete folder/file abc*")
                continue

        elif "time" in commands:
            Time()
        
        elif "date" in commands:
            Date()
        
        elif "exit" in commands or "quit" in commands:
            Exit()

        else:
            try:
                response = chat_session.send_message(commands)
                model_response = response.text
                if len(model_response.split(".")) > 5:
                    choice = input("Roais: The response is long. Do you wish to hear it: ")
                    engine.say("The response is long. Do you wish to hear it: ")
                    engine.runAndWait()
                    if choice == "yes":
                        print(model_response)
                        engine.say(model_response)
                        engine.runAndWait()
                    else:
                        print(model_response)
                else:
                    print(model_response)   
                    engine.say(model_response)
                    engine.runAndWait()                     
                        
            except Exception as e:
                print("Roais: I could not handle that right now.")
                engine.say("I could not handle that right now.")
                engine.runAndWait()
                
def LogIn():
    Admin = {'Name': 'Suhas', 'Password': 'SigmaBoy28'}

    while True:
        user = input("Enter the username: ")
        if user == Admin['Name']: 
            print("Welcome, please enter password: ")
            password = input("Enter the password: ")
            
            if password == Admin['Password']:
                print("Verifying......>")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".......")
                time.sleep(0.5)
                print("..............")
                time.sleep(2)
                print("Logged in")
                print(f"Welcome {Admin['Name']}, ROAIS is ready to serve")
                engine.say(f"Welcome {Admin['Name']}, ROAIS is ready to serve")
                engine.runAndWait()
                Commands()
                break
            else:
                print("Wrong password")
                continue
        
        else:
            print("Unknown user, please enter again")
            continue

LogIn()
Start()

while True:
    Commands()
