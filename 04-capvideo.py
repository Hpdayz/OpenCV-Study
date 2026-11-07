import cv2

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)
# 获取视频设备，0表示第一个摄像头
cap = cv2.VideoCapture(0)
while True:
  # 从摄像头读取数据帧
  ret, frame = cap.read()
  # 将视频帧显示在窗口中
  cv2.imshow('video', frame)
  # 等待键盘事件，如果为q，退出
  key = cv2.waitKey(1)
  if(key & 0xFF == ord('q')):
    break

# 释放摄像头资源
cap.release()
# 销毁所有窗口
cv2.destroyAllWindows()