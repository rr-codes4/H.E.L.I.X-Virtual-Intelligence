# H.E.L.I.X-Virtual-Intelligence
Inspired by sci-fi metas this project brings the iconic JARVIS concept out of the flat screen and straight into physical space but with ULTRON vibe(robotic and cold). 
It’s an interactive AI companion that projects a custom holographic interface and responds to voice and system commands in real-time.
It even responds to hand gestures using computer vision and voice commands.
But I have used lightweight models which might reduce the quality of reasoning,visual and performance. Doing so would let this project run of low level laptops.
# HOW IT WORKS?
**1. Voice Recognition:**
It uses Vosk to process voice commands given by the user.

**2. AI Processing and Logic:**
The transcribed text is sent to a Python backend powered by Meta's Llama hosted by Groq API.
AI parses the request and analyzes it.

**3. Holographic Display (The Hologram):**
I planned to use Raspberry pi LCD display but dropped the idea because it will just restrict the hologram to roughly 2.5 cm.
Instead I decided to make this project more impactful , I will be using 15.6 inch HDMI display that could give me a larger hologram display and more easier to interact with it.

4. Hardware Control & Interaction:
Computer Vision: A USB webcam captures live video frames, using OpenCV and MediaPipe for real-time hand gesture tracking.
Microcontroller Bridge: A USB-connected Arduino handles physical components (like status LEDs or peripheral hardware) triggered via Python serial commands from the Raspberry Pi.

**IMPORTANT**
I have used AI(Gemini, Github copilot) for certain code generation that automated and sped up my work and also for debugging (which took me hours even after using AI) 

I have uploaded screeshots of my CAD and one more CAD with Hardwares

![CAD Front View](./software/cad/Isometric_view.png)
![CAD Side View](./software/cad/front_view.png)





