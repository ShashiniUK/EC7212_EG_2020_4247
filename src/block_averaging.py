import cv2
import numpy as np

def block_average(image, block_size):
    """Replace non-overlapping blocks with their average value"""

    if len(image.shape) == 3:  # Color image
        height, width, channels = image.shape
        result = image.copy().astype(np.float32)

        for i in range(0, height - block_size + 1, block_size):
            for j in range(0, width - block_size + 1, block_size):
                block = image[i:i+block_size, j:j+block_size, :]
                for c in range(channels):
                    block_avg = np.mean(block[:, :, c])
                    result[i:i+block_size, j:j+block_size, c] = block_avg

    else:  # Grayscale image
        height, width = image.shape
        result = image.copy().astype(np.float32)

        for i in range(0, height - block_size + 1, block_size):
            for j in range(0, width - block_size + 1, block_size):
                block = image[i:i+block_size, j:j+block_size]
                block_avg = np.mean(block)
                result[i:i+block_size, j:j+block_size] = block_avg

    return result.astype(np.uint8)
