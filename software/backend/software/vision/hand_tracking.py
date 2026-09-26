
"""
H.E.L.I.X Hand Gesture Tracking System
Uses MediaPipe and OpenCV to detect hand gestures via USB webcam.
Sends trigger signals to main logic backend.
"""

import cv2 
import mediapipe as mp
import time

class HandTracker:
    def __init__(self, max_hands=1, detection_con=0.7, track_con=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=detection_con,
            min_tracking_confidence=track_con
        )
        self.mp_draw = mp.solutions.drawing_utils

    def process_frame(self, frame):
        #Convert BGR image to RGB for MediaPipe
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        
        gesture_detected = None
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks overlay on screen
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # Simple Gesture Check: Index finger raised (Tip: Landmark 8, PIP: Landmark 6)
                landmarks = hand_landmarks.landmark
                if landmarks[8].y < landmarks[6].y:
                    gesture_detected = "POINTING_UP"

        return frame, gesture_detected


def main():
    # Initialize USB Webcam (Index 0)
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()

    print("[H.E.L.I.X] Hand tracking active. Press 'q' to exit.")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("[H.E.L.I.X Warning] Frame capture failed.")
            break

        # Process frame for gestures
        processed_frame, gesture = tracker.process_frame(frame)

        if gesture:
            print(f"[H.E.L.I.X Gesture] Detected: {gesture}")

        # Display window for testing local vision stream
        cv2.imshow("H.E.L.I.X Vision Stream", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
