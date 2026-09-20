import sys
from tkinter import Tk, filedialog
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

__all__ = ["select_image", "subplot"]


def select_image() -> str:
    """Open a file dialog to select an image path."""
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"),
            ("All files", "*.*"),
        ],
    )
    root.destroy()

    if not file_path:
        print("No image selected.")
        sys.exit()

    return file_path


def subplot(
    image1=None,
    image2=None,
    cmap1=None,
    cmap2=None,
    title1="Image-1",
    title2="Image-2",
):
    """Plot two images side by side."""
    if image1 is None:
        f_image1 = select_image()
        image1 = cv.imread(f_image1)
        if image1 is None:
            raise FileNotFoundError(f"Could not read image: {f_image1}")

    if cmap1 != "gray" and len(image1.shape) == 3:
        image1 = cv.cvtColor(image1, cv.COLOR_BGR2RGB)

    if image2 is None:
        f_image2 = select_image()
        image2 = cv.imread(f_image2)
        if image2 is None:
            raise FileNotFoundError(f"Could not read image: {f_image2}")

    if cmap2 != "gray" and len(image2.shape) == 3:
        image2 = cv.cvtColor(image2, cv.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image1, cmap=cmap1)
    plt.title(title1)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(image2, cmap=cmap2)
    plt.title(title2)
    plt.axis("off")

    plt.tight_layout()
    plt.show()