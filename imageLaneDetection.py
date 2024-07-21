import cv2
import os
# Import libraries for video writing (optional, choose one)
# Option 1: OpenCV VideoWriter
# import cv2 as cv

# Option 2: FourCC code for more video codec flexibility
# import cv2

# Hiện đang thiếu folder ultrafastLaneDetector

from ultrafastLaneDetector import UltrafastLaneDetector, ModelType

# Define video input and output paths (modify as needed)
video_input_path = "data/dashcam2.mp4"
video_output_path = "output_lanes.mp4"

output_folder = 'output'

# Initialize lane detection model
model_path = "models/tusimple_18.pth"
model_type = ModelType.TUSIMPLE
use_gpu = False
lane_detector = UltrafastLaneDetector(model_path, model_type, use_gpu)



# Start video capture
cap = cv2.VideoCapture(video_input_path)
if not cap.isOpened():
  print(f"Error: Cannot open video file {video_input_path}")
  exit()

fps = 30.0
out = cv2.VideoWriter(video_output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (int(cap.get(3)), int(cap.get(4))))

frame_count = 0

while cap.isOpened():
    try:
        # Read frame from the video
        ret, frame = cap.read()
    except:
        continue

    if ret:
        # Detect lanes
        output_img = lane_detector.detect_lanes(frame)
        # Write the frame with detected lanes to the output video
        #out.write(output_img)
        output_path = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(output_path, output_img)
        frame_count += 1
        print('Thanh cong')
    else:
        break

# Release resources
cap.release()
#out.release()

print("Video processing complete. Output saved as", video_output_path)
