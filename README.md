# Worker Safety Vision 👷

A computer vision tool that uses standard webcams to detect if workers are wearing required safety helmets and vests in real-time.

## Description
A computer vision tool that uses standard webcams and deep learning to detect if workers are wearing mandatory safety equipment (PPE) like helmets and vests in real-time.

## Key Features
- **Real-Time PPE Detection:** Identifies helmets, vests, and safety goggles in video frames.
- **Automated Alerts:** Triggers a software alarm when an unprotected worker enters a hazardous zone.
- **Compliance Logging:** Records time-stamped visual evidence of safety breaches for audit reports.

## Tech Stack
- **Language:** Python
- **Libraries:** OpenCV, MediaPipe, TensorFlow, Streamlit
- **Model:** Pre-trained Object Detection Model (SSD/YOLO) specialized for PPE.

## Engineering Logic
- **Backend:** The system utilizes OpenCV to capture video frames and MediaPipe for person detection, then passes the region of interest to a custom classifier that identifies safety gear.
- **Software Engine:** A Streamlit dashboard provides a live safety feed with bounding boxes drawn around workers, highlighting "Safe" (Green) or "Risk" (Red) status.
