
import cv2
import numpy as np

def intensity_level_reduction(image, num_levels):
    if num_levels <= 0 or (num_levels & (num_levels - 1)) != 0:
        raise ValueError("Number of levels must be a positive power of 2")

    factor = 256 // num_levels

    if len(image.shape) == 3:  
        quantized_image = np.zeros_like(image)
        for channel in range(3):
            quantized_image[:, :, channel] = (image[:, :, channel] // factor) * factor
    else:  
        quantized_image = (image // factor) * factor

    return np.clip(quantized_image, 0, 255).astype(np.uint8)
