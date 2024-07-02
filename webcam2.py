import cv2
from pyzbar.pyzbar import decode

# Define global variable to store barcode data
barcode_data = ""

# Define function to capture and decode barcode
def decodeBarcode():
    global barcode_data
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        decoded_objs = decode(frame)
        for obj in decoded_objs:
            barcode_data = obj.data.decode('utf-8')
            print("Barcode Data:", barcode_data)
            return
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Call function to capture and decode barcode
decodeBarcode()
print("Global variable 'barcode_data' contains:", barcode_data)
