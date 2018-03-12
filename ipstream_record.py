import cv2
from datetime import datetime

frame_width = 480
frame_height = 640

date = datetime.now()
time = date.time()
format_time = date.strftime('%H:%M:%S')

vid_title = date.date()
vid_title = str(vid_title) + "_" + format_time.replace(':','')

file_string = "/home/whaplescr/PycharmProjects/PiDashCam" \
              "/out/%s.avi"%(vid_title)

cap = cv2.VideoCapture('http://192.168.50.177:8081/frame.mjpg')
_fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter(file_string, _fourcc, 12,(frame_width,frame_height))

minute = 60
record_time = minute * 5

while True:
  ret, frame = cap.read()
  # frame_copy = frame

  out.write(frame)
  # cv2.imshow('Video', frame)#_copy)

  if cv2.waitKey(1) == 27:
    exit(0)

  time_diff = datetime.now() - date
  time_diff = time_diff.total_seconds()

  if time_diff >= record_time:
    cap.release()
    out.release()
    exit(0)

