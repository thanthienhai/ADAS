import cv2
import numpy as np

def detect_lines(image):
    # Convert the image to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to the image.
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection to the image.
    edges = cv2.Canny(blur, 50, 150)

    # Find the lines in the image.
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=100)

    return lines

def get_speed(lines, image):
    # Get the width of the image.
    width = image.shape[1]

    # Get the number of lines.
    n_lines = len(lines)

    # Initialize the speed.
    speed = 0

    # For each line, calculate the speed.
    for line in lines:
        # Get the x-coordinates of the start and end points of the line.
        x1, y1, x2, y2 = line[0]

        # Get the length of the line.
        length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Get the speed of the line.
        speed += length / width

    return speed

if __name__ == "__main__":
    # Read the image.
    image = cv2.imread("image.jpg")

    # Detect the lines in the image.
    lines = detect_lines(image)

    # Get the speed of the lines.
    speed = get_speed(lines, image)

    # Print the speed.
    print("The speed of the car is:", speed, "km/h")