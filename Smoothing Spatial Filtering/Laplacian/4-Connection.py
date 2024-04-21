import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 로드
image = cv2.imread('Smoothing Spatial Filtering\Laplacian\laplacian.jpeg', cv2.IMREAD_GRAYSCALE)  # 이미지 경로를 지정하세요.

# 라플라시안 커널 정의
kernel_a = np.array([[0, -1, 0],
                     [-1, 4, -1],
                     [0, -1, 0]], dtype=np.float32)

kernel_b = np.array([[0, 1, 0],
                     [1, -4, 1],
                     [0, 1, 0]], dtype=np.float32)

# 필터 적용
filtered_image_a = cv2.filter2D(image, -1, kernel_a)
filtered_image_b = cv2.filter2D(image, -1, kernel_b)

# 결과 이미지 표시
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(132)
plt.imshow(filtered_image_a, cmap='gray'), plt.title('Filter A Result')
plt.subplot(133)
plt.imshow(filtered_image_b, cmap='gray'), plt.title('Filter B Result')
plt.show()
