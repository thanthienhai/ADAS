import cv2
import numpy as np

def detect_lanes_2(image):
    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to binarize the image
    threshold_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the image
    contours, hierarchy = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contours
    largest_contours = [contour for contour in contours if cv2.contourArea(contour) > 1000]

    # Classify the contours as lanes
    lanes = []
    for contour in largest_contours:
        # Calculate the center of the contour
        center = cv2.moments(contour)["m00"] / cv2.moments(contour)["m01"]

        # Calculate the width and height of the contour
        width = cv2.arcLength(contour, True)
        height = cv2.contourArea(contour) / width

        # Check if the contour is a lane
        if height > 50 and width > 100:
            lanes.append(contour)

    # Draw the lanes on the image
    for lane in lanes:
        cv2.drawContours(image, [lane], -1, (0, 255, 0), 2)

    return image

# Load the image
image = cv2.imread("C:\\Coding\\ADAS\\Highway-1.jpg")

# Detect the lanes
detected_image = detect_lanes_2(image)

# Show the detected lanes
cv2.imshow("Detected lanes", detected_image)
cv2.waitKey(0)