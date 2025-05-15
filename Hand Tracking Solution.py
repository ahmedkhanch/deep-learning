# Import necessary libraries
import cv2
import mediapipe as mp

# Initialize Mediapipe Hands and Drawing utilities
mp_hands = mp.solutions.hands  # Load the Mediapipe Hands model
mp_draw = mp.solutions.drawing_utils  # Utility to draw landmarks and connections

# Open the webcam for video input
cap = cv2.VideoCapture(0)

# Create a Mediapipe Hands object
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read a frame from the webcam.")
            break

        # Convert the BGR frame to RGB because Mediapipe expects RGB input
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect hand landmarks
        results = hands.process(img_rgb)

        # Check if hands were detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks and connections on the frame
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the frame with hand tracking
        cv2.imshow("Hand Tracking", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close the display window
cap.release()
cv2.destroyAllWindows()
