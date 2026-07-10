# opencv-fundamentals

A structured collection of OpenCV computer vision projects — from document scanning to face detection and object tracking — built as a foundational learning ladder toward robotics and embedded vision applications.

## About

This repository documents my progression through classical computer vision techniques using OpenCV, built as preparation for more advanced robotics and embedded vision work. Each project builds on concepts from the previous one — starting with image preprocessing and perspective transforms, moving through Haar Cascade-based face/eye detection, and culminating in contour-based object tracking.

These projects form the foundation for a larger pan-tilt face-tracking robot (see [pan-tilt-face-tracker] — coming soon), which integrates this vision pipeline with Arduino-based servo control.

## Projects

| # | Project | Description | Status |
|---|---------|-------------|--------|
| 01 | Document Scanner | Perspective warp-based document scanning from a live/still image | 🔜 Planned |
| 02 | [Face & Eye Detection](./02-face-eye-detection) | Haar Cascade-based face and eye detection with live webcam feed | ✅ Complete |
| 03 | [Face Tracking (Offset + Smoothing)](./03-face-tracking-offset) | Calculates face position offset from frame center, maps to servo angles, applies exponential smoothing for stable tracking | ✅ Complete (software) |
| 04 | Color/Object Tracking | HSV-based color masking and contour tracking | 🔜 In progress |
| 05 | Motion Detection | Frame differencing-based motion/intruder detection | 🔜 In progress |
| 06 | [Shape/Contour Detection](./06-shape-contour-detection) | Classical CV pipeline: blur → grayscale → Canny → dilation → contours | ✅ Complete |

## Tech Stack
- Python 3
- OpenCV (`opencv-python`)
- NumPy

## Setup
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Roadmap
This repo is part of a larger learning path:
1. OpenCV fundamentals (this repo)
2. Pan-tilt face tracker with Arduino servo integration (separate repo, in progress)
3. ROS2 fundamentals
4. Sensor fusion + embedded deployment (Raspberry Pi)

## License
MIT — see [LICENSE](./LICENSE)
