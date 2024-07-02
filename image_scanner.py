import cv2
from pyzbar import pyzbar

# Load the image
image = cv2.imread("test.jpg")

# Find the barcodes in the image
barcodes = pyzbar.decode(image)

# Loop over the detected barcodes
for barcode in barcodes:
    # Extract the barcode's type and data
    barcode_type = barcode.type
    barcode_data = barcode.data.decode("utf-8")
    
    # Print the results
    print("Type: ", barcode_type)
    print("Data: ", barcode_data)
    
    # Draw a rectangle around the barcode
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with the detected barcodes
cv2.imshow("Barcode Image", image)
cv2.waitKey(0)
