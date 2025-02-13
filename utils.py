# utils.py
import cv2

def ResizeWithAspectRatio(image, width=2560, height=None, inter=cv2.INTER_AREA):
    h, w = image.shape[:2]
    r = width / float(w) if width else height / float(h)
    dim = (width, int(h * r)) if width else (int(w * r), height)
    return cv2.resize(image, dim, interpolation=inter)
