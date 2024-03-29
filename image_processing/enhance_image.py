# This script will sharpen and enhance clarity on images to make text legible and readable without messing with the colors too much.
# This is useful for fixing screenshots on reports that are blurry.
# Make sure to run this: pip install opencv-python

import cv2
import numpy as np
import sys

def enhance_terminal_text(input_path, output_path):
    # Read the input image
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Image not found.")
        return

    # Convert the image to YCrCb color space
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Split the channels
    y, cr, cb = cv2.split(ycrcb)

    # Apply a mild sharpening to the Y channel
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    y_sharpened = cv2.filter2D(y, -1, kernel)

    # Merge the channels back
    merged = cv2.merge([y_sharpened, cr, cb])

    # Convert back to BGR color space
    final_image = cv2.cvtColor(merged, cv2.COLOR_YCrCb2BGR)

    # Save the processed image
    cv2.imwrite(output_path, final_image)
    print(f"Enhanced image saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python enhance_image.py input_path output_path")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    enhance_terminal_text(input_path, output_path)
