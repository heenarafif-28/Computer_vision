"""Experiment 3: Edge Detection Techniques for Feature Extraction"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('input/input.jpg')
if image is None:
    print("Error: Could not load image. Check file path.")
    exit()

# Convert for display and processing
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Pre-smoothing with Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Sobel X gradient (detects vertical edges)
sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
sobel_x_abs = cv2.convertScaleAbs(sobel_x)

# Sobel Y gradient (detects horizontal edges)
sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

# Combined Sobel magnitude
sobel_combined = cv2.addWeighted(sobel_x_abs, 0.5, sobel_y_abs, 0.5, 0)

# Laplacian edge detection
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Canny edge detection (low=50, high=150)
canny_edges = cv2.Canny(blurred, 50, 150)

# Display results
titles = ['Original Image', 'Grayscale', 'Sobel X (Vertical Edges)',
          'Sobel Y (Horizontal Edges)', 'Combined Sobel', 'Laplacian', 'Canny']
images = [image_rgb, gray, sobel_x_abs, sobel_y_abs, sobel_combined, laplacian_abs, canny_edges]

fig, axes = plt.subplots(2, 4, figsize=(22, 9))
for i in range(7):
    row, col = i // 4, i % 4
    if i == 0:
        axes[row][col].imshow(images[i])
    else:
        axes[row][col].imshow(images[i], cmap='gray')
    axes[row][col].set_title(titles[i], fontsize=11, fontweight='bold')
    axes[row][col].axis('off')

axes[1][3].axis('off')  # hide unused subplot

plt.suptitle('Experiment 3: Edge Detection Techniques for Feature Extraction',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/edge_detection_output.png', dpi=150, bbox_inches='tight')
plt.show()
print("Experiment 3 completed. Output saved to outputs/edge_detection_output.png")
