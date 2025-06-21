import cv2
import os
from src.intensity_reduction import intensity_level_reduction
from src.smoothing import apply_averaging
from src.rotation import rotate_image
from src.block_averaging import block_average


input_path = 'data/input.jpg'
image = cv2.imread(input_path)

if image is None:
    print(" Error: Could not load input image. Check the path or file name.")
    exit()

os.makedirs('results/intensity_reduction', exist_ok=True)
os.makedirs('results/smoothing', exist_ok=True)
os.makedirs('results/rotations', exist_ok=True)
os.makedirs('results/block_reduction', exist_ok=True)

intensity_levels = [2, 4, 8, 16, 32, 64, 128]
for level in intensity_levels:
    reduced = intensity_level_reduction(image, level)
    cv2.imwrite(f'results/intensity_reduction/{level}_levels.jpg', reduced)

kernel_sizes = [3, 10, 20]
for k in kernel_sizes:
    smoothed = apply_averaging(image, k)
    cv2.imwrite(f'results/smoothing/{k}x{k}.jpg', smoothed)

for angle in [45, 90]:
    rotated = rotate_image(image, angle)
    cv2.imwrite(f'results/rotations/rotated_{angle}.jpg', rotated)

block_sizes = [3, 5, 7]
for b in block_sizes:
    block_img = block_average(image, b)
    cv2.imwrite(f'results/block_reduction/{b}x{b}.jpg', block_img)
