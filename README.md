# Virtual-webcam
Ultra-lightweight real-time webcam background isolation and custom backdrop switcher built with Python and OpenCV.

Virtual Cam is a high-efficiency computer vision app designed to isolate the user from their physical background in real-time. Built specifically to run on low-spec hardware (such as dual-core CPUs and low RAM environments) without lagging video calls on platforms like Discord, Zoom, or Google Meet.

# Key Features
Real-Time Background Replacement: Isolates the subject and swaps out the physical background with custom images.

Hot-Swappable Backdrops: Switch between multiple custom background images on the fly using simple keyboard shortcuts (N, Spacebar, or 1-9).

Ultra Low-Resource Footprint: Optimized with frame downsampling (360p @ 24 FPS) and fast HSV color space segmentation for minimal CPU/RAM consumption.

Mobile Webcam Compatibility: Fully compatible with smartphone camera bridges like Iriun Webcam and DroidCam.

Discord Screen Share Ready: Outputs a dedicated window ready to share directly into video calls.

# Built With
Python 3

OpenCV (cv2)

NumPy
Getting Started

# Prerequisites

Python 3.x installed on your system.

A webcam or mobile camera app (Iriun / DroidCam).
# Installation

# Clone the repository:
(Bash)
git clone https://github.com/YOUR_USERNAME/Virtual-cam.git
cd Virtual-cam

# Install required libraries:
pip install opencv-python numpy
Bash
pip install opencv-python numpy
Set up your backgrounds:

Create a folder named backgrounds on your Desktop.

Drop any .jpg or .png images into the folder.
Running the AppExecute the main script from your terminal or Command Prompt:Bashpython webcam.py
Keyboard ControlsKeyActionN / SpacebarSwitch to the next background image1 - 9Jump directly to a specific background imageQExit the application
