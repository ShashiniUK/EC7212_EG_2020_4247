import cv2

def apply_averaging(image, kernel_size):
    if len(image.shape) == 3:  
        result = cv2.blur(image, (kernel_size, kernel_size))
    else:  
        result = cv2.blur(image, (kernel_size, kernel_size))
    return result
