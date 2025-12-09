import math
import os
from datetime import datetime


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def timestamp_filename(prefix, ext="png"):
    return f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext}"


def euclidean(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def get_angle(a, b, c):
    ab = (a[0] - b[0], a[1] - b[1])
    cb = (c[0] - b[0], c[1] - b[1])
    dot = ab[0] * cb[0] + ab[1] * cb[1]
    mag1 = math.hypot(ab[0], ab[1])
    mag2 = math.hypot(cb[0], cb[1])
    if mag1 * mag2 == 0:
        return 0
    v = dot / (mag1 * mag2)
    v = max(-1, min(1, v))
    return math.degrees(math.acos(v))
