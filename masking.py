# masking.py
import cv2
import numpy as np
from utils import ResizeWithAspectRatio

def create_road_mask(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([2, 0, 114])
    upper = np.array([30, 50, 245])
    mask = cv2.inRange(hsv, lower, upper)
    resized_mask = ResizeWithAspectRatio(mask)
    cv2.imshow('Mask', resized_mask)
    cv2.waitKey(0)
    return mask
    
def clean_mask(mask, min_area=1000):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
    cleaned_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    cleaned_mask = cv2.morphologyEx(cleaned_mask, cv2.MORPH_OPEN, kernel, iterations=1)
    
    contours, _ = cv2.findContours(cleaned_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_mask = np.zeros_like(cleaned_mask)
    
    for contour in contours:
        if cv2.contourArea(contour) >= min_area:
            cv2.drawContours(filtered_mask, [contour], -1, 255, -1)
    
    x = ResizeWithAspectRatio(filtered_mask)
    cv2.imshow('Cleaned Mask', x)
    cv2.waitKey(0)
    return filtered_mask

