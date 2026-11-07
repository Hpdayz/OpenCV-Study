import cv2

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)
# 获取视频文件路径
cap = cv2.VideoCapture(r'C:\Users\nnnmm\Desktop\Study\openCV\05-video.mp4')

while True:
  # 从视频文件中获取视频帧
  ret, frame = cap.read()
  # 把视频帧显示在窗口
  cv2.imshow('video', frame)
  # 等待键盘事件，如果为q，退出
  key = cv2.waitKey(40)
  if key & 0xFF == ord('q'):
    break
# 释放视频文件资源
cap.release()
# 销毁所有窗口
cv2.destroyAllWindows()