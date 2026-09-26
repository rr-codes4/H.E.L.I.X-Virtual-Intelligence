import sys
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import numpy as np
#The programme will capture the live voice feed the voice into vosk and processes the audio into text strings.
#:)
try:
    model = Model(lang="en-us") #Initially i wrote in my code to check if a file named as model exist and it wasn't working
    #So copilot used this to bypass every file error:) It is important for speech to text conversion
except Exception as e:
    print(f"Error loading Vosk model: {e}")
    sys.exit(1)

recognizer = KaldiRecognizer(model, 16000) #setting up the frequency at 16000 Hz

def listen_for_speech() -> str:
    """Captures user speech and returns transcribed text string."""
    audio_queue = queue.Queue()

    def audio_callback(indata, frames, time, status): #It will all the time in my background everytime my microphone records something

        audio_queue.put(bytes(indata)) #Convert to bytes and put in queue      

    # The stream closes automatically when exiting the 'with' block,
    # freeing up audio hardware for pyttsx3 to speak cleanly!
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        while True: 
            try:
                data = audio_queue.get(timeout=0.5)
            except queue.Empty:
                continue
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                if text:
                    return text
            else:
                partial_result = json.loads(recognizer.PartialResult())
                if partial_result.get("partial"):
                    pass 
        

        #YAyyyyyy!