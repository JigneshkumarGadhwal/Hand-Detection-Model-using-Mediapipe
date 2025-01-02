import cv2
import mediapipe as mp

# Initialize Mediapipe hand module:
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# capture the video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break

    # Converting frame to RGB
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # Process the frame
    result = hands.process(rgb_frame)

    # Drawing hand landmarks if detected.
    if result.multi_hand_landmarks: # If hands are detected, this attribute contains a list of detected hands, each with its landmark coordinates.
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracking",frame)

    if cv2.waitKey(1) & 0xFF == (27):
        break

cap.release()
cv2.destroyAllWindows()