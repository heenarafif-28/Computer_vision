"""Experiment 1: Image Enhancement Using Classical Filtering Techniques"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('input/input.jpg')
if image is None:
    print("Error: Could not load image. Check file path.")
    exit()

# Convert BGR to RGB for Matplotlib display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Mean Filter (5x5 kernel)
mean_filtered = cv2.blur(image_rgb, (5, 5))

# Apply Gaussian Filter (5x5 kernel, auto sigma)
gaussian_filtered = cv2.GaussianBlur(image_rgb, (5, 5), 0)

# Apply Median Filter (kernel size 5)
median_filtered = cv2.medianBlur(image_rgb, 5)

# Apply Bilateral Filter (d=9, sigmaColor=75, sigmaSpace=75)
bilateral_filtered = cv2.bilateralFilter(image_rgb, 9, 75, 75)

# Display results
titles = ['Original Image', 'Mean Filter (5x5)', 'Gaussian Filter (5x5)',
          'Median Filter (5x5)', 'Bilateral Filter (d=9)']
images = [image_rgb, mean_filtered, gaussian_filtered, median_filtered, bilateral_filtered]

fig, axes = plt.subplots(1, 5, figsize=(22, 4))
for i in range(5):
    axes[i].imshow(images[i])
    axes[i].set_title(titles[i], fontsize=10, fontweight='bold')
    axes[i].axis('off')

plt.suptitle('Experiment 1: Image Enhancement Using Classical Filtering Techniques',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('outputs/filtering_output.png', dpi=150, bbox_inches='tight')
plt.show()
print("Experiment 1 completed. Output saved to outputs/filtering_output.png")
