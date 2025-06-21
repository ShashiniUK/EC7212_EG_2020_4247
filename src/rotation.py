# import cv2
# import numpy as np

# def rotate_image(image, angle):
#     """Rotate the given image by the specified angle without cropping"""

#     if len(image.shape) == 3:
#         height, width, _ = image.shape
#     else:
#         height, width = image.shape

#     center = (width // 2, height // 2)
#     rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

#     # Compute new bounding dimensions to prevent cropping
#     cos = abs(rotation_matrix[0, 0])
#     sin = abs(rotation_matrix[0, 1])
#     new_width = int((height * sin) + (width * cos))
#     new_height = int((height * cos) + (width * sin))

#     # Adjust the rotation matrix to account for translation
#     rotation_matrix[0, 2] += (new_width / 2) - center[0]
#     rotation_matrix[1, 2] += (new_height / 2) - center[1]

#     # Rotate the image
#     rotated = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))

#     return rotated


import cv2
import numpy as np

def rotate_image(image, angle):
    """Rotate image by specified angle with full canvas and replicated edges (no black corners)"""

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Compute rotation matrix and bounding box size
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    cos = np.abs(rot_mat[0, 0])
    sin = np.abs(rot_mat[0, 1])

    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    # Adjust transformation matrix to center
    rot_mat[0, 2] += (new_w / 2) - center[0]
    rot_mat[1, 2] += (new_h / 2) - center[1]

    # Rotate using BORDER_REPLICATE to avoid black corners
    rotated = cv2.warpAffine(image, rot_mat, (new_w, new_h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    return rotated
