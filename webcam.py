import cv2
import numpy as np

# 1. Open webcam
cap = cv2.VideoCapture(0)

# 2. Enforce 360p resolution for low Pentium CPU usage
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
cap.set(cv2.CAP_PROP_FPS, 24)

# 3. Create a solid black background
backdrop = np.zeros((360, 640, 3), dtype=np.uint8)

print("Running background isolator! Click the video window and press 'q' to exit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip horizontally for natural mirror view
    frame = cv2.flip(frame, 1)

    # Convert frame to HSV color space for ultra-fast thresholding
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR_HSV)

    # Define color range of your background wall (default: isolates high contrast)
    # Adjust these values if needed to match your room lighting
    lower_bg = np.array([0, 0, 0])
    upper_bg = np.array([180, 255, 60])

    # Create mask of the background
    mask = cv2.inRange(hsv, lower_bg, upper_bg)

    # Invert mask so white = you, black = background
    person_mask = cv2.bitwise_not(mask)

    # Start with the black backdrop and copy ONLY you onto it
    output = backdrop.copy()
    output[person_mask > 0] = frame[person_mask > 0]

    # Show live feed window
    cv2.imshow("Isolated Feed (Discord)", output)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()