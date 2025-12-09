import time
import os
import pyautogui
from pynput.mouse import Button, Controller
import config
from utils import euclidean, timestamp_filename, get_angle

mouse = Controller()


class GestureHandler:
    def __init__(self):
        os.makedirs(config.SAVE_DIR, exist_ok=True)
        self.last_click_time = 0
        self.last_drag_time = 0
        self.last_screenshot_time = 0
        self.dragging = False

    # ---------- Finger Counting ----------
    def count_fingers(self, lm):
        fingers = 0

        # Thumb
        if lm[4][0] > lm[3][0]:
            fingers += 1

        # Other fingers (tip y < pip y)
        finger_tips = [8, 12, 16, 20]
        finger_pips = [6, 10, 14, 18]

        for tip, pip in zip(finger_tips, finger_pips):
            if lm[tip][1] < lm[pip][1]:
                fingers += 1

        return fingers

    # ---------- Core Gestures ----------
    def left_click(self):
        now = time.time()
        if now - self.last_click_time > config.CLICK_DEBOUNCE:
            self.last_click_time = now
            mouse.click(Button.left)
            return "Left Click"

    def right_click(self):
        now = time.time()
        if now - self.last_click_time > config.CLICK_DEBOUNCE:
            self.last_click_time = now
            mouse.click(Button.right)
            return "Right Click"

    def double_click(self):
        pyautogui.doubleClick()
        return "Double Click"

    def screenshot(self):
        now = time.time()
        if now - self.last_screenshot_time > config.SCREENSHOT_COOLDOWN:
            self.last_screenshot_time = now
            fname = timestamp_filename("screenshot")
            path = os.path.join(config.SAVE_DIR, fname)
            pyautogui.screenshot().save(path)
            return "Screenshot"

    # ---------- Action Handler ----------
    def handle(self, frame, lm, smoothed_pos, screen_size, frame_size):
        sx, sy = smoothed_pos
        sw, sh = screen_size
        fw, fh = frame_size

        mx = int((sx / fw) * sw)
        my = int((sy / fh) * sh)

        fingers = self.count_fingers(lm)

        # NEW FINGER RULES
        if fingers == 2:
            return "Idle"
        if fingers == 3:
            pyautogui.moveTo(mx, my, duration=0)
            return "Move"
        if fingers == 4:
            pyautogui.scroll(300)
            return "Scroll"

        # ----------- Existing gestures ----------
        thumb_index_dist = euclidean(lm[4], lm[8])
        index_angle = get_angle(lm[5], lm[6], lm[8])
        middle_angle = get_angle(lm[9], lm[10], lm[12])

        # Left click gesture
        if index_angle < config.ANGLE_THRESHOLD_CLICK and middle_angle > 90:
            return self.left_click()

        # Right click gesture
        if middle_angle < config.ANGLE_THRESHOLD_CLICK and index_angle > 90:
            return self.right_click()

        # Double click
        if index_angle < 50 and middle_angle < 50:
            return self.double_click()

        # Screenshot (pinch)
        if thumb_index_dist < 0.05:
            return self.screenshot()

        # Drag (pinch & hold)
        if thumb_index_dist < 0.06 and not self.dragging:
            self.dragging = True
            mouse.press(Button.left)
            return "Drag Start"

        if self.dragging and thumb_index_dist > 0.06:
            self.dragging = False
            mouse.release(Button.left)
            return "Drag End"

        return None
