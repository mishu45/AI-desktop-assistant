import webbrowser

import speech_recognition as sr
import os
import win32com.client
import wikipedia
import openai
from config import apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def chat(query):


def ai(prompt):
    openai.api_key = apikey
    text =f"OpenAI response for {prompt}\n ***************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="",
        temperature=0.7,
        max_token=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0

    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('AI')[1:]).strip()}.txt","w") as f:
        f.write(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio =r.listen(source)
        try:
            # print("Recognizing")

            query = r.recognize_google(audio, language = 'en-in')
#            print("listened ")
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


# Press the green button in the gutter to run the script.
def say(text):
    os.system(f'say "{text}"')


if __name__ == '__main__':

    s = "Hello I am Jarvis A.I. How may I help you today?"
    speaker.Speak(s)
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com/"], ["google","https://google.com"], ["wikipedia","https://wikipedia.com"]]
        speaker.Speak("Opening...")
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

    if "using AI ".lower() in query.lower():
        ai(prompt=query)

    elif "sleep".lower() in query.lower():
        exit()
    else:
        chat(query)



