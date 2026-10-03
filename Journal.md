# Helix : Hardware planning, CAD Optimization
# September 28, 2026

2 hours
H.E.L.I.X is an interactive virtual intelligence assistant combined with holographic display (inspired by J.A.R.V.I.S) with local voice processing and hand gestures recognition.

##CHALLENGES : Working on low-end Laptop with integrated graphics resulted in crashes and freezing.

##SOLUTION: Made lightweight CAD model on Onshape focused strictly on physical accuracy.

ASSEMBLY (CHASSIS): The base box is to represent the frame and LCD screen, 4 pillars for support, the pyramid for the acrylic pyramid sheet for the Pepper's Ghost effect. HARDWARE COMPONENTS : A 15.6-inch screen for the display, Arduino Nano (Microcontroller) for hardware triggers and controlling status LED connected to Raspberry, USB webcam, Rapsberry Pi 4/5 runs the python backend , USB microphone & speakers/audio apators,M5x40 Flathead Bolts & M5 Hex Nuts 16 sets for assembling all parts.

I did the best to find and these parts and make the model before my laptop crashes again

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/0c3f72d1-8e17-457f-8b0c-7bef45867f4c" />


# Bringing Helix to life
# Oct 1 2026
2 hours 43 min
The first task was to prepare the main backend for the project. 
![Screenshot_16_.png](https://cdn.hackclub.com/01a0f7ea-80ce-7bdf-883c-463382e7df30/Screenshot_16_.png)

The first step was API calling. I used Groq's open source API. Due to a stupid mind of mine I forgot to set up my API locally. Well, 2 hours for debugging is just hyperbole; it was not that long. I used GitHub Copilot to debug and see what is happening. I used DuckDuckGo search for Helix to fetch live news. You don't need an API to use DuckDuckGo.

Next up: giving Helix a personality , setting up DuckDuckGo news search
![Screenshot_17_.png](https://cdn.hackclub.com/01a0f7ef-a853-7cc0-8190-2b3ee729c15a/Screenshot_17_.png)

![Screenshot_19_.png](https://cdn.hackclub.com/01a0f7f2-4f3d-7ec6-941d-a9f450ed8b9f/Screenshot_19_.png)
Using a low level model hosted by Groq was a good idea for my Low end Laptop, it was already hanging.
query_helix(user_text)--The brain: time.perf_counter() measures how much time AI takes to think,printing response latency.Sends my spoken text along with the persona of Helix defined above to an LLM endpoint (using Me.chat.completion.create with a model like openai/gpt-oss-120b).If API call fails it handles it gracefully instead of crashing out.

Next up , making Helix hear things
![Screenshot_20_.png](https://cdn.hackclub.com/01a0f7f6-3954-77ed-bf4e-4d7f1fcd6610/Screenshot_20_.png)

I used Vosk again a low level model , which reduces the quality of reasoning but increases the speed of response. This programme decides the pace or say tone of helix's voice.listen_for_speech() instead of running forever in the background,this wraps the listener into a function and waits for us to speak,captures one full sentence and returns it as a string. Added a timeout to prevent the queue from locking up indefinitely.with sd.RawInputStream(...) block makes the stream close automatically when the function returns text or finishes. Releases Windows audio hardware instantly and allowing the pyttsx3 engine to speak without freezing.

![Screenshot_21_.png](https://cdn.hackclub.com/01a0f7ff-3699-70d3-9162-fe0c02c5a2d1/Screenshot_21_.png)
This is important while using Vosk model as Vosk is an open-source, offline speech recognition toolkit. It captures audio and transcribes it into written text.But it cannot synthesize voice or speak back to the user. Adding text-to-speech eliminates this issue. Pairing vosk with pyttsx3  makes a fully conversational AI assistant.The speak function takes the text string as input and if its empty it exits immediately.Else the code is explained in the screenshot itself with my comments.

![Screenshot_22_.png](https://cdn.hackclub.com/01a0f804-de6e-7783-b04f-a7aebade4cdf/Screenshot_22_.png)

This looks for the unzipped Vosk speech model, if the folder is missing it returns an error,in case the file is accidentally deleted I will know it. Initialized Vosk and set up Kaldirecognizer . Setting up a thread-safe queue.Queue() to bridge audio input stream and recognition loop.To prevent lagging the audio_callback function grabs the raw audio block from my microphone and pushes into the queue.Queue().Opens raw input stream and pull raw audio chunks from the queue.When Vosk detects a sentence (recognizer.AcceptWaveform(data) returns True) it extracts the text from the JSON output and prints: HELIX Heard: -> '[text]'.While I am still speaking it fetches real-time partial transcriptions (recognizer.PartialResult()) and updates the console dynamically on a single line (Listening... [partial text]).try...except KeyboardInterrupt ensure Helix stops on pressing ctrl+C.


# Helix Firmware
# Oct 2 2026
4min
Setting up a physical status indicator in Helix.
I don't have C++ experience so I had to use AI for it.
But I understood the workflow and here it is
![Screenshot_23_.png](https://cdn.hackclub.com/01a0fb19-35ca-74b1-b719-ec77f1a6e729/Screenshot_23_.png)
![Screenshot_24_.png](https://cdn.hackclub.com/01a0fb1a-7df9-7d4d-9a84-520fe89f1e26/Screenshot_24_.png)
Pin Mapping(setup):Defines three different pin for RGB/seperate status LED's , Pin 8 (Green for listening) Pin 9 (Blue for processing/thinking) and Pin 10 (Red for speaking).Initializes 6900 baud serial communication for talking back and forth for Raspberry Pi.

Serial Command Listener (loop): The Arduino Nano continuously check if Raspberry Pi has sent a character over serial Serial.available() > 0. Based on the character received it will toggle the appropriate LED ON while turning others OFF 
'L': Turns on the Green LED (Vosk is listening).

'P': Turns on the Blue LED (LLM is processing).

'S': Turns on the Red LED (TTS is speaking).

'X': Turns OFF all LEDs (Idle/Reset state).

# Giving Helix eyes
# Oct 2 2026
24min
![Screenshot_25_.png](https://cdn.hackclub.com/01a0fb35-0388-7de6-9b87-6298900c8bfe/Screenshot_25_.png)
![Screenshot_26_.png](https://cdn.hackclub.com/01a0fb3e-f08c-760a-8f6e-ed1de880a2ae/Screenshot_26_.png)
The HandTracker Class: MediaPipe initialization, setting up mp.solutions.hands--> this sets up rules tracking maximum of one hand(max_hands=1) 
self.mp_draw = ...----> Loads drawing tools to map skeleton on hand
cv2.cvtColor -----> Converts camera default BGR into RGB MediaPipe requires RGB.
self.hands.process-----> Finding HAnds
If hands are found it makes joint connection lines onto the video frame and we will see hand skeleton on screen!
landmarks[8].y < landmarks[6].y----> Using some maths...Plotting coordinates.Compares the tip of your index finger (Landmark 8) with its middle joint (Landmark 6).Since CV coordinates start from y=0 a smaller y-coordinate means the finger is higher means POinting_up

![Screenshot_27_.png](https://cdn.hackclub.com/01a0fb43-ab8b-78c3-9ea2-a1c77f14cd4c/Screenshot_27_.png)
Function main is the main loop
cv2.VideoCapture(0)---> connects to primary USB webcam
while cap.isOpened()----> captures video frame one-by-one
if gesture spotted [H.E.L.I.X Gesture] Detected: POINTING_UP printed.
cv2.imshow---> Displays live stream titled "H.E.L.I.X Vision Stream"
ord('q')---> ON pressing q on my keyboard the camera is released and all windows closed.
![Screenshot_28_.png](https://cdn.hackclub.com/01a0fb43-e3d0-714b-bee0-99d1efaaf0be/Screenshot_28_.png)

# Debuggin with the help of AI
# Oct 2 2026
28min
![Screenshot_29_.png](https://cdn.hackclub.com/01a0fb4c-cac2-7648-8622-279d776b37d3/Screenshot_29_.png)

Faced many issues that need to be fixed. Sometimes the problem is right in front of you and you can't fix it. 
I used GitHub Copilot it fixed the API key error and Model not found error that I was getting even after downloading the zipped folder and adding unzipped one in vscode.Basically the programme was not able to recognize the model folder.AI fixed , changed the code.
# Hardware Architecture & Schematic Overview
# Oct 3 2026
1 hour
To ensure reliable multi-voltage communication for Helix project,the schematic integrates Raspberry pi and Arduino Nano.

Safe Logic Level Translation: Because the Raspberry Pi 5 is 3.3V logic and the Arduino Nano is 5V, we cannot cross wire the data lines. We have a 4 channel logic level shifter (U4) that takes care of the voltage conversion:

High voltage rail (VCC1) is powered from 5V.

Low voltage rail (VCC2) is referencing the Pi 5 board 3.3V power pin (Pin 1).

Serial UART Data: Bi-directional serial data communication is established across the level shifter between the Arduino Nano (D0/RX, D1/TX) and the Pi 5 GPIO UART pins (GPIO14/TXD, GPIO15/RXD).

Common Reference Ground: A common reference ground connects everything, the Raspberry Pi 5, Arduino Nano, the level shifter (VEE) and the indicators.
![Screenshot_39_.png](https://cdn.hackclub.com/01a10080-c66f-715d-bf0f-5d3f8d7440cf/Screenshot_39_.png)



