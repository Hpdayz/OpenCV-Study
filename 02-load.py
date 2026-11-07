import cv2
cv2.nameWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('[path]')
cv2.imshow('img', img)
key = cv2.waitKey(0)
if(key == 'q'):
  exit()
cv2.destoryAllWindows()