#imprting all modules use in my project
import speech_recognition as sr
import webbrowser
import pyttsx3
import pygame
import os
import time
from gtts import gTTS

import musiclibrary

#initializing speech recognizer

r=sr.Recognizer()

#speak function

def speak(text):
    #convert text into speech using gtts
    #then play mp3 with pygame
    #we add small pauses between sentences to sound more human

    #split text into sentences with short pause
    sentences =text.split(". ")
    for sentence in sentences:
        if not sentence.strip():
            continue

        #convert sentence to audio
        tts = gTTS(text=sentence, lang='en')
        tts.save("temp.mp3")

        #initiaize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load("temp.3")
        pygame.mixer.music.play()

        #wait until playback is finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

        os.remove("temp.mp3") # removing the temporary file

        time.sleep(0.5) # pause briefly between sentences

def processCommand(c):

    #this is gonna handel recognized speech command and perform function a/c to command
    c_lower=c.lower()

    if "open google" in c_lower:
        speak("sure maryam .i am opening google for you...")
        webbrowser.open("https://google.com")
    elif "open youtube" in c_lower:
        speak("sure maryam .i am opening youtube for you...")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c_lower:
        speak("sure maryam .i am opening facebook for you...")
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c_lower:
        speak("sure maryam .i am opening linkedin for you...")
        webbrowser.open("https://linkedin.com")

    elif c_lower.startswith("play"):
        #now processing for playing songs if user say play
        try:
            song_name=c_lower.split(" ",1)[1]
            if song_name in musiclibrary.music:
                speak(f"i am playing {song_name} for you maryam...enjoy!")
                webbrowser.open(musiclibrary.music[song_name])
            else:
                speak("sorry  maryam i don't have that music in my library")
        except IndexError:
            speak('''please specify a song name for example
                long time no see
                sometimes
                ''')
    elif "exit" in c_lower or "stop" in c_lower:
        speak("goodbye maryam have a wonderfull day")
        #exit the script
        raise SystemExit 
    else:
        speak("i did't understand the command please try again")


# MAIN LOOP

if __name__=="__main__":
    speak("initializing JARVIS ..waiting for the wakeup word.")

    while True:
        #continusly listen for wakeup word
        try:
            with sr.Microphone() as source:
                print("listening for wake word")
                audio=r.listen(source,timeout=3,phrase_time_limit=2)

                #convert speech to text
                word=r.recognize_google(audio)
                print(f"you said{word}")
                 # Check if user said "Jarvis"
            if word.lower() == "jarvis":
                # Greeting with short pauses
                speak("Hey Maryam. Hope you're doing great. What's on your mind today. I am here to help.")
                # Now wait for the actual command
                with sr.Microphone() as source:
                    speak("Yaaa")
                    audio_cmd = r.listen(source)
                try:
                    command=r.recognize_google(audio_cmd)
                    print(f"command recognized{command}")

                    #passing the command to function to work further
                    processCommand(command)
                except Exception as e:
                    speak("sorry i did't found that.")
        except sr.WaitTimeoutError:
            #if no speech detected just continue the loop
            continue
        except sr.UnknownValueError:
            #could not understand audio
            continue
        except sr.RequestError as e:
            speak("sorry i am having trouble connecting")
        except SystemExit:
            #exit gracefully
            break
        except Exception as e:
            print(f" An unexpected error {e} has occured")

