# This code was used to take pictures from the camera for training the model

import cv2
import os
from picamera2 import Picamera2
import time
import sys
import select


name = 'Ayo'

# Defined the directory where images will be stored
dataset_dir = "/home/c-00314717/my_project/env/ai at the edge/dataset/Ayo"

# Cchecking if the directory exist and if it doesn't it creates one
os.makedirs(dataset_dir, exist_ok=True)

# Initializing the camera
picam2 = Picamera2()

# Configuring the camera for still image capture
picam2.configure(picam2.create_still_configuration())

# Start the camera (no preview in headless mode)
picam2.start()

# Allow the camera to initialize properly before starting the loop
time.sleep(2)  # Delay to give time for camera setup

# Start capturing images
img_counter = 0

print("Press Enter to capture an image. Type 'exit' to stop.")

while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Check for user input in the terminal
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        user_input = sys.stdin.readline().strip()
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        elif user_input == '':
            # Save the captured frame to the dataset directory
            img_name = f"{dataset_dir}/image_{img_counter}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!")
            img_counter += 1
        else:
            print("Invalid input. Press Enter to capture or type 'exit' to stop.")
    
    time.sleep(0.1)  # Short delay to avoid busy loop

# Clean up
picam2.close()

