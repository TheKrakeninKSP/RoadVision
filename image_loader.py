# image_loader.py
import cv2
import os

def load_images(num_images=6):
    images = []
    for i in range(num_images):
        img = cv2.imread(f'image_{i}.png')
        if img is not None:
            images.append(img)
    return images
