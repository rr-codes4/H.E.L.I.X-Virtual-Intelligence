import os
import sys
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

MODEL_PATH = "model"
if not os.path.exists(MODEL_PATH):
    print(f"Error: '{MODEL_PATH}' folder not found. Make sure your unzipped Vosk model is named 'model'.")
    sys.exit(1)

audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    """Callback function to push audio blocks into the processing queue."""
    if status:
        print(f"Audio Warning: {status}", file=sys.stderr)
    audio_queue.put(bytes(indata))

print("Initializing Vosk Engine...")
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

print("\n[HELIX VOICE ENGINE ONLINE] Speak into your mic (Press Ctrl+C to stop)...\n")

try:
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip()
                if text:
                    print(f"HELIX Heard: -> '{text}'")
            else:
                
                partial_res = json.loads(recognizer.PartialResult())
                partial = partial_res.get("partial", "").strip()
                if partial:
                    print(f"Listening... {partial}\r", end="")

except KeyboardInterrupt:
    print("\n[HELIX VOICE ENGINE OFFLINE]")
except Exception as e:
    print(f"\nError starting audio stream: {e}")