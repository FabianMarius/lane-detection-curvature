**Lane Detection and Road Curvature Estimation with OpenCV**

 **Overview**

This project implements a Lane Detection System for real-time video streams or prerecorded video files. The system detects lane markings on the road, estimates lane curvature, calculates vehicle offset from lane center, and overlays this information on the original video frames.

The pipeline is built using Python with the main logic in LaneDetection.py and supporting utility functions in utlis.py. It is designed to be modular, allowing easy extension for more advanced perception or integration with autonomous driving applications.

 **Scope**

 - Detect left and right lane lines in challenging lighting and road conditions.

 - Compute lane curvature in meters and vehicle lateral offset from lane center.

 - Overlay lane boundaries and metrics on video frames for visualization.

 - Support both video files (.mp4) and live camera feed.

**Solution**

The system uses computer vision techniques, including:

 - Camera calibration to remove lens distortion.

 - Color and gradient thresholding to extract lane features.

 - Perspective transform to create a bird’s-eye view for accurate lane analysis.

 - Histogram and sliding window method for lane pixel detection.

 - Polynomial fitting to model lane lines.

 - Curvature and offset calculations in real-world units.

All utility functions are implemented in utlis.py, while LaneDetection.py orchestrates the end-to-end pipeline.

 **Execution Flow**

Below is the detailed execution flow of the system:

          ┌─────────────┐
          │  Input      │
          │ Video/Camera│
          └─────┬───────┘
                │
        ┌───────▼────────┐
        │ Calibration &  │
        │ Preprocessing  │
        │ - cal_undistort│
        │ - preprocess   │
        └───────┬────────┘
                │
        ┌───────▼─────────┐
        │ Perspective      │
        │ Transform        │
        │ - warp_image()   │
        └───────┬─────────┘
                │
        ┌───────▼──────────┐
        │ Lane Detection &  │
        │ Polynomial Fitting│
        │ - get_hist()      │
        │ - sliding_window()│
        │ - np.polyfit()    │
        └───────┬──────────┘
                │
        ┌───────▼──────────┐
        │ Curvature & Offset│
        │ - measure_curvature_real() │
        │ - calculate_vehicle_offset() │
        └───────┬──────────┘
                │
        ┌───────▼──────────┐
        │ Visualization &  │
        │ Overlay           │
        │ - draw_lane()     │
        └───────┬──────────┘
                │
        ┌───────▼─────────┐
        │ Output Video    │
        │ with lane lines │
        │ and metrics     │
        └─────────────────┘

 **Metrics Calculated**

 - Lane curvature (meters) – estimates the radius of the lane curve.

 - Vehicle offset (meters) – calculates lateral deviation from the lane center.

 **Results**

 - Real-time lane overlay on videos.

 - Curvature and offset displayed dynamically.

 - Robust detection in different lighting and partial occlusion scenarios.

 **Limitations**

 - Struggles with worn-out or missing lane markings.

 - Sensitivity to extreme shadows or glare.

 - Assumes roughly flat roads; hills and slopes may affect accuracy.

 **Documentation & Code Structure**

LaneDetection.py – main execution script.

utlis.py – utility functions: calibration, preprocessing, warping, histogram, sliding window, polynomial fitting, curvature and offset calculations, visualization.

VideoTest01.mp4 – example input video.

**_Clone this repository_**:

**git clone https://github.com/username/lane-detection-curvature.git**

**_Install dependencies_**:
The project is implemented in Python **3.10+** with the following dependencies:
- **_opencv-python_**
- **_numpy_**
- **_matplotlib_**

**_Run the main script command_**:

_python LaneDetection.py_

📝 License

This project is released under the MIT License.
