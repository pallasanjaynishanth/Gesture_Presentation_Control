import cv2
import mediapipe as mp
import pyautogui
import time

print("GESTURE CONTROL FILE IS RUNNING")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Camera not accessible")
    input("Press Enter to exit...")
    exit()

cv2.namedWindow("Gesture Presentation Control", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gesture Presentation Control", 640, 480)
prev_time = 0
cooldown = 2.0  

gesture_history = []
GESTURE_FRAMES_REQUIRED = 5  


def fingers_up(hand):
    fingers = []


    fingers.append(hand.landmark[4].x > hand.landmark[3].x)


    for tip in [8, 12, 16, 20]:
        fingers.append(hand.landmark[tip].y < hand.landmark[tip - 2].y)

    return fingers

print("Gesture system started")
print("1 finger = Next slide | 2 fingers = Previous slide | ESC = Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame not captured")
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    current_time = time.time()

    if results.multi_hand_landmarks and results.multi_handedness:
        confidence = results.multi_handedness[0].classification[0].score

       
        if confidence >= 0.8:
            for hand in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame, hand, mp_hands.HAND_CONNECTIONS
                )

                count = fingers_up(hand).count(True)

                
                gesture_history.append(count)
                if len(gesture_history) > GESTURE_FRAMES_REQUIRED:
                    gesture_history.pop(0)

                
                if (
                    gesture_history.count(1) == GESTURE_FRAMES_REQUIRED
                    and current_time - prev_time > cooldown
                ):
                    pyautogui.press("pagedown")
                    prev_time = current_time
                    gesture_history.clear()
                    cv2.putText(
                        frame, "NEXT SLIDE",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2
                    )

                
                elif (
                    gesture_history.count(2) == GESTURE_FRAMES_REQUIRED
                    and current_time - prev_time > cooldown
                ):
                    pyautogui.press("pageup")
                    prev_time = current_time
                    gesture_history.clear()
                    cv2.putText(
                        frame, "PREVIOUS SLIDE",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2
                    )
        else:
            gesture_history.clear()
    else:
        gesture_history.clear()

    cv2.imshow("Gesture Presentation Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
