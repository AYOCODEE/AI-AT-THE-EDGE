
import cv2
import os
from picamera2 import Picamera2, Preview
import time
import face_recognition
import pickle
from imutils.video import FPS
import tkinter as tk

# Initialize 'currentname' to trigger only when a new person is identified.
currentname = "unknown"
# Load the known faces and embeddings along with face recognition data
encodingsP = "encodings.pickle"

# Load the face encodings data
print("[INFO] loading encodings...")
data = pickle.loads(open(encodingsP, "rb").read())

# Initialize Picamera2 for the Raspberry Pi camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())

# Start preview (optional, for showing camera feed)
picam2.start_preview(Preview.QTGL)
picam2.start()

# Start the FPS counter
fps = FPS().start()

# Create the Tkinter window
root = tk.Tk()
root.title("Face Recognition")

# Create a label to display the detected name
label = tk.Label(root, text="Detecting...", font=("Helvetica", 20))
label.pack(padx=20, pady=20)

# Function to update the label with the recognized name
def update_label(name):
    label.config(text=f"Welcome {name}")

# Face recognition function that runs in the background
def recognize_faces():
    global currentname
    # Capture a frame from the camera (as an array)
    frame = picam2.capture_array()

    # Convert the frame from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face locations
    boxes = face_recognition.face_locations(frame_rgb)

    # Compute the facial embeddings for each detected face
    encodings = face_recognition.face_encodings(frame_rgb, boxes)
    names = []

    # Loop through each detected face encoding
    for encoding in encodings:
        # Try to match the encoding to known faces
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"  # Default name if no match

        # Check if a match is found
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            # Get the name with the most votes
            name = max(counts, key=counts.get)

        # Always update the name (whether recognized or "Unknown")
        update_label(name)

        # Add name (either recognized or 'Unknown')
        names.append(name)

    # Update FPS counter
    fps.update()

    # Schedule the next call to this function to keep the UI updating
    root.after(1, recognize_faces)  # Recursively call after 1ms

# Start the recognition loop
recognize_faces()

# Start the Tkinter event loop
root.mainloop()

# After exiting the main loop, stop FPS and release resources
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
picam2.stop()
