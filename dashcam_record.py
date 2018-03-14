import cv2
from datetime import datetime

frame_width = 480
frame_height = 640

date = datetime.now()
time = date.time()
format_time = date.strftime('%H:%M:%S')

vid_title = date.date()
vid_title = str(vid_title) + "_" + format_time.replace(':','')

file_string = "out/dashboard_camera/%s.avi"%(vid_title)

cap = cv2.VideoCapture('http://192.168.50.177:8081/frame.mjpg')
_fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter(file_string, _fourcc, 12,(frame_width,frame_height))

minutes = 5
record_time = minutes * 60

count = 0
while True:
  count += 1
  ret, frame = cap.read()

  out.write(frame)

  if cv2.waitKey(1) == 27:
    exit(0)

  time_diff = datetime.now() - date
  time_diff = time_diff.total_seconds()

  if time_diff >= record_time:
    cap.release()
    out.release()
    exit(0)

