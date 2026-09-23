import pyttsx3

def speak(text: str):
    """Speaks text out loud cleanly using pyttsx3."""
    if not text:
        return
    
    print(f"\n[HELIX]: {text}\n", flush=True)
    
    try:
        # Re-initialize engine per call to prevent Windows SAPI5 audio locks
        engine = pyttsx3.init() #My Laptop is a bit jerky so initializing fresh engine instance would not let windows audio freeze
        engine.setProperty('rate', 160)#160 words per minute :]
        engine.say(text)#Speaking the text
        engine.runAndWait()#running the engine and waiting for it to finish...
        engine.stop()#Stooping the engine to free up audio resources for the next call
    except Exception as e:
        print(f"[TTS ERROR]: Failed to play voice output: {e}")

if __name__ == "__main__":
    speak("Text-to-speech engine operational.")


