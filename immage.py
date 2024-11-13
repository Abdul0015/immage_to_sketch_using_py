import cv2 as cv

image = cv.imread("47626.jpg")

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

invert_image = cv.bitwise_not(gray_image)

blur_image = cv.GaussianBlur(invert_image, (21, 21), 0)

invert_blur = cv.bitwise_not(blur_image)

sketch = cv.divide(gray_image, invert_blur, scale=256.0)

cv.imwrite("Sketch4.png", sketch)
