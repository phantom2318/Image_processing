# Image Processing with OpenCV & Custom Library (`ipress`)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5.x%20%2F%204.x-green.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A hands-on collection of fundamental image processing and computer vision techniques implemented in Python using OpenCV, NumPy, and Matplotlib. 

This repository also includes **`ipress`**, a custom local utility library created to streamline common computer vision tasks like interactive GUI image selection and side-by-side Matplotlib plotting.

---

## 📁 Repository Structure

```text
Image_processing/
├── .vscode/
│   └── settings.json           # Configures Pylance extraPaths for the local library
├── Basic operation/
│   ├── Arithmatic_operation.py # Image addition and weighted blending
│   ├── Color_generation.py     # Color spaces, canvas creation & display
│   ├── drawing.py              # Geometric shapes, lines, and annotations
│   ├── Geo_tranformation.py    # Rotation, scaling, translation & perspective
│   ├── Operation_of_Images.py  # Pixel manipulation, slicing, ROI, channel split/merge
│   └── thresholding.py         # Binary, adaptive, and Otsu thresholding
├── Local_library/
│   ├── ipress/
│   │   ├── __init__.py         # Package exports
│   │   └── img_utils.py        # Dialog picker & side-by-side subplot visualizer
│   └── pyproject.toml          # PEP 621 package configuration for ipress
├── .gitignore                  # Ignores pycache, build artifacts, environments
├── LICENSE                     # MIT License
├── README.md                   # Project documentation
└── requirements.txt            # Project dependencies
```

---

## 📦 The `ipress` Library

The repository includes a custom utility package located in [`Local_library`](Local_library/). It eliminates boilerplate code across your image processing scripts:

### Key Utilities:
- **`select_image() -> str`**: Opens a native OS file dialog (with topmost focus) allowing you to browse and select image files (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`).
- **`subplot(image1, image2, ...)`**: Plots two images side-by-side using Matplotlib. Automatically handles BGR-to-RGB color space conversion, supports colormaps (e.g. `cmap="gray"`), custom titles, and falls back to interactive file selection if an image argument is omitted.

### Quick Example:
```python
import ipress as ipr
import cv2 as cv

# Interactively select an image using file dialog
path = ipr.select_image()
img = cv.imread(path)

# Perform any OpenCV operation
blurred = cv.GaussianBlur(img, (15, 15), 0)

# Display original and processed image side-by-side
ipr.subplot(img, blurred, title1="Original", title2="Gaussian Blur")
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/phantom2318/Image_processing.git
cd Image_processing
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install the Local `ipress` Package in Editable Mode
Installing with `-e` ensures that any modifications made to `Local_library/ipress` take effect immediately without reinstalling:
```bash
pip install -e Local_library
```

> **Note for VS Code users**: The included `.vscode/settings.json` already contains `"python.analysis.extraPaths": ["${workspaceFolder}/Local_library"]`. This guarantees full Pylance IntelliSense, autocomplete, and docstrings out of the box.

---

## 🧪 Modules & Operations Covered

| Script | Topics Covered | Key OpenCV Functions |
|---|---|---|
| [`Arithmatic_operation.py`](Basic%20operation/Arithmatic_operation.py) | Arithmetic Addition, Alpha Blending | `cv.add`, `cv.addWeighted`, `cv.resize` |
| [`Color_generation.py`](Basic%20operation/Color_generation.py) | Custom Color Generation, Pixel Arrays | `cv.cvtColor`, `np.full` |
| [`drawing.py`](Basic%20operation/drawing.py) | Drawing Primitives | `cv.line`, `cv.circle`, `cv.rectangle`, `cv.putText` |
| [`Geo_tranformation.py`](Basic%20operation/Geo_tranformation.py) | Affine, Scaling, Rotation, Perspective | `cv.warpAffine`, `cv.getRotationMatrix2D`, `cv.resize` |
| [`Operation_of_Images.py`](Basic%20operation/Operation_of_Images.py) | Region of Interest (ROI), Channel Operations | `cv.split`, `cv.merge`, array slicing |
| [`thresholding.py`](Basic%20operation/thresholding.py) | Binary, Adaptive, and Otsu Thresholding | `cv.threshold`, `cv.adaptiveThreshold` |

---

## 🛠️ Running the Scripts

Run any script directly from the project root:

```bash
# Example: Run arithmetic blending operations
python "Basic operation/Arithmatic_operation.py"

# Example: Run geometric transformation experiments
python "Basic operation/Geo_tranformation.py"
```

When prompted, select image file(s) via the GUI file picker to view the results.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/phantom2318/Image_processing/issues).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

