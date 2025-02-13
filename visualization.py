# visualization.py
import cv2
import numpy as np

def color_roads(image, mask, color=(0, 255, 0)):
    overlay = np.zeros_like(image)
    overlay[mask > 0] = color
    return cv2.addWeighted(image, 0.6, overlay, 0.4, 0)

def display_road_directions(mask, image):
    center = (mask.shape[1] // 2, mask.shape[0] // 2)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    directions = set()
    
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx, cy = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
            angle = np.arctan2(center[1] - cy, cx - center[0]) * 180 / np.pi
            
            direction = ("East" if -15 <= angle <= 15 else
                         "Northeast" if 15 < angle <= 75 else
                         "North" if 75 < angle <= 105 else
                         "Northwest" if 105 < angle <= 190 else
                         "West" if angle > 190 or angle < -165 else
                         "Southwest" if -165 < angle <= -105 else
                         "South" if -105 < angle <= -75 else
                         "Southeast")
            
            if direction not in directions:
                cv2.putText(image, direction, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 5)
                directions.add(direction)
    return image, directions
