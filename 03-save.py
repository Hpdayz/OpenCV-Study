import cv2
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('C:/Users/nnnmm/Desktop/Study/openCV/R-C.jpg')
cv2.imshow('img', img)
while True:
  key = cv2.waitKey(0)
  if(key == ord('q')):
    break
  elif(key == ord('s')):
    cv2.imwrite('C:/Users/nnnmm/Desktop/Study/openCV/R-C-save.jpg', img)
  
cv2.destoryAllWindows()