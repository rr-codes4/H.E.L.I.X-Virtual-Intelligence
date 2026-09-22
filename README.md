# H.E.L.I.X-Virtual-Intelligence
Inspired by sci-fi metas this project brings the iconic JARVIS concept out of the flat screen and straight into physical space but with ULTRON vibe. 
It’s an interactive AI companion that projects a custom holographic interface and responds to voice and system commands in real-time.
It even responds to hand gestures using computer vision and voice commands (voice is like ultron).
# HOW IT WORKS?
**1. Voice Recognition:**
It uses Vosk to process voice commands given by the user.

**2. AI Processing and Logic:**
The transcribed text is sent to a Python backend powered by Meta's Llama hosted by Groq API.
AI parses the request and analyzes it.

**3. Holographic Display (The Hologram):**
I will be using Raspberry Pi LCD Screen a compact HDMI display connected directly to Raspberry pi which will render the 4-way split UI graphics.

Light from the Raspberry Pi LCD screen reflects off a 4-sided pyramidal acrylic sheet placed precisely over the display merging the reflections to create a floating 3D holographic optical illusion in mid-air.

4. Hardware Control & Interaction:
Computer Vision: A USB webcam captures live video frames, using OpenCV and MediaPipe for real-time hand gesture tracking.
Microcontroller Bridge: A USB-connected Arduino handles physical components (like status LEDs or peripheral hardware) triggered via Python serial commands from the Raspberry Pi.

**IMPORTANT**
I have AI(Gemini, Github copilot) for certain code generation to automate and speed up my work and debugging (which took me hours even after using AI) 





