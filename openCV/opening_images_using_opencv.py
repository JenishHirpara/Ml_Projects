import cv2

img = cv2.imread('../numpy_images/pexels-monstera-5063470.jpg')

while True:
    cv2.imshow('Girl', img)
    # If we've waited at least 1 ms AND we've pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()