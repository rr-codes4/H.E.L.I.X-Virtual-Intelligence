# NOTE: The Block Diagram is AI generated but the idea and formatting is mine.

**Project HELIX — Hardware Architecture & Signal Flow**

This document details the physical components, signal routing, power distribution, and hardware interface layout for the **HELIX Holographic AI Assistant**.
This diagram is only for rough understadning of the working of the model.
---

## 🏗 System Block Diagram

```text
=================================================================================
                            HELIX HARDWARE ARCHITECTURE
=================================================================================

 [ 12V 2A Power Adapter ]
            |
            v
 +------------------------+    LVDS Ribbon Cable    +---------------------------+
 | LCD HDMI DRIVER BOARD  |========================>| RECYCLED LAPTOP LCD SCREEN|
 +------------------------+                         | (14.5"-15" Display Base)  |
            ^                                       +---------------------------+
            | HDMI Cable                                          |
            v                                                     v
 +-------------------------------------------------------------------------------+
 |                        RASPBERRY PI (MAIN PROCESSOR)                          |
 |                                                                               |
 |  • Vosk Voice Recognition (STT)      • Groq API (Meta Llama LLM Engine)     |
 |  • OpenCV + MediaPipe Gesture Engine • Python Serial Controller               |
 +-------------------------------------------------------------------------------+
     |                    |                     |                     |
     | USB                | USB                 | USB                 | USB (Serial)
     v                    v                     v                     v
+------------+      +------------+        +-----------+         +------------------+
| USB WEBCAM |      |  USB MIC   |        |  SPEAKER  |         | ARDUINO (BRIDGE) |
|(Gesture CV)|      |(Voice In)  |        |(Audio Out)|         +--------+---------+
+------------+      +------------+        +-----------+                  |
                                                                         v
                                                                +------------------+
                                                                | STATUS LED RING  |
                                                                |  (RGB / Neopixel)|
                                                                +------------------+
