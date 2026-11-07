import cv2

# 创建 VideoWriter 对象
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
vw = cv2.VideoWriter('./video-save.mp4', fourcc, 20, (640, 480))

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow('video', 300, 200)


# 获取视频文件路径
cap = cv2.VideoCapture(0)

# while True:
# 判断摄像头是否为打开状态 - 在进入循环
while cap.isOpened():
  # 从视频文件中获取视频帧
  ret, frame = cap.read() 
  # 把视频帧显示在窗口
  cv2.imshow('video', frame)
  # 重新将窗口设为指定大小
  cv2.resizeWindow('video', 300, 200)
  # 写数据到多媒体文件
  if ret: # 判断读到了数据帧 - 在写入文件
    vw.write(frame)
  # 等待键盘事件，如果为q，退出
  key = cv2.waitKey(40)
  if key & 0xFF == ord('q'):
    break
# 释放摄像头资源
cap.release()
# 释放VideoWriter资源
vw.release()
# 销毁所有窗口
cv2.destroyAllWindows()