# NOTE: The Block Diagram is AI generated but the idea and formatting is mine.

**Project HELIX — Hardware Architecture & Signal Flow**

This document details the physical components, power distribution, and hardware interface layout for the **HELIX Holographic AI Assistant**.
This diagram is only for rough understanding of the working of the model.
---

## 🏗 System Block Diagram

```text
=================================================================================
                            HELIX HARDWARE ARCHITECTURE
=================================================================================

+-------------------------------------------------------------------+
|                        HOST MACHINE                               |
|                  (Acer Laptop / Raspberry Pi)                     |
+-------------------+----------------------------+------------------+
                    |                            |
          (HDMI Video Out)               (USB Data & Power)
                    |                            |
                    v                            v
  +-----------------------------------+  +--------------------------+
  |  15.6" / 10.1" HDMI DISPLAY       |  |  ARDUINO NANO            |
  |  (Pepper's Ghost Optical Visuals) |  |  (Lighting & Sensors)    |
  +-----------------------------------+  +------------+-------------+
                                                      |
                                           +----------+----------+
                                           |                     |
                                           v                     v
                                    [ WS2812B RGB ]      [ Micro-Servo ]
                                    [  LED Strip  ]      [ Base Swivel ]
                                                                
