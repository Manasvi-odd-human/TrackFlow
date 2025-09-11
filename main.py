import subprocess
import ollama
import requests
import json
import pyttsx3
import tkinter as tk
import csv
import datetime as dt
import datetime
import os
import pandas as pd

speak = pyttsx3.init()

presentTime ="Present time is " + str(dt.datetime.now())
 #Storing, fetching and organizing data in data.csv

def addEvent(eventDataAsList, dataFrame):
    event = pd.DataFrame([eventDataAsList])
    dataFrame = pd.concat(data, event, ignore_index=True)
    dataFrame.to_csv(data, ignore_index=True)

def markCompleted(eventId, data=pd.read_csv("data.csv")):
    mask = data["eventId"]==eventId
    if not mask.any():
        print("Data not found")
    else :
        data.loc[mask, 'isCompleted'] = True
        data.to_csv("data.csv", index=False)

def updateEvent(eventDetails):
    data=pd.read_csv("data.csv")
    mask = data["eventId"]==eventDetails[0]
    if not mask.any():
        print("Data not found")
    else :
        data.loc[mask, "title"]=eventDetails[1]
        data.loc[mask, "time"]=eventDetails[2]
        data.loc[mask, "isCompleted"]=eventDetails[3]
    data.to_csv("data.csv", index=False)

def deleteEvent(eventId):
    data=pd.read_csv("data.csv")
    indexToRemove = data.index[data["eventId"]==eventId]
    data = data.drop(index=indexToRemove)
    data.to_csv("data.csv", index=False)

#check if data.csv exists and load it, or create it and load it
if not os.path.exists("data.csv"):
    file = open("data.csv", mode="w")
    file.write("eventId, title, time, isCompleted")

else:
    file = "data.csv"
    data = pd.read_csv(file)
    print(data)
    

# functionCallingDocs= 'createTask()="creates task and accepts parameters taskName, taskTime (in form of datetime python library object, but can be set to string : NotProvidedByUser if user has not provided the time or the information of time can not be drawn from the intructions)\
#                      updateTask()="updates data of existing task, strictly acceppts taskId"'


# nameOfApp ="TrackFlow"

# contextAboutRuntime = f'You are Phi 3 AI model being run on ollama server. Your job is to act as the backbone of an AI task manager/assignment/team management app that allows user to input instructions in natural language and you convert those actions to function calls so that they can be run inside the app. Thus, creating an experience of interacting with the app in natural language. The name of the app is {nameOfApp}. Your duty is to be kind, polite and respectful to the user all while acting as the engine of this incredible application. If you ever find yourself being prompted vurgurly, criminally or inappropriately, you must refuse to answer immediately and call the endChat() function, make sure to use this function whenever you feel you are being violated or exposed to the type of chat that you should not be.'
# contextAboutHowToReply ="you have to reply strictly in JSON format and stick strictly to this format, otherwise you may break the app. The app is designed to handle requests in this particular scheama only."
# replySchema = "{'reply':string /*contains the message to be displayed to the user'*/, functionCall : string /*this string contains the pure python code that will be passed to eval, you have to derive instructions from the user about how the instructions can be broken down in terms of the functions provided to you, do not try to define functions. Any mess up in python code (functions called with wrong syntax) may cause the app to break*/'}"
# otherInstructions="Always enter date time in form of a datetime object as per datetime library of python"
# systemPrompt = contextAboutRuntime + contextAboutHowToReply + replySchema + otherInstructions + str(functionCallingDocs) + presentTime
# userInstructions =input ("Tell me what's on your mind today ?")
# previousChat ="..."
# ollamallamaProcess = subprocess.Popen(["ollama", "serve"])

# try:
#     isOllamaWorking = requests.get("http://localhost:11434/api/tags")
#     ollamaProcess = subprocess.Popen(["ollama", "serve"])
# except:
#     pass

# while True:
# #model="hf.co/second-state/Osmosis-Structure-0.6B-GGUF:Q4_K_M"
#     model="hf.co/second-state/Phi-3-mini-128k-instruct-GGUF:Q4_K_M"
def TalkToAI():
    reply = ollama.generate(model=model, prompt=systemPrompt + previousChat+ userInstructions, format="json").response
    return reply
#     print(reply)
#     replyInJson = json.loads(reply)
#     eval(replyInJson["functionCall"])
#     speak.say(reply)
#     speak.say("What else can I do for you ?")
#     speak.runAndWait()

#     previousChat = previousChat + userInstructions + reply 
#     print(previousChat)
#     userInstructions =input ("What else can I do for you ?")

# UI code


# root = tk.Tk()
# root.title("TrackFlow")
# root.geometry("1080x720")
# trackFlowLogoText = tk.Button(root, text="TrackFlow", command=HandleClick(action="print", id="1"))
# trackFlowLogoText.pack( padx=30, pady=20)

# root.mainloop()