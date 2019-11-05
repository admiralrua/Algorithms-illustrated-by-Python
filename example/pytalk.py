"""
from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("gm.mp3")
"""

from random import randint
from time   import sleep
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")

with open("wordlist.txt") as f:
    wordlist = []
    for line in f:
        wordlist.append(line.strip())

nword = len(wordlist)-1      
times = 5

for i in range(times):
    value = randint(0, nword)
    speak.Speak(wordlist[value])
    sleep(2)