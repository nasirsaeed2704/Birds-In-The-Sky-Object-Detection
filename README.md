# Birds-In-The-Sky-Object-Detection
This project explores a simple yet effective object detection method using OpenCV to identify birds flying in the sky. The solution is designed to detect objects where birds are visibly darker than the background, leveraging computer vision techniques like adaptive thresholding and contour detection.

Key Features:
Adaptive Thresholding: Dynamically highlights objects by separating them from varying backgrounds, reducing noise from elements like clouds.
Contour Detection: Identifies and highlights detected birds by drawing bounding boxes around them.
Dynamic Image Resizing: Ensures large images fit comfortably within the display for easy visualization.
Noise Reduction: Dilates objects to make them more pronounced while filtering out small artifacts.
How It Works:
Image Preprocessing: The input image is converted to grayscale and processed using adaptive Gaussian thresholding for robust object separation.
Object Enhancement: A dilation process makes contours more distinct.
Contour Filtering: Only significant objects are considered for detection, ensuring precision by ignoring small, irrelevant shapes.
Visualization: Bounding boxes are drawn around detected birds for visual inspection.
Performance and Limitations:
This approach works best in images where birds are clearly distinguishable from the sky. It reduces cloud interference to some extent, but excessive cloud cover or similar background clutter may yield incorrect outputs. Future improvements could involve more advanced filtering techniques and better handling of noisy environments.

Usage:
The project reads bird images from a specified directory, processes them, and displays detection results one at a time.
