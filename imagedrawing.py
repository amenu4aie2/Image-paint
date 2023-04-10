import pyautogui
import time
import cv2

# Open Microsoft Paint
# pyautogui.press('win')
# pyautogui.typewrite('paint')
# pyautogui.press('enter')

# Wait for Paint to open
time.sleep(2)

# Set the canvas size
# pyautogui.hotkey('ctrl', 'w')
# pyautogui.typewrite(['right', 'right', 'down', 'down'])
# pyautogui.press('enter')
# set the canvas size to 488 277
# pyautogui.typewrite(['4', '8', '8', 'down', '2', '7', '7', 'enter'])

# # Select the large brush
# pyautogui.click(x=50, y=50)  # Click the "Brushes" button
# pyautogui.click(x=50, y=100)  # Click the "Size" button
# pyautogui.click(x=100, y=300)  # Click the large brush size

# Load the image
img = cv2.imread(
    r'C:\Users\cody\Downloads\imagedrawinig\yyy.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invert_img = 255 - gray_img

# Apply a Gaussian blur to the inverted image
blur_img = cv2.GaussianBlur(invert_img, (21, 21), 0)

# Blend the grayscale image and the blurred image to create a pencil sketch effect
pencil_sketch_img = cv2.divide(gray_img, 255 - blur_img, scale=256)
# SHOW THE IMAGE

# cv2.imshow('image', pencil_sketch_img)

# # # SAVE THE IMAGE
# cv2.imwrite('pencil_sketch_img.jpg', pencil_sketch_img)
# 488277488

#  S277
# et the starting position of the mouse cursor
x, y = 600, 300
pyautogui.moveTo(x, y)


# Iterate over each pixel of the pencil sketch image
for i in range(0, pencil_sketch_img.shape[0], 5):
    for j in range(0, pencil_sketch_img.shape[1], 5):

        # Calculate the grayscale value of the pixel
        gray_value = pencil_sketch_img[i, j]

        # Move the mouse cursor to the current pixel

        # Click the mouse to draw a point with the grayscale value as the color
        # if grey value is less than 128, then the color is black
        if gray_value < 251:
            pyautogui.moveTo(x+j, y+i)
            # double left click pyautogui
            pyautogui.doubleClick()

            # Hold down the left mouse button
            pyautogui.mouseDown(button='left')
            # move the mouse cursor to the next pixel
            pyautogui.moveRel(1, 0)
            # Release the left mouse button
            pyautogui.mouseUp(button='left')

        # Move the mouse cursor to the next pixel
        # pyautogui.moveRel(1, 0)

    # Move the mouse cursor to the next row
    pyautogui.moveRel(-pencil_sketch_img.shape[1], 1)
