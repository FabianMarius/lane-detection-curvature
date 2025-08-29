# Lane Detection and Road Curvature Estimation with OpenCV

## Overview
This project implements a **Lane Detection System** for real-time video streams or prerecorded video files.  
The system detects lane markings on the road, estimates lane curvature, calculates vehicle offset from lane center, and overlays this information on the original video frames.  

It was developed as part of a **technical project in the automotive & intelligent vehicle domain**, aiming to simulate how autonomous cars can use vision systems to maintain their position on the road.  

## Scope and Objectives
- Detect left and right lane lines in different lighting and road conditions.  
- Estimate lane curvature (in meters) using polynomial fitting.  
- Compute the vehicle's lateral offset from lane center.  
- Overlay the detected lane and metrics (curvature, offset) directly on the video.  
- Support both video files (.mp4) and live camera feeds.  

## Solution & Techniques
The system uses computer vision techniques with **Python + OpenCV**:  

1. Image Acquisition  
   - Input from video file or live camera feed.  

2. Camera Calibration  
   - Correction of lens distortion using calibration parameters.  

3. Preprocessing  
   - Color space transformations.  
   - Gradient thresholding and Canny edge detection to create binary masks.  

4. Perspective Transform (Bird’s-Eye View)  
   - Warping the region of interest to simulate a top-down view of the road.  

5. Histogram and Sliding Windows  
   - Generating a histogram of pixel intensity to identify lane line positions.  
   - Using sliding windows to track pixels belonging to lane lines.  

6. Polynomial Fitting  
   - Fitting a 2nd-degree polynomial for each lane line.  

7. Metrics Calculation  
   - Lane curvature in real-world units (meters).  
   - Vehicle offset relative to the lane center.  

8. Visualization  
   - Drawing lane lines, curvature, and offset directly on the video frames.  

## Execution Flow

```text
      ┌─────────────┐
      │  Input      │
      │ Video/Camera│
      └─────┬───────┘
            │
    ┌───────▼────────┐
    │ Calibration &  │
    │ Preprocessing  │
    └───────┬────────┘
            │
    ┌───────▼─────────┐
    │ Perspective      │
    │ Transform        │
    └───────┬─────────┘
            │
    ┌───────▼──────────┐
    │ Lane Detection &  │
    │ Polynomial Fitting│
    └───────┬──────────┘
            │
    ┌───────▼──────────┐
    │ Curvature & Offset│
    └───────┬──────────┘
            │
    ┌───────▼──────────┐
    │ Visualization &  │
    │ Overlay           │
    └───────┬──────────┘
            │
    ┌───────▼─────────┐
    │ Output Video    │
    └─────────────────┘
```

## Metrics Calculated
- Lane curvature: radius of the road curve in meters.  
- Vehicle offset: lateral deviation from the lane center in meters.  

## Results
- Lane detection accuracy of approximately 85% in normal daylight conditions.  
- Dynamic overlay of curvature and offset information.  
- Robust detection in moderate lighting and partial occlusion scenarios.  

## Limitations
- Reduced accuracy at night or in adverse weather conditions (fog, heavy rain).  
- Slower processing: a 30-second video required ~60 seconds to process on a standard laptop. With optimization or better hardware, real-time processing is achievable.  
- Worn-out or missing lane markings significantly decrease detection reliability.  

## Documentation & Code Structure
- LaneDetection.py – main execution pipeline.  
- utlis.py – utility functions: calibration, preprocessing, perspective transform, histogram, sliding window, polynomial fitting, curvature/offset calculations, visualization.  
- VideoTest01.mp4 – example input video.  

## Installation & Run
Clone this repository:

```bash
git clone https://github.com/username/lane-detection-curvature.git
```

Install dependencies:

```bash
pip install opencv-python numpy matplotlib
```

Run the main script:

```bash
python LaneDetection.py
```

## Future Work
- Optimize code for real-time video processing.  
- Improve robustness for night driving and harsh weather conditions.  
- Extend the system with deep learning-based lane detection models.  

## License
This project is released under the MIT License.
