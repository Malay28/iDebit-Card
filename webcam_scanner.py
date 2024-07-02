import cv2
from pyzbar import pyzbar


def scan_barcode():
    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find the barcodes in the frame
        barcodes = pyzbar.decode(gray)

        # Loop over the detected barcodes
        for barcode in barcodes:
            # Draw a rectangle around the barcode
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Get the data from the barcode
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            # Print the barcode data and type
            print("Barcode data: ", barcode_data)
            print("Barcode type: ", barcode_type)
            return

        # Display the frame
        cv2.imshow('Barcode Scanner', frame)

        # Wait for key press
        key = cv2.waitKey(1)

        # Exit if the 'q' key is pressed
        if key == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
scan_barcode()
