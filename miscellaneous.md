# Miscellaneous

## Text-to-speech with Python
A friend of mine taking an English course asked me if it is hard to write a Python script to read-out-loud a list of his learning word list in a random order. It turns out that with just a couple of code line, we can easily do it in the Windows OS computer. This section briefly describes how to do that and provides a piece of code for illustration. 

The code based on Speech API in the Windows OS. To invoke this API from Python, this code will help you:

```python
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
speak.Speak("Hello World!")
```

Now the rest is only reading the wordlist from a text file into a [list of word](/example/wordlist.txt), generating a random number and choosing a corresponding word to read-out-loud, and dont forget to have a little bit pause between reading two consecutive words. 

```python
from random import randint
from time   import sleep
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")

with open("wordlist.txt") as f:                 # read the wordlist file
    wordlist = []
    for line in f:
        wordlist.append(line.strip())           # each line is considered as a word to be read, it can also be a sentence
 
nword = len(wordlist)-1      
times = 100                                     # number of words to be read

for i in range(times):
    value = randint(0, nword)                   # generate a random number -> VALUE
    speak.Speak(wordlist[value])                # take a word at location VALUE to be read 
    sleep(2)                                    # delay 2s before reading the next word
```

In that code, each line in the wordlist file contains a word. If each line contains a sentence then a sentence is read instead. You can play around more with the Speech API such as volume, voices, reading rate.... Please refer to the homepage of the engine [here](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ee125077\(v=vs.85\)) for more information.
