import cv2
import mediapipe as mp
import pyautogui
from utils import ensure_dir
from gestures import GestureHandler
from smoothing import EMA
import config

ensure_dir(config.SAVE_DIR)

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=config.MODEL_COMPLEXITY,
    min_detection_confidence=config.DETECTION_CONFIDENCE,
    min_tracking_confidence=config.TRACKING_CONFIDENCE,
    max_num_hands=config.MAX_NUM_HANDS
)

draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.WEBCAM_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.WEBCAM_HEIGHT)

screen_w, screen_h = pyautogui.size()
handler = GestureHandler()
ema = EMA(alpha=config.SMOOTHING_ALPHA)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    h, w, _ = frame.shape
    lm = []

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        draw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)

        for p in hand.landmark:
            lm.append((p.x, p.y))

        tip = hand.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
        fx, fy = int(tip.x * w), int(tip.y * h)

        sx, sy = ema.update(fx, fy)

        gesture = handler.handle(frame, lm, (sx, sy), (screen_w, screen_h), (w, h))
        if gesture:
            cv2.putText(frame, gesture, (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        ema.x = None
        ema.y = None

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
