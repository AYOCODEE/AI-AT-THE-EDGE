# import cv2
# import os
# from picamera2 import Picamera2, Preview
# import time

# # Replace with your name
# name = 'Ayo'

# # Define the directory where images will be stored
# dataset_dir = "/home/c-00314717/my_project/env/ai at the edge/dataset/Ayo"

# # Create the directory if it doesn't already exist
# os.makedirs(dataset_dir, exist_ok=True)

# # Initialize the cameras
# picam2 = Picamera2()

# # Configure the camera for still image capture
# picam2.configure(picam2.create_still_configuration())

# # Start the preview with explicit QTGL for graphical window pop-up
# picam2.start_preview(Preview.QTGL)

# # Allow the camera to initialize properly before starting the loop
# time.sleep(2)  # Delay to give time for camera setup

# # Ensure the camera is started
# picam2.start()

# # Start capturing images
# img_counter = 0

# while True:
#     # Capture a frame from the camera
#     frame = picam2.capture_array()

#     # Display the frame using OpenCV
#     cv2.imshow("Press Space to take a photo", frame)

#     # Wait for a key press
#     k = cv2.waitKey(1) & 0xFF

#     if k == 27:  # ESC key pressed to exit
#         print("Escape hit, closing...")
#         break
#     elif k == 32:  # SPACE key pressed to save image
#         # Save the captured frame to the dataset directory
#         img_name = f"{dataset_dir}/image_{img_counter}.jpg"
#         cv2.imwrite(img_name, frame)
#         print(f"{img_name} written!")
#         img_counter += 1

# # Clean up
# cv2.destroyAllWindows()
# picam2.close()


# # import cv2
# # import os
# # from picamera2 import Picamera2, Preview
# # import time

# # # Replace with your name
# # name = 'Ayo'

# # # Define the directory where images will be stored
# # dataset_dir = "/home/c-00314717/my_project/env/ai at the edge/dataset/Ayo"

# # # Create the directory if it doesn't already exist
# # os.makedirs(dataset_dir, exist_ok=True)

# # # Initialize the cameras
# # picam2 = Picamera2()

# # # Configure the camera for still image capture
# # picam2.configure(picam2.create_still_configuration())

# # # Start the preview with explicit QTGL for graphical window pop-up
# # picam2.start_preview(Preview.QTGL)

# # # Allow the camera to initialize properly before starting the loop
# # time.sleep(2)  # Delay to give time for camera setup

# # # Ensure the camera is started
# # picam2.start()

# # # Start capturing images
# # img_counter = 0

# # while True:
# #     # Capture a frame from the camera
# #     frame = picam2.capture_array()

# #     # Instead of displaying the image, we save it directly
# #     # Check if we should save the image when SPACE is pressed
# #     k = cv2.waitKey(1) & 0xFF

# #     if k == 27:  # ESC key pressed to exit
# #         print("Escape hit, closing...")
# #         break
# #     elif k == 32:  # SPACE key pressed to save image
# #         # Save the captured frame to the dataset directory
# #         img_name = f"{dataset_dir}/image_{img_counter}.jpg"
# #         cv2.imwrite(img_name, frame)
# #         print(f"{img_name} written!")
# #         img_counter += 1

# # # Clean up
# # cv2.destroyAllWindows()
# # picam2.close()


import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully!")

cap.release()

