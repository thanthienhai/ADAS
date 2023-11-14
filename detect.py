import cv2
import numpy as np

def detect_lines(image):
    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to smooth the image
    blur_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    # Apply Canny edge detection to find edges in the image
    edges = cv2.Canny(blur_image, 50, 150)

    # Apply Hough transform to find lines in the image
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)

    # Draw the lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return image

def detect_lines_1(image):
    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to smooth the image
    blur_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
    
    # Apply Canny edge detection to find edges in the image
    edges = cv2.Canny(blur_image, 50, 150)
    """
    # Apply Hough transform to find lines in the image
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)
    
    # Draw the lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    """
    return edges

def region_of_interest(image):
    """ Function for drawing region 
    of interest on original frame """
    
    # Get size of the original frame
    height, width = image.shape
    
    # Create mask with 0s filled
    mask = np.zeros_like(image)
    
    # Draw polygon
    polygon = np.array([[
        (int(width*0.30), height),              # Bottom-left point
        (int(width*0.46),  int(height*0.72)),   # Top-left point
        (int(width*0.58), int(height*0.72)),    # Top-right point
        (int(width*0.82), height),              # Bottom-right point
    ]], np.int32)
    
    # Fill polygon with value 255 (white color)
    cv2.fillPoly(mask, polygon, 255)
    
    # AND bitwise the mask and the original frame
    roi = cv2.bitwise_and(frame, mask)
    
    return roi
# Load the video
#cap = cv2.VideoCapture("C:\\Coding\\ADAS\\1.mp4")

# Read the first frame from the video
#ret, frame = cap.read()
frame = cv2.imread("C:\\Coding\\ADAS\\high-600.jpg")
# Detect the lines in the frame
detected_frame = detect_lines(frame)
#detected_frame_1 = region_of_interest(detected_frame)
# Show the detected lines
cv2.imshow("Detected lines", detected_frame)
cv2.waitKey(0)