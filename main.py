# main.py
import cv2
from image_loader import load_images
from stitcher import stitch_images
from masking import create_road_mask, clean_mask
from visualization import color_roads, display_road_directions

def main():
    images = load_images()
    if len(images) < 2:
        print("Need at least two images to perform stitching")
        return
    
    panorama = stitch_images(images)
    cv2.imwrite('stitched_image.jpg', panorama)
    
    road_mask = create_road_mask(panorama)
    cleaned_mask = clean_mask(road_mask)
    cv2.imwrite('road_mask.jpg', cleaned_mask)
    
    result = color_roads(panorama, cleaned_mask)
    cv2.imshow('Colored Roads', result)
    cv2.waitKey(0)
    cv2.imwrite('colored_roads.jpg', result)
    
    result2, directions = display_road_directions(cleaned_mask, panorama)
    cv2.imshow('Final Result', result2)
    cv2.waitKey(0)
    cv2.imwrite('final.jpg', result2)
    print("Final result saved as 'final.jpg'")
    print("Directions:", directions)
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

