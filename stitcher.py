# stitcher.py
import cv2
from image_loader import load_images
from utils import ResizeWithAspectRatio

def stitch_images(images):
    stitcher = cv2.Stitcher_create()
    status, panorama = stitcher.stitch(images)
    print("Panorama Generated")
    resized_pano = ResizeWithAspectRatio(panorama)
    cv2.imshow('Wide View Image', resized_pano)
    cv2.waitKey(0)
    return panorama
