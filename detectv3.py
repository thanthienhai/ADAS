from PIL import Image

def detect_lanes(image):
    # Convert image to grayscale
    grayscale_image = image.convert('L')

    # Find contours in the image
    contours, hierarchy = cv2.findContours(grayscale_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Return the contours
    return contours

# Load the image
image = Image.open("C:\\Coding\\ADAS\\Highway-1.jpg")

# Detect the lanes
contours = detect_lanes(image)

# Show the detected lanes
cv2.imshow("Detected lanes", image)
cv2.waitKey(0)

