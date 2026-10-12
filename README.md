# Image to Sketch Converter 🎨

A simple Python project that converts a normal image into a pencil sketch using **OpenCV**. This project was created while learning image processing and exploring computer vision techniques in Python.

## 📌 About the Project

The Image to Sketch Converter takes an input image and transforms it into a pencil sketch-style image using grayscale conversion, image inversion, Gaussian blur, and image division.

The final sketch is saved as a new PNG image.

## ✨ Features

- Converts a color image into a pencil sketch effect.
- Uses grayscale conversion to remove color information.
- Applies image inversion and Gaussian blur.
- Generates a sketch-style output image.
- Saves the resulting image in PNG format.
- Simple implementation using Python and OpenCV.

## 🛠️ Technologies Used

- **Python** — Programming language.
- **OpenCV (`cv2`)** — Image processing and computer vision.
- **NumPy** — Used internally by OpenCV for image array operations.

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your system.

Install OpenCV using pip:

```bash
pip install opencv-python
```

### Installation and Execution

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/Image-to-Sketch-Converter.git
```

Replace `YOUR-USERNAME` with your GitHub username and update the repository name if needed.

**2. Navigate to the project folder**

```bash
cd Image-to-Sketch-Converter
```

**3. Add your input image**

Place the image named `47626.jpg` in the same directory as your Python script.

**4. Run the Python script**

```bash
python sketch.py
```

Replace `sketch.py` with the actual name of your Python file.

**5. View the output**

After successful execution, the sketch will be saved as:

```text
Sketch4.png
```

## ⚙️ How It Works

The project uses the following image processing steps:

1. **Read the image:** Loads the input image using `cv.imread()`.
2. **Convert to grayscale:** Converts the color image into shades of gray.
3. **Invert the grayscale image:** Creates a negative version of the grayscale image.
4. **Apply Gaussian blur:** Smooths the inverted image to create a soft effect.
5. **Invert the blurred image:** Produces the inverted blur needed for the sketch effect.
6. **Create the sketch:** Divides the grayscale image by the inverted blurred image to generate the pencil sketch effect.
7. **Save the output:** Writes the final sketch to `Sketch4.png`.

## 💻 Code

```python
import cv2 as cv

image = cv.imread("47626.jpg")

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

invert_image = cv.bitwise_not(gray_image)

blur_image = cv.GaussianBlur(invert_image, (21, 21), 0)

invert_blur = cv.bitwise_not(blur_image)

sketch = cv.divide(gray_image, invert_blur, scale=256.0)

cv.imwrite("Sketch4.png", sketch)
```

## 🎯 What I Learned

Through this project, I practiced:

- Reading and saving images using OpenCV.
- Converting color images into grayscale.
- Understanding image inversion using bitwise operations.
- Applying Gaussian blur for image smoothing.
- Combining image processing techniques to create artistic effects.
- Saving processed images in different formats.

## 🔮 Future Improvements

- Allow users to select an image dynamically.
- Add a graphical user interface (GUI).
- Provide controls to adjust sketch intensity and blur.
- Support multiple image formats.
- Display the original and sketch images side by side.
- Add an option to save the output with a custom filename.

## 👨‍💻 Author

Created as a learning project while exploring Python, OpenCV, and image processing.

---

⭐ If you find this project interesting, feel free to star the repository!
