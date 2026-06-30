import cv2

# Define grid boundaries
GRID_ROWS = 8
GRID_COLS = 8
HIGHLIGHT_COLOR = (255, 0, 0) # Blue in BGR

# Initial state holders
original_image = None
display_image = None
cell_height = 0
cell_width = 0

def mouse_callback(event, x, y, flags, param):
    global display_image
    
    if event == cv2.EVENT_LBUTTONDOWN:
        col = x // cell_width
        row = y // cell_height
        print(f"Clicked cell: Row={row}, Col={col} | Pixel coords: x={x}, y={y}")
        
        # Redraw configuration matrix clean plate
        display_image = original_image.copy()
        
        x1 = col * cell_width
        y1 = row * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        
        cv2.rectangle(display_image, (x1, y1), (x2, y2), HIGHLIGHT_COLOR, -1)
        cv2.addWeighted(display_image, 0.3, original_image, 0.7, 0, dst=display_image)
        draw_grid(display_image)
        
        cv2.putText(display_image, f"({row}, {col})", (x1 + 5, y1 + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow("Aerial Grid", display_image)

def draw_grid(img):
    h, w = img.shape[:2]
    # Vertical splits
    for i in range(1, GRID_COLS):
        x = i * (w // GRID_COLS)
        cv2.line(img, (x, 0), (x, h), (0, 255, 0), 1)
    # Horizontal splits
    for i in range(1, GRID_ROWS):
        y = i * (h // GRID_ROWS)
        cv2.line(img, (0, y), (w, y), (0, 255, 0), 1)

if __name__ == "__main__":
    original_image = cv2.imread("aerial_view.jpg")
    
    if original_image is None:
        print("Error: Could not load image.")
    else:
        display_image = original_image.copy()
        img_height, img_width = original_image.shape[:2]
        cell_width = img_width // GRID_COLS
        cell_height = img_height // GRID_ROWS
        
        draw_grid(display_image)
        cv2.namedWindow("Aerial Grid")
        cv2.imshow("Aerial Grid", display_image)
        cv2.setMouseCallback("Aerial Grid", mouse_callback)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()