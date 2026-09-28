# Image Processing with OpenCV & Custom Library (`ipress`)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5.x%20%2F%204.x-green.svg)](https://opencv.org/)
[![scikit-image](https://img.shields.io/badge/scikit--image-0.21%2B-orange.svg)](https://scikit-image.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive, modular collection of computer vision and digital image processing algorithms implemented in Python using **OpenCV**, **NumPy**, **Matplotlib**, and **scikit-image**.

This repository covers foundational pixel operations, spatial filtering, edge detection, color space conversions, feature extraction (histograms, CDF equalization, GLCM, custom convolution kernels), and includes a custom local helper package called **`ipress`** to streamline GUI file picking, saving, and side-by-side visualization.

---

## 📁 Repository Structure

```text
Image_processing/
├── .vscode/
│   └── settings.json               # Configures Pylance extraPaths for local library
├── Basic operation/
│   ├── Arithmatic_operation.py     # Simple pixel addition and weighted alpha blending
│   ├── Color_generation.py         # Custom RGB array synthesis and display
│   ├── drawing.py                  # Geometric shapes, lines, and annotations
│   ├── Edge_Detection.py           # Sobel, Laplacian, and Canny edge detection
│   ├── Filtering.py                # Mean, Gaussian, Median, and Bilateral smoothing
│   ├── Geo_tranformation.py        # Rotation, scaling, affine & perspective transforms
│   ├── masking.py                  # Bitwise masking and masked histogram analysis
│   ├── Operation_of_Images.py      # Pixel access, ROI cropping, channel split/merge
│   └── thresholding.py             # Binary, adaptive, and Otsu thresholding
├── Feature_Extraction/
│   ├── GLCM.py                     # Gray-Level Co-occurrence Matrix texture analysis
│   ├── histogram.py                # Grayscale/RGB histograms and full CDF equalization
│   └── kernel_operation.py         # Dynamic 2D convolution, blurring & sharpening
├── Image Formats/
│   └── Color_Scale.py              # Conversions: BGR, Gray, YCrCb, YUV, HSV, HLS, LAB
├── Local_library/
│   ├── ipress/
│   │   ├── __init__.py             # Exports: select_image, save_image, subplot
│   │   └── img_utils.py            # Dialog picker, file saver, and subplot visualizer
│   └── pyproject.toml              # PEP 621 package configuration for ipress
├── .gitignore                      # Python, packaging, cache, and OS ignore rules
├── LICENSE                         # MIT License
├── README.md                       # Project documentation
└── requirements.txt                # Project dependencies
```

---

## 📦 The `ipress` Helper Library

Located in [`Local_library/`](Local_library/), **`ipress`** is a custom package designed to remove repetitive boilerplate across image processing workflows:

### Key Functions
- **`select_image() -> str`**: Launches an OS-native file dialog (with topmost focus) to choose an image (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`).
- **`save_image(image, default_name="saved_image.png")`**: Opens a native "Save As" file dialog to export processed images directly to disk.
- **`subplot(image1, image2, cmap1=None, cmap2=None, title1="Image-1", title2="Image-2")`**: Displays two images side-by-side using Matplotlib. Automatically handles BGR-to-RGB conversion, accepts custom colormaps (e.g. `cmap="gray"`), and triggers the file selector automatically if either image argument is omitted.

### Usage Example
```python
import ipress as ipr
import cv2 as cv

# 1. Interactive file selection
path = ipr.select_image()
img = cv.imread(path)

# 2. Perform an operation (e.g. Gaussian Blur)
blurred = cv.GaussianBlur(img, (15, 15), 0)

# 3. Side-by-side comparison
ipr.subplot(img, blurred, title1="Original", title2="Gaussian Blur")

# 4. Save processed output
ipr.save_image(blurred, default_name="blurred_output.png")
```

---

## 🧪 Modules & Features

### 1. Basic Operations ([`Basic operation/`](Basic%20operation/))

| Script | Topics Covered | Key OpenCV / NumPy Methods |
|---|---|---|
| [`Arithmatic_operation.py`](Basic%20operation/Arithmatic_operation.py) | Pixel-wise addition, weighted alpha blending | `cv.add`, `cv.addWeighted`, `cv.resize` |
| [`Color_generation.py`](Basic%20operation/Color_generation.py) | Custom RGB color canvas synthesis | `np.full`, `cv.cvtColor` |
| [`drawing.py`](Basic%20operation/drawing.py) | Drawing lines, rectangles, circles, text | `cv.line`, `cv.circle`, `cv.rectangle`, `cv.putText` |
| [`Edge_Detection.py`](Basic%20operation/Edge_Detection.py) | First & second derivative edge detectors | `cv.Sobel`, `cv.Laplacian`, `cv.Canny`, `cv.bilateralFilter` |
| [`Filtering.py`](Basic%20operation/Filtering.py) | Linear & non-linear smoothing / denoising | `cv.blur`, `cv.GaussianBlur`, `cv.medianBlur`, `cv.bilateralFilter` |
| [`Geo_tranformation.py`](Basic%20operation/Geo_tranformation.py) | Scaling, rotation, affine, perspective warp | `cv.warpAffine`, `cv.getRotationMatrix2D`, `cv.getPerspectiveTransform` |
| [`masking.py`](Basic%20operation/masking.py) | Bitwise ROI masking & masked histograms | `cv.bitwise_and`, `cv.rectangle`, `cv.calcHist` |
| [`Operation_of_Images.py`](Basic%20operation/Operation_of_Images.py) | Pixel indexing, ROI slicing, channel splitting | `cv.split`, `cv.merge`, NumPy array slicing |
| [`thresholding.py`](Basic%20operation/thresholding.py) | Global, Adaptive (Mean/Gaussian), Otsu | `cv.threshold`, `cv.adaptiveThreshold` |

### 2. Feature Extraction ([`Feature_Extraction/`](Feature_Extraction/))

| Script | Description | Highlights |
|---|---|---|
| [`GLCM.py`](Feature_Extraction/GLCM.py) | **Gray-Level Co-occurrence Matrix**: Texture feature extraction across multiple distances and angular orientations ($0, \pi/5, \pi/3, \pi/2, \pi$). | Uses `skimage.feature.graycomatrix` to quantify spatial relationships between pixel intensities. |
| [`histogram.py`](Feature_Extraction/histogram.py) | **Histogram Analysis & Equalization**: Generates 1D intensity and 3-channel RGB histograms, standard grayscale equalization, and manual 3-channel RGB equalization using cumulative distribution functions (CDF). | `cv.calcHist`, `cv.equalizeHist`, `np.cumsum`, `np.ma.masked_equal`. |
| [`kernel_operation.py`](Feature_Extraction/kernel_operation.py) | **Custom 2D Spatial Filtering**: Interactive kernel builder supporting dynamic dimension input for custom box blurring, uniform noise filtering, and high-pass sharpening filters. | `cv.filter2D`, dynamic matrix operations, integrated with `ipr.save_image()`. |

### 3. Image Formats & Color Spaces ([`Image Formats/`](Image%20Formats/))

| Script | Description | Supported Color Spaces |
|---|---|---|
| [`Color_Scale.py`](Image%20Formats/Color_Scale.py) | Interactive color space conversion and comparative visualizer. | **BGR**, **GRAY**, **YCrCb**, **YUV**, **HSV / HSV_FULL**, **HLS / HLS_FULL**, and **CIE LAB**. |

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
Installing with `-e` ensures that any edits made to `Local_library/ipress` take effect immediately across all scripts without reinstalling:
```bash
pip install -e Local_library
```

> **Note for VS Code users**: The included `.vscode/settings.json` already contains `"python.analysis.extraPaths": ["${workspaceFolder}/Local_library"]`. This guarantees full Pylance IntelliSense, autocomplete, and docstrings out of the box.

---

## 🛠️ Running the Scripts

Run any module directly from the terminal. Most scripts offer an interactive menu and launch a GUI file chooser:

```bash
# 1. Run color space conversions
python "Image Formats/Color_Scale.py"

# 2. Run histogram analysis and equalization
python "Feature_Extraction/histogram.py"

# 3. Run texture analysis via GLCM
python "Feature_Extraction/GLCM.py"

# 4. Run edge detection experiments
python "Basic operation/Edge_Detection.py"
```

---

## 🤝 Contributing

Contributions, questions, and feature suggestions are welcome! Feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/phantom2318/Image_processing).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
