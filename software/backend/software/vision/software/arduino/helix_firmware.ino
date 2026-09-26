/*
  H.E.L.I.X Firmware - Arduino Nano
  controls Status LEDs based on commands from Raspberry Pi (Python)
*/

// Define LED Pins (matches architecture diagram)
const int statusLED_Listen = 8;    // Green LED for Vosk listening
const int statusLED_Process = 9;   // Blue LED for LLaMA processing
const int statusLED_Speak = 10;    // Red LED for TTS output

void setup() {
  // Start Serial Communication at 9600 baud (must match main.py)
  Serial.begin(9600);
  
  // Set LED pins as outputs
  pinMode(statusLED_Listen, OUTPUT);
  pinMode(statusLED_Process, OUTPUT);
  pinMode(statusLED_Speak, OUTPUT);

  // Initialize LEDs OFF
  digitalWrite(statusLED_Listen, LOW);
  digitalWrite(statusLED_Process, LOW);
  digitalWrite(statusLED_Speak, LOW);
}

void loop() {
  // Check if a serial command is available from main.py
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the command (e.g., 'L', 'P', 'S')
    
    // Process commands and control LEDs (or other hardware)
    if (command == 'L') { // Listening state
      digitalWrite(statusLED_Listen, HIGH);
      digitalWrite(statusLED_Process, LOW);
      digitalWrite(statusLED_Speak, LOW);
    } 
    else if (command == 'P') { // Processing state
      digitalWrite(statusLED_Listen, LOW);
      digitalWrite(statusLED_Process, HIGH);
      digitalWrite(statusLED_Speak, LOW);
    } 
    else if (command == 'S') { // Speaking state
      digitalWrite(statusLED_Listen, LOW);
      digitalWrite(statusLED_Process, LOW);
      digitalWrite(statusLED_Speak, HIGH);
    } 
    else if (command == 'X') { // Idle state / Error
      digitalWrite(statusLED_Listen, LOW);
      digitalWrite(statusLED_Process, LOW);
      digitalWrite(statusLED_Speak, LOW);
    }
  }
}
