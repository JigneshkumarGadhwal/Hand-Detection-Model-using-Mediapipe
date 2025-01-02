import cv2
import mediapipe as mp

# Initialize Mediapipe hand module:
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Capture the video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    result = hands.process(rgb_frame)

    # Draw landmarks for the index finger and thumb
    if result.multi_hand_landmarks: #If hands are detected, this attribute contains a list of detected hands, each with its landmark coordinates.
        for hand_landmarks in result.multi_hand_landmarks:
            for idx in [4, 8]:  # Thumb tip (4) and Index finger tip (8)
                #Converts the normalized x-coordinate to the pixel value in the corresponding  frame width and height.
                x, y = int(hand_landmarks.landmark[idx].x * frame.shape[1]), int(hand_landmarks.landmark[idx].y * frame.shape[0])
                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)  # Draw green circle
            mp_draw.draw_landmarks(frame, hand_landmarks, None)  # No connections drawn

    cv2.imshow("Index Finger & Thumb Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Escape key to exit
        break

cap.release()
cv2.destroyAllWindows()
