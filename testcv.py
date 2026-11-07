import cv2

cv2.namedWindow('im', cv2.WINDOW_NORMAL) # WINDOW_NORMAL 可调节窗口 WINDOW_AUTOSIZE 不可调节窗口
cv2.resizeWindow('im', 300, 200)
img = cv2.imread(r'C:/Users/nnnmm/Desktop/Study/openCV/R-C.jpg')
cv2.imshow('im', img)
key = cv2.waitKey(0)
print(key)
print('q')
print(ord('q'))
if (key == 'q'):
  cv2.destroyWindow('im')