import cv2
from google.colab.patches import cv2_imshow

# Load image feed from drone camera
image = cv2.imread("drone_image.jpg")

if image is None:
    print("Error: Could not load image.")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Binary Thresholding isolates bright white structures (values > 200)
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    # Extract structural contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Approximate contour topology to polygon matching
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        
        # Check if polygon contour has 4 corners (rectangle/square)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, "Landing Pad", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print("Landing Pad Detected - Initiating Landing Sequence")
            print("Landing")
            
    # Save output image matrix copy
    cv2.imwrite("sahi.jpg", image)
    cv2_imshow(image)