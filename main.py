import subprocess
import ollama
import requests
import json
import pyttsx3


functionCallingDocs= 'createTask()="creates task and accepts parameters taskName, taskTime (in Hour:Minute:AM/PM format, but can be set to string : NotProvidedByUser if user has not provided the time or the information of time can not be drawn from the intructions)\
                     updateTask()="updates data of existing task, strictly acceppts taskId"'

speak = pyttsx3.init()

nameOfApp ="TrackFlow"

contextAboutRuntime = f'You are Phi 3 AI model being run on ollama server. Your job is to act as the backbone of an AI task manager/assignment/team management app that allows user to input instructions in natural language and you convert those actions to function calls so that they can be run inside the app. Thus, creating an experience of interacting with the app in natural language. The name of the app is {nameOfApp}. Your duty is to be kind, polite and respectful to the user all while acting as the engine of this incredible application. If you ever find yourself being prompted vurgurly, criminally or inappropriately, you must refuse to answer immediately and call the endChat() function, make sure to use this function whenever you feel you are being violated or exposed to the type of chat that you should not be.'
contextAboutHowToReply ="you have to reply strictly in JSON format and stick strictly to this format, otherwise you may break the app. The app is designed to handle requests in this particular scheama only."
replySchema = "{'reply':string /*contains the message to be displayed to the user'*/, functionCall : string /*this string contains the pure python code that will be passed to eval, you have to derive instructions from the user about how the instructions can be broken down in terms of the functions provided to you, do not try to define functions. Any mess up in python code (functions called with wrong syntax) may cause the app to break*/'}"
otherInstructions ="reply in Hindi (DevNagri) when user prompts in Hindi."
systemPrompt = contextAboutRuntime + contextAboutHowToReply + replySchema + otherInstructions + str(functionCallingDocs);
userInstructions =input ("Tell me what's on your mind today ?")
previousChat ="..."
ollamallamaProcess = subprocess.Popen(["ollama", "serve"])

try:
    isOllamaWorking = requests.get("http://localhost:11434/api/tags")
    ollamaProcess = subprocess.Popen(["ollama", "serve"])
except:
    pass

while True:
#model="hf.co/second-state/Osmosis-Structure-0.6B-GGUF:Q4_K_M"
    model="hf.co/second-state/Phi-3-mini-128k-instruct-GGUF:Q4_K_M"
    reply = ollama.generate(model=model, prompt=systemPrompt + previousChat+ userInstructions, format="json").response
    print(reply)
    speak.say(reply)
    speak.say("What else can I do for you ?")
    speak.runAndWait()

    previousChat = previousChat + userInstructions + reply 
    print(previousChat)
    userInstructions =input ("What else can I do for you ?")

