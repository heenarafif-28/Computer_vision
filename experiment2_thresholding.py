"""Experiment 2: Thresholding Techniques for Image Segmentation"""

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

# Global Thresholding (T=127)
_, global_thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Adaptive Mean Thresholding (block=11, C=2)
adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY, 11, 2)

# Adaptive Gaussian Thresholding (block=11, C=2)
adaptive_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY, 11, 2)

# Otsu's Thresholding (automatic threshold)
otsu_val, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"Otsu's automatically selected threshold: {otsu_val}")

# Display results
titles = ['Original Image', 'Grayscale Image', 'Global Threshold (T=127)',
          'Adaptive Mean', 'Adaptive Gaussian', "Otsu's Threshold"]
images = [image_rgb, gray, global_thresh, adaptive_mean, adaptive_gaussian, otsu_thresh]

fig, axes = plt.subplots(2, 3, figsize=(16, 9))
for i, ax in enumerate(axes.flat):
    if i == 0:
        ax.imshow(images[i])
    else:
        ax.imshow(images[i], cmap='gray')
    ax.set_title(titles[i], fontsize=11, fontweight='bold')
    ax.axis('off')

plt.suptitle('Experiment 2: Thresholding Techniques for Image Segmentation',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/thresholding_output.png', dpi=150, bbox_inches='tight')
plt.show()
print("Experiment 2 completed. Output saved to outputs/thresholding_output.png")
