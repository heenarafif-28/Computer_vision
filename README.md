# Computer Vision – Assignment 1

**B.Tech Artificial Intelligence and Data Science**  
**Course:** Computer Vision (Academic Year 2025–2026)

This repository contains Python implementations of fundamental computer vision techniques across three laboratory experiments:

1. **Experiment 1: Image Enhancement Using Classical Filtering Techniques**
   - Mean Filter (`cv2.blur`)
   - Gaussian Filter (`cv2.GaussianBlur`)
   - Median Filter (`cv2.medianBlur`)
   - Bilateral Filter (`cv2.bilateralFilter`)
2. **Experiment 2: Thresholding Techniques for Image Segmentation**
   - Global (Fixed) Thresholding (`cv2.threshold`)
   - Adaptive Mean Thresholding (`cv2.adaptiveThreshold`)
   - Adaptive Gaussian Thresholding (`cv2.adaptiveThreshold`)
   - Otsu's Automated Thresholding (`cv2.THRESH_OTSU`)
3. **Experiment 3: Edge Detection Techniques for Feature Extraction**
   - Sobel Operator (X-gradient, Y-gradient, Combined magnitude)
   - Laplacian Second-Derivative Operator
   - Canny Multi-Stage Optimal Edge Detector

---

## Directory Structure

```
Computer_vision/
├── README.md
├── requirements.txt
├── Computer_Vision_Assignment_1.docx
├── Computer_Vision_Assignment_1.pdf
├── experiment1_filtering.py
├── experiment2_thresholding.py
├── experiment3_edge_detection.py
├── generate_final_assignment.py
├── input/
│   └── input.jpg
└── outputs/
    ├── filtering_output.png
    ├── thresholding_output.png
    ├── edge_detection_output.png
    └── github_repo_screenshot.png
```

---

## Installation & Setup

1. Clone or download this repository:
   ```bash
   git clone https://github.com/heenarafif-28/Computer_vision.git
   cd Computer_vision
   ```
2. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run each experiment:
   ```bash
   python experiment1_filtering.py
   python experiment2_thresholding.py
   python experiment3_edge_detection.py
   ```
   All generated figures will be automatically saved to the `outputs/` folder.
