#!/usr/bin/env python3
import sys
import speech_recognition as sr
from os import listdir,path

if(len(sys.argv)<2):
    print("Required input parameter: path of directory with audio files")
    exit()

directory = sys.argv[1] # directory with audio files
r = sr.Recognizer()
file = open("testfile.txt","w") # output file: each line will contain the name of the audio file and the corresponding recognized text

for f in listdir(directory):
    audioFile=path.join(directory,f)
    # use the audio file as the audio source
    with sr.AudioFile(audioFile) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    value=""
    try:
        value="Google thinks you said " + r.recognize_google(audio, None, 'it-IT')
        #value="Sphinx thinks you said " + r.recognize_sphinx(audio, 'it-IT')
        print(value)
    except sr.UnknownValueError:
        value="Sphinx could not understand audio"
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        value="Sphinx error"
    file.write('\n'+f+value)
file.close() 

exit()

